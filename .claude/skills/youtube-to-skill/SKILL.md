---
name: youtube-to-skill
description: Transcribe one or more YouTube videos — or every video from a pasted channel/playlist link — and turn the content into a new Claude skill under .claude/skills/, or fold it into an existing matching skill. Trigger automatically whenever the user pastes one or more youtube.com / youtu.be links (single video, channel handle like @name, /channel/, /c/, or a playlist) and asks to transcribe them, summarize them, or turn them into a skill — including Polish phrasing like "wrzucam link", "zrób z tego skilla", "zaktualizuj skilla", "transkrypcja z YT", "scrapuj kanał". Also trigger on a bare YouTube link with no extra instructions, since that is this project's whole workflow.
---

# YouTube → Claude Skill automation

This project's core workflow: the user pastes one or more YouTube links.
For each link, transcribe the video, extract the reusable knowledge/method
it teaches, and store that knowledge as a Claude skill in `.claude/skills/`
— updating an existing skill if the video's topic already has one, or
creating a new skill folder if it doesn't. Then commit the result.

Do this without asking for confirmation at each step (auto mode) — only
stop and ask the user when something is genuinely ambiguous (e.g. the video
could plausibly belong to two very different existing skills).

## Step 1 — Collect the links

Pull every YouTube URL out of the user's message (`youtube.com/watch?v=`,
`youtu.be/`, `/shorts/`, `/live/`).

**If a link is a channel or playlist instead of a single video**
(`youtube.com/@handle`, `/channel/UC...`, `/c/name`, `/playlist?list=...`),
expand it first:

```
python3 .claude/skills/youtube-to-skill/scripts/list_channel_videos.py "<url>" --limit 50
```

This prints `{"videos": [{"url": ..., "title": ...}, ...], "error": ...}`
using yt-dlp's flat-playlist mode (fast, no per-video download). Default
limit is 50 — for a channel, ask the user how many of the newest videos to
process if they haven't said, rather than assuming "all of them" (channels
can have hundreds). Then treat each returned `url` as an individual video
link and process it through steps 2-6.

Process every individual video link (from a direct link or an expanded
channel/playlist) in turn through steps 2-6.

## Step 2 — Fetch the transcript

Run:

```
python3 .claude/skills/youtube-to-skill/scripts/fetch_transcript.py "<url>"
```

This prints a JSON object with `video_id`, `title`, `channel`, `source`,
`language`, `transcript`, `error`. It first tries the lightweight
`youtube-transcript-api` (no download, just pulls the caption track), and
falls back to `yt-dlp`'s auto-generated subtitles if that fails. Both
require outbound network access to YouTube.

**If `transcript` is null / `error` is set:** most likely this session's
network policy blocks youtube.com (a 403 from the egress proxy), or the
video has no captions at all. Tell the user plainly what failed, and ask
them to either:
- paste the transcript/subtitles text directly, or
- run this in an environment that can reach YouTube (e.g. local Claude
  Code).

Do not silently give up — a missing transcript still means the user gets a
clear next step, not just an error message.

## Step 3 — Read and understand the transcript

Read the full transcript text. Identify:
- The core topic / domain (e.g. copywriting technique, a tool's workflow,
  a mental model, marketing framework, coding pattern).
- The concrete, reusable instructions or principles it teaches — not a
  summary of "what the video is about", but material another Claude
  session could actually follow to do the thing.
- Anything that's clearly filler, ads, or off-topic tangents — leave that
  out.

## Step 4 — Decide: update an existing skill, or create a new one

Run:

```
python3 .claude/skills/youtube-to-skill/scripts/list_skills.py
```

This lists every skill's directory name, `name`, and `description`. Compare
the video's topic against these descriptions.

- **Clear topical match** (e.g. a new video about Jim Edwards' copywriting
  templates and a `copywriting-secrets` skill already exists) → update that
  skill (Step 5).
- **No match, or the match is only superficial** → create a new skill
  (Step 6).
- **Genuinely ambiguous between two existing skills** → ask the user which
  one, in one short question.

## Step 5 — Update an existing skill

1. Edit `.claude/skills/<skill>/SKILL.md`: fold the new knowledge into the
   body where it fits thematically — don't just append a dated changelog
   entry. Merge it into the existing structure (add a new technique to a
   list, extend a framework section, etc.) so the skill reads as one
   coherent document, not a stitched-together log. Keep the frontmatter
   `description` accurate — widen it if the skill now covers more ground.
2. Save the full transcript as `.claude/skills/<skill>/references/<slug>.md`
   (slug derived from the video title), with a one-line header noting the
   source URL and video title. Only reference this file from SKILL.md if
   the raw transcript has ongoing value (verbatim scripts, exact wording to
   reuse) — otherwise the extracted knowledge in SKILL.md's body is enough
   and the reference file is just an archival record.

## Step 6 — Create a new skill

1. Pick a short kebab-case name describing the capability (not the video
   title) — e.g. `hook-writing-framework`, not `video-about-hooks`.
2. Create `.claude/skills/<name>/SKILL.md` with:
   - YAML frontmatter: `name` and a `description` written the same way as
     every skill in this file's own frontmatter — third person, states
     what it does AND when to trigger it, front-loads concrete trigger
     phrases/keywords a user would actually type.
   - A body that teaches the method/framework/knowledge extracted from the
     video, structured for someone applying it cold (headings, concrete
     steps or templates, not a prose recap of the video).
3. Save the transcript under `.claude/skills/<name>/references/<slug>.md`
   the same way as Step 5.2.

## Step 7 — Commit

Stage the new/changed files under `.claude/skills/` and commit with a
message naming the skill and, briefly, what was learned — e.g.
`Update copywriting-secrets skill with Jim Edwards video on bullet formulas`.
Push per this repo's branch instructions. Don't push work unrelated to the
skill files touched in this run.

## Step 8 — Tell the user what happened

One short summary per video: which skill was created or updated, and the
key points pulled from it. Skip restating the whole transcript back to them.
