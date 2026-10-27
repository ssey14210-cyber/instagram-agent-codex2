# AGENTS.md — Instagram Agent (Codex Edition)

## Project Overview

`instagram-agent-codex` is a faithful, Codex-compatible port of the Instagram Agent Skill pack. It equips AI agents with thirteen specialized skills and six local heuristic Python tools to manage, optimize, write, research, and audit an Instagram presence.

### Core Philosophy
1. **Human-in-the-loop**: The agent drafts, lints, and calculates. **The user posts.** No tool or skill automatically publishes to Instagram or bypasses user confirmation.
2. **Local, zero-dependency tools**: All six Python scripts execute locally using only the Python standard library. No external APIs, credentials, or network telemetry required.
3. **Evidence over assumptions**: Outlier multiples beat raw vanity view counts; retention graphs beat gut feeling; honest platform constraints beat outdated advice.
4. **No fabrication**: The agent never invents metrics, testimonials, or revenue figures. If data is unknown, it outputs `{{your number}}` and flags it for the user.

---

## Skill Inventory & Discovery

Skills are discoverable under `.agents/skills/<skill-name>/SKILL.md` (and mirrored in `skills/<skill-name>/SKILL.md`). When a user request matches a skill's purpose, activate the corresponding skill:

| Skill | Directory | Primary Purpose & Activation Triggers |
| --- | --- | --- |
| `ig-reel` | `.agents/skills/ig-reel/` | Turns an idea into a Reel script with 3 scored hook options, timed beat sheet, and on-screen text. Triggers on "write a reel", "script a reel", "hook for video". |
| `ig-viral` | `.agents/skills/ig-viral/` | Researches top niche reels, computes outlier multiples over account medians, identifies hook formulas, and builds a swipe file. Triggers on "find viral reels", "what's working in my niche". |
| `ig-caption` | `.agents/skills/ig-caption/` | Writes and lints captions against the 125-character feed truncation box, 5-hashtag cap, single ask, and keyword searchability. Triggers on "write caption", "caption linter", "hashtags". |
| `ig-carousel` | `.agents/skills/ig-carousel/` | Designs swipe posts (6–10 slides), 1080x1350 grid-safe layouts, 6-word covers, and recap slides. Triggers on "carousel", "swipe post", "slide deck". |
| `ig-story` | `.agents/skills/ig-story/` | Maps daily 3–7 frame story sequences with tactical sticker placement (polls, question boxes) to drive DM interactions. Triggers on "daily stories", "story sequence", "poll idea". |
| `ig-profile` | `.agents/skills/ig-profile/` | Scores profiles out of 100 against a 12-factor rubric (`references/rubric.json`) and delivers rewrites in fix-first order. Triggers on "audit my bio", "profile review", "optimize profile". |
| `ig-plan` | `.agents/skills/ig-plan/` | Architectures the weekly content mix (Proof, Teach, Opinion, Story, Offer) and the 10-account daily engagement list. Triggers on "plan my week", "content calendar". |
| `ig-human` | `.agents/skills/ig-human/` | Strips machine fingerprints (invisible characters, punctuation quirks, slop words) and runs a 5-check humanization panel. Triggers on "humanize", "remove AI tells", "de-slop". |
| `ig-comment` | `.agents/skills/ig-comment/` | Drafts high-value comments on other creators' posts using 9 specific comment archetypes. Triggers on "comment on this", "daily engagement comments". |
| `ig-reply` | `.agents/skills/ig-reply/` | Triages comments under user posts into 6 buckets (Keyword, Lead, Substance, Question, Support, Noise) and drafts public replies or Reel responses. Triggers on "reply to comments", "handle comments". |
| `ig-dm` | `.agents/skills/ig-dm/` | Crafts non-spammy DMs for keyword fulfillment, warm approaches, collab pitches, and strictly two follow-ups. Triggers on "DM outreach", "pitch collab", "keyword response". |
| `ig-repurpose` | `.agents/skills/ig-repurpose/` | Extracts standalone claims, mechanisms, numbers, and stories from long-form assets (podcasts, videos, articles) into a week of reels/carousels. Triggers on "repurpose podcast", "cut into reels". |
| `ig-audit` | `.agents/skills/ig-audit/` | Post-mortem on past performance using outlier multiples, non-follower reach, 3-second hold rate, and sends-per-reach. Triggers on "audit my posts", "why did this flop", "insights review". |

---

## Local Python Tools

The repository includes six standalone utilities in `scripts/` (and alongside their respective skills):

