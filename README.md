# Instagram Agent (Codex Edition)

Thirteen agent skills that run an Instagram account: Reels off 26 scored hook formulas, a viral research skill, a caption linter, and a humanizer. Free, MIT, zero external dependencies.

This repository is a faithful, Codex-compatible port of the original [instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) created by [Jake Schincariol](https://opusjake.ai).

---

## What This Project Does

- **Reels Scripting (`ig-reel`)**: Generates scripts from raw ideas, selects and scores three candidate hooks from [26 formulas](references/hooks.json), crafts on-screen text cards, and produces timed beat sheets.
- **Viral Research (`ig-viral`)**: Gathers and ranks niche reels by outlier multiple over each account's own median view count, classifies hook formulas, and compiles an evidence-backed swipe file.
- **Caption Linting (`ig-caption`)**: Previews captions in the exact 125-character feed truncation box before the "... more" tap, checks search keywords, and enforces Instagram's 5-hashtag cap.
- **Slide Decks (`ig-carousel`)**: Architects high-dwell 1080x1350 carousels with 6-word covers, safe-zone layouts, and screenshot-worthy recap slides.
- **Daily Stories (`ig-story`)**: Sequences 3–7 daily story frames with high-conversion sticker placements (polls, question boxes) that feed directly into warm DM conversations.
- **Profile Optimization (`ig-profile`)**: Evaluates profiles against a [12-factor rubric](references/rubric.json) out of 100, then delivers step-by-step rewrites in fix-first priority order.
- **Content Planning (`ig-plan`)**: Builds a weekly schedule balancing Proof, Teaching, Opinion, Story, and Offer posts alongside a 10-account daily engagement list.
- **Fingerprint Removal & Humanizer (`ig-human`)**: Strips zero-width characters, BOMs, curly quotes, em dashes, and 154 stock AI phrases using [slop.json](references/slop.json), then evaluates drafts across a 5-check humanization panel.
- **Audits, Comments & DMs (`ig-audit`, `ig-comment`, `ig-reply`, `ig-dm`, `ig-repurpose`)**: Post-mortems based on retention and sends-per-reach, comment archetypes, inbound comment triage, non-spammy DMs, and long-form asset repurposing.

> [!IMPORTANT]
> **Human Approval Gate**: These skills draft, calculate, and lint. **You post.** This repository does not automate unauthorized browser actions, scraping, or posting.

---

## Repository Structure

```
instagram-agent-codex/
├── AGENTS.md                   # Codex project instructions & operational guide
├── README.md                   # Project documentation
├── LICENSE                     # MIT License (Jake Schincariol)
├── CONTRIBUTING.md             # Contribution guidelines
├── .gitignore                  # Git ignore rules for caches & data
├── .agents/
│   └── skills/                 # Codex-discoverable skill hierarchy
│       ├── ig-audit/           # Content audit post-mortem
│       ├── ig-caption/         # Caption writer & linter
│       ├── ig-carousel/        # Carousel slide copy & structure
│       ├── ig-comment/         # Outbound comment generator (9 types)
│       ├── ig-dm/              # Inbound/collab DM sequences
│       ├── ig-human/           # Text de-slopper & humanizer
│       ├── ig-plan/            # Weekly content calendar
│       ├── ig-profile/         # Profile 100-point audit & rewrites
│       ├── ig-reel/            # Reel script, hooks & beat sheet
│       ├── ig-reply/           # Inbound comment triage (6 buckets)
│       ├── ig-repurpose/       # Long-form to short-form repurposer
│       ├── ig-story/           # Daily story frame sequences
│       └── ig-viral/           # Outlier research & swipe ranker
├── scripts/                    # Zero-dependency CLI tools
│   ├── hookscore.py            # 5-property hook scoring panel
│   ├── beats.py                # Timed beat sheet generator
│   ├── caption.py              # Caption truncation linter
│   ├── detect.py               # 5-check AI detection panel
│   ├── humanize.py             # 3-pass machine fingerprint stripper
│   └── swipe.py                # TSV outlier multiple & hook ranker
├── references/                 # Core datasets and classification rubrics
│   ├── hooks.json              # 26 hook formulas, examples & regexes
│   ├── rubric.json             # 12-factor 100-point profile scoring rubric
│   └── slop.json               # 154 AI stock words, invisible characters & tells
├── templates/
│   └── voice.md                # Voice profile starter template
├── examples/                   # Sample inputs for testing & demonstration
└── tests/                      # Automated Python test suite
```

---

## Installation & Setup

### Requirements
- Python 3.8+ (Standard library only; no pip packages required)
- Any Codex-compatible agent runtime or terminal environment

### Setup
1. Clone or open this repository in your Codex workspace:
   ```bash
   git clone https://github.com/<your-username>/instagram-agent-codex.git
   cd instagram-agent-codex
   ```
2. Set up your voice profile:
   ```bash
   mkdir -p instagram
   cp templates/voice.md instagram/voice.md
   ```
   Fill in `instagram/voice.md` with your tone, background, audience, and off-limit topics. Every skill checks this profile to keep copy sounding authentic.

---

## Skill Discovery & Invocation

Codex automatically discovers skills under `.agents/skills/<skill-name>/SKILL.md`.

You can invoke skills conversationally in your agent session:
- *"Write a reel about why cold outreach failed for my consulting business."* &rarr; invokes `ig-reel`
- *"Lint this caption and check for keywords 'freelance design, client contracts'."* &rarr; invokes `ig-caption`
- *"Humanize this script and remove AI tells."* &rarr; invokes `ig-human`
- *"Score my profile and fix the bio."* &rarr; invokes `ig-profile`
- *"Rank this list of collected reels and build a swipe file."* &rarr; invokes `ig-viral`

---

## The Six Standalone Tools

All utilities are written in pure Python using only standard library modules.

### 1. Hook Scorer (`hookscore.py`)
Scores hooks out of 100 on five essential metrics: `LENGTH`, `SPECIFICITY`, `STAKES`, `FRONTLOAD`, and `ADDRESS`. Flags fatal openers (greetings, preambles, emojis, hashtags).
```bash
python3 scripts/hookscore.py examples/sample_hooks.txt
```
```
HOOK RANKING
==============================================================================
->  85.6 STRONG  Nobody tells you that your first 30 reels are supposed to flop
        weakest: SPECIFICITY (75)
    81.4 STRONG  I lost $18,000 because of one missing contract.
        weakest: ADDRESS (70)
    54.4 OK      Stop scrolling if you want to grow on Instagram in 2026 🔥
        weakest: STAKES (70)
        dealbreaker: Opens with "stop scrolling".
```

### 2. Beat Sheet Generator (`beats.py`)
Times speaking duration at ~165 wpm, flags beats exceeding 4.0 seconds, highlights runs of abstract lines, and verifies loop closures.
```bash
python3 scripts/beats.py examples/sample_script.txt --target 30
```
```
BEAT SHEET  ·  73 words  ·  ~26.6s at 165 wpm  ·  target 30.0s
========================================================================
  0:00.0   2.9s  HOOK    I lost $18,000 because of one missing contract.
  0:02.9  14.6s  MID     Here is the exact clause I now put in every single...
                         ^ 14.6s on one beat
  0:17.4   2.9s          Section 4. Payment on delivery, not on approval.
  0:20.4   2.9s          Approval is a feeling. Delivery is a date.
  0:23.3   3.3s  CTA     That one word change is worth $18,000 to me.
------------------------------------------------------------------------
  - Beat 2 runs past 4s. Either split the line or change what is on screen.
  - Loops: the last beat repeats "$18,000" from the hook.
```

### 3. Caption Linter (`caption.py`)
Renders the visual 125-character cut box as seen in mobile feeds, verifies the December 2025 5-hashtag cap, and flags unclickable links.
```bash
python3 scripts/caption.py examples/sample_caption.txt --keywords "client contracts,freelance pricing"
```
```
  WHAT THE FEED SHOWS
  +------------------------------------------------------+
  | I lost $18,000 because of one missing clause in a    |
  | contract, and the worst part is that I had read the  |
  | thing twice before I si                              |
  +-------------------------------------------- ... more +

  PASS  LENGTH            389 / 2200 characters
  WARN  FIRST LINE        133 characters, so it gets cut at 125 mid-thought
  PASS  HOOK IS CONCRETE  2 numbers or names in the visible window
  PASS  HASHTAGS          3 tags: #freelance #contracts #agencyowner
  PASS  ONE ASK           one call to action: comment a keyword
```

### 4. Humanizer (`humanize.py`)
Runs three deterministic cleaning passes: deletes zero-width and invisible characters, standardizes typography, and swaps 154 stock AI slop terms while reporting structural tells.
```bash
python3 scripts/humanize.py draft.txt -o clean.txt --report
```

### 5. AI Detection Panel (`detect.py`)
Computes local heuristic scores (0–100) across five dimensions: Burstiness, Specificity, Slop Density, Fingerprint, and Voice.
```bash
python3 scripts/detect.py before.txt after.txt
```
```
  BURSTINESS    ###################.....  78.4
  SPECIFICITY   #############...........  53.6
  SLOP DENSITY  ........................   0.0
  FINGERPRINT   ################........  68.7
  VOICE         #################.......  70.0
  ------------------------------------------------------------
  HUMAN SCORE   ###################.....  79.7   PASS    (+47.2)
```

### 6. Swipe File Outlier Ranker (`swipe.py`)
Ranks collected reels by outlier multiple (views / median), matches hooks against 26 formulas, and generates an evidence-backed swipe report.
```bash
python3 scripts/swipe.py examples/sample_swipe.tsv --out instagram/swipe.md
```

---

## Running the Test Suite

Run the full automated test suite using Python's built-in `unittest` runner:
```bash
python3 -m unittest discover tests
```

---

## What Was Migrated

- **Skill discovery**: Converted from Claude plugin and slash-command conventions (`~/.claude/`) to native Codex directory standards (`.agents/skills/` and `AGENTS.md`).
- **Path resolution**: Updated tools and skills to prioritize local workspace directories (`instagram/`, `references/`, `scripts/`) while maintaining backward-compatible fallbacks.
- **Cleaned configuration**: Removed Anthropic/Claude-specific plugin manifests (`.claude-plugin/`, `marketplace.json`, `plugin.json`) in favor of standard agent instructions.
- **Expanded test coverage**: Added an automated regression test suite in `tests/` covering all 6 Python utilities and validating all 13 skill metadata files.
- **Preserved core logic**: Kept 100% of the original scoring algorithms, formulas, weights, regex patterns, and rubric items intact.

---

## Platform Limitations & Ethics

- **Zero Unauthorized Automation**: Instagram's Terms of Use strictly prohibit automated posting, mass following, automated comment scraping, and bulk DM dispatching. Every skill in this pack operates as a local writing assistant; you copy and post the finished text yourself.
- **Honest Detection**: Heuristic detection scores measure pattern regularity and lexical tells; they do not guarantee "undetectable" output across proprietary third-party commercial detectors.
- **No Hallucinations**: Real numbers and genuine stories always outperform fabricated claims. If data is missing, the agent outputs `{{your number}}`.

---

## Attribution & License

- Original Author: [Jake Schincariol](https://opusjake.ai) ([Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill))
- License: [MIT License](LICENSE)
