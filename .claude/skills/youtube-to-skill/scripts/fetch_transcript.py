#!/usr/bin/env python3
"""Fetch a YouTube video's transcript + basic metadata as plain text.

Usage:
    python3 fetch_transcript.py <youtube-url-or-id> [--lang en,pl]

Prints a JSON object to stdout:
    {
      "video_id": "...",
      "title": "..." | null,
      "channel": "..." | null,
      "source": "youtube_transcript_api" | "yt-dlp",
      "language": "en" | null,
      "transcript": "full plain text transcript",
      "error": null
    }

On failure, "transcript" is null and "error" explains what went wrong
(including the case where this environment cannot reach YouTube at all,
so the caller can fall back to asking the user for a manual transcript).
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import os
import glob


def extract_video_id(text: str) -> str:
    text = text.strip()
    patterns = [
        r"(?:v=|/videos/|embed/|youtu\.be/|/shorts/|/live/)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", text):
        return text
    raise ValueError(f"Could not extract a YouTube video ID from: {text!r}")


def ensure_package(pip_name: str, import_name: str = None):
    import_name = import_name or pip_name
    try:
        __import__(import_name)
        return True
    except ImportError:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--quiet", pip_name],
                check=True,
                timeout=120,
            )
            __import__(import_name)
            return True
        except Exception:
            return False


def via_transcript_api(video_id: str, langs):
    if not ensure_package("youtube-transcript-api", "youtube_transcript_api"):
        return None, "youtube-transcript-api not installable in this environment"

    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )

    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"

    chosen = None
    lang_used = None
    try:
        chosen = transcript_list.find_transcript(langs)
        lang_used = chosen.language_code
    except NoTranscriptFound:
        try:
            chosen = transcript_list.find_generated_transcript(langs)
            lang_used = chosen.language_code
        except NoTranscriptFound:
            for t in transcript_list:
                chosen = t
                lang_used = t.language_code
                break

    if chosen is None:
        return None, "No transcript track available for this video"

    try:
        fetched = chosen.fetch()
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"

    snippets = fetched.snippets if hasattr(fetched, "snippets") else fetched
    lines = []
    for s in snippets:
        text = s.text if hasattr(s, "text") else s.get("text", "")
        text = text.strip()
        if text:
            lines.append(text)
    full_text = " ".join(lines)
    return {"text": full_text, "language": lang_used}, None


def via_ytdlp(video_id: str, langs):
    if not ensure_package("yt-dlp", "yt_dlp"):
        return None, None, "yt-dlp not installable in this environment"

    url = f"https://www.youtube.com/watch?v={video_id}"
    with tempfile.TemporaryDirectory() as tmp:
        out_tmpl = os.path.join(tmp, "%(id)s.%(ext)s")
        cmd = [
            sys.executable, "-m", "yt_dlp",
            "--skip-download",
            "--write-auto-sub", "--write-sub",
            "--sub-lang", ",".join(langs) + ".*",
            "--sub-format", "vtt",
            "--dump-json",
            "-o", out_tmpl,
            url,
        ]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        except Exception as e:
            return None, None, f"{type(e).__name__}: {e}"

        meta = None
        if proc.stdout.strip():
            try:
                meta = json.loads(proc.stdout.strip().splitlines()[-1])
            except Exception:
                meta = None

        vtt_files = sorted(glob.glob(os.path.join(tmp, "*.vtt")))
        if not vtt_files:
            err = proc.stderr.strip()[-800:] if proc.stderr else "no subtitle file produced"
            return None, meta, err

        vtt_path = vtt_files[0]
        lang_match = re.search(r"\.([a-zA-Z-]+)\.vtt$", os.path.basename(vtt_path))
        lang_used = lang_match.group(1) if lang_match else None

        with open(vtt_path, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()

        text = vtt_to_text(raw)
        return {"text": text, "language": lang_used}, meta, None


def vtt_to_text(raw: str) -> str:
    lines = raw.splitlines()
    out = []
    last = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            continue
        if re.fullmatch(r"\d+", line):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = re.sub(r"\[.*?\]", "", line).strip()
        if not line:
            continue
        if line == last:
            continue
        out.append(line)
        last = line
    return " ".join(out)


def fetch_metadata_ytdlp(video_id: str):
    if not ensure_package("yt-dlp", "yt_dlp"):
        return None
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = [sys.executable, "-m", "yt_dlp", "--skip-download", "--dump-json", url]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if proc.stdout.strip():
            return json.loads(proc.stdout.strip().splitlines()[-1])
    except Exception:
        pass
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--lang", default="en,pl", help="comma-separated language preference order")
    args = parser.parse_args()

    langs = [l.strip() for l in args.lang.split(",") if l.strip()]

    result = {
        "video_id": None,
        "title": None,
        "channel": None,
        "source": None,
        "language": None,
        "transcript": None,
        "error": None,
    }

    try:
        video_id = extract_video_id(args.url)
    except ValueError as e:
        result["error"] = str(e)
        print(json.dumps(result, ensure_ascii=False))
        return

    result["video_id"] = video_id

    data, err = via_transcript_api(video_id, langs)
    if data:
        result["source"] = "youtube_transcript_api"
        result["language"] = data["language"]
        result["transcript"] = data["text"]
    else:
        yt_data, meta, yt_err = via_ytdlp(video_id, langs)
        if yt_data:
            result["source"] = "yt-dlp"
            result["language"] = yt_data["language"]
            result["transcript"] = yt_data["text"]
        else:
            result["error"] = f"transcript_api: {err} | yt-dlp: {yt_err}"

    meta = fetch_metadata_ytdlp(video_id)
    if meta:
        result["title"] = meta.get("title")
        result["channel"] = meta.get("channel") or meta.get("uploader")

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