### 1. `hookscore.py` — Reel Hook Scoring Panel
Scores first lines against five core properties: `LENGTH`, `SPECIFICITY`, `STAKES`, `FRONTLOAD`, `ADDRESS`, and detects dealbreaker openers (e.g. "stop scrolling", greetings, emojis, hashtags).
```bash
# Rank multiple candidate hooks (one per line)
python3 scripts/hookscore.py hooks.txt

# Score a single hook directly
python3 scripts/hookscore.py --hook "I lost $18,000 on one missing contract."

# Emit structured JSON output
python3 scripts/hookscore.py hooks.txt --json
```

### 2. `beats.py` — Script Timing & Beat Sheet Analyzer
Estimates spoken duration based on words-per-minute (default 165 wpm), identifies long beats (>4.0s), detects abstract stretches, and checks for replay loops.
```bash
# Analyze a script
python3 scripts/beats.py script.txt

# Set target duration (e.g. 30 seconds)
python3 scripts/beats.py script.txt --target 30

# Adjust speaking pace
python3 scripts/beats.py script.txt --wpm 180 --target 45 --json
```

### 3. `caption.py` — Feed Truncation Preview & Caption Linter
Renders the visual 125-character box before "... more", enforces Instagram's 5-hashtag cap (effective Dec 2025), flags dead links, validates single calls to action, and verifies keyword presence.
```bash
# Basic caption lint
python3 scripts/caption.py caption.txt

# Verify presence of targeted search terms
python3 scripts/caption.py caption.txt --keywords "client proposals,agency pricing"

# Output as JSON
python3 scripts/caption.py caption.txt --json
```

### 4. `detect.py` — 5-Signal AI Detection Heuristic Panel
Evaluates drafts against five heuristics: Burstiness, Specificity, Slop Density, Fingerprint (invisible characters/typography), and Voice (contractions, personal pronouns, structural tells).
```bash
# Score a single draft
python3 scripts/detect.py draft.txt

# Compare before-and-after drafts
python3 scripts/detect.py before.txt after.txt

# Output JSON
python3 scripts/detect.py draft.txt --json
```

### 5. `humanize.py` — Three-Pass AI Fingerprint Removal
Pass 1: Removes invisible characters (zero-width spaces, BOMs, word joiners, soft hyphens).
Pass 2: Normalizes typography (em dash to comma, curly quotes to straight).
Pass 3: Replaces stock AI lexical items from `references/slop.json` while reporting structural tells for manual author rewriting.
```bash
# Clean draft and output to stdout
python3 scripts/humanize.py draft.txt

# Clean draft and output detailed stderr change report
python3 scripts/humanize.py draft.txt --report

# Save cleaned output to file
python3 scripts/humanize.py draft.txt -o clean.txt
```

### 6. `swipe.py` — Outlier Multiple Ranking & Hook Classifier
Ranks a TSV file of collected reels against account medians or follower counts, classifies hooks against the 26 formulas in `references/hooks.json`, and generates markdown swipe files.
```bash
# Analyze captured TSV
python3 scripts/swipe.py captured.tsv

# Generate markdown swipe file
python3 scripts/swipe.py captured.tsv --out instagram/swipe.md
```

---

## State and File Conventions

To ensure consistent project behavior across platforms:

1. **Voice Profile**: Stored in `instagram/voice.md` (or `~/.codex/instagram/voice.md`). Use `templates/voice.md` as the starting template.
2. **Swipe File**: Stored in `instagram/swipe.md`. Generated by `scripts/swipe.py`.
3. **Content Log**: Stored in `instagram/log.md`. Tracks published hook formulas and engagement history.
4. **Content Plan**: Stored in `instagram/plan.md`. Weekly calendar generated by `ig-plan`.
5. **Reference Data**:
   - `references/hooks.json`: 26 hook formulas, examples, traps, and regex match patterns.
   - `references/rubric.json`: 12-factor 100-point profile scoring rubric.
   - `references/slop.json`: 154 stock terms, 18 invisible classes, 11 typographic rules, and 16 structural tells.

---

## Operating Guidelines for AI Agents

1. **Always run tools rather than guessing**: When scoring a hook, timing a script, linting a caption, or checking humanization, invoke the Python scripts directly.
2. **Never claim 100% "undetectable" AI text**: The detection heuristics are local indicators, not guarantees against third-party commercial detector APIs.
3. **Respect current platform realities**:
   - Hashtag cap: 5 maximum (Instagram Dec 2025 update).
   - Feed truncation: ~125 characters.
   - Links: Not clickable in post captions; direct to bio, stories, or DMs.
4. **Output copy-ready blocks**: Present final content cleanly formatted in Markdown code blocks so the user can easily copy and paste it into Instagram.
