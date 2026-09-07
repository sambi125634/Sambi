#!/usr/bin/env python3
"""List video URLs from a YouTube channel, handle, or playlist — metadata only, no download.

Usage:
    python3 list_channel_videos.py <channel-or-playlist-url> [--limit N]

Accepts a channel URL in any form (https://youtube.com/@handle,
/channel/UC..., /c/name, /playlist?list=...) and prints a JSON array of
{"url", "title"} for its videos (newest first, as returned by YouTube),
using yt-dlp's flat playlist extraction (fast — no per-video metadata
fetch, no download).
"""
import argparse
import json
import subprocess
import sys


def ensure_ytdlp():
    try:
        import yt_dlp  # noqa: F401
        return True
    except ImportError:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--quiet", "yt-dlp"],
                check=True,
                timeout=120,
            )
            import yt_dlp  # noqa: F401
            return True
        except Exception:
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    if not ensure_ytdlp():
        print(json.dumps({"error": "yt-dlp not installable in this environment", "videos": []}))
        return

    url = args.url

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--flat-playlist",
        "--skip-download",
        "--playlist-end", str(args.limit),
        "--dump-json",
        url,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except Exception as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}", "videos": []}))
        return

    videos = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except Exception:
            continue
        vid = entry.get("id")
        if not vid:
            continue
        videos.append({
            "url": f"https://www.youtube.com/watch?v={vid}",
            "title": entry.get("title"),
        })

    result = {"videos": videos}
    if not videos:
        result["error"] = (proc.stderr.strip()[-800:] if proc.stderr else "no videos found")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
