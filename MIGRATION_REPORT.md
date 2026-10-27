# Migration Report: Instagram Agent Skill to Codex

**Project Objective**: Migrate `instagram-agent-skill` (Claude-specific skill pack) to `instagram-agent-codex` (Codex-compatible repository).  
**Source Repository**: [https://github.com/Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill)  
**Inspected Source Revision**: Commit `d03c56bb598be770c60b201f94237e5d1a4268a6` (2026-09-13T14:10:29Z)  
**Target Repository**: `instagram-agent-codex`  
**License**: MIT (Jake Schincariol)  

---

## 1. Inventory & Files Migrated

### Source Inventory vs Target Inventory

| Source Path (Original) | Target Path (Codex) | Status | Notes |
| --- | --- | --- | --- |
| `skills/ig-audit/SKILL.md` | `.agents/skills/ig-audit/SKILL.md` | Migrated | Updated config paths to `instagram/log.md` |
| `skills/ig-caption/SKILL.md` | `.agents/skills/ig-caption/SKILL.md` | Migrated | Preserved feed truncation & 5-hashtag rules |
| `skills/ig-caption/caption.py` | `scripts/caption.py` & `.agents/skills/ig-caption/caption.py` | Migrated | Added cross-platform UTF-8 console output |
| `skills/ig-carousel/SKILL.md` | `.agents/skills/ig-carousel/SKILL.md` | Migrated | Preserved 1080x1350 grid safe zone rules |
| `skills/ig-comment/SKILL.md` | `.agents/skills/ig-comment/SKILL.md` | Migrated | Updated log path to `instagram/log.md` |
| `skills/ig-dm/SKILL.md` | `.agents/skills/ig-dm/SKILL.md` | Migrated | Preserved 3 DM types and 2-follow-up limit |
| `skills/ig-human/SKILL.md` | `.agents/skills/ig-human/SKILL.md` | Migrated | Preserved 5-check panel & structural tells |
| `skills/ig-human/detect.py` | `scripts/detect.py` & `.agents/skills/ig-human/detect.py` | Migrated | Dynamic path resolution for `slop.json`, UTF-8 output |
| `skills/ig-human/humanize.py` | `scripts/humanize.py` & `.agents/skills/ig-human/humanize.py` | Migrated | Dynamic path resolution for `slop.json`, UTF-8 output |
| `skills/ig-human/slop.json` | `references/slop.json` & `.agents/skills/ig-human/slop.json` | Migrated | 154 stock terms, 18 invisible classes, 16 tells |
| `skills/ig-plan/SKILL.md` | `.agents/skills/ig-plan/SKILL.md` | Migrated | Updated path to `instagram/plan.md` |
| `skills/ig-profile/SKILL.md` | `.agents/skills/ig-profile/SKILL.md` | Migrated | Preserved 12-factor 100-point rubric |
| `skills/ig-profile/rubric.json` | `references/rubric.json` & `.agents/skills/ig-profile/rubric.json` | Migrated | 100-point profile scoring rubric |
| `skills/ig-reel/SKILL.md` | `.agents/skills/ig-reel/SKILL.md` | Migrated | Updated path to `instagram/voice.md` & `log.md` |
| `skills/ig-reel/beats.py` | `scripts/beats.py` & `.agents/skills/ig-reel/beats.py` | Migrated | Added cross-platform UTF-8 console output |
| `skills/ig-reel/hookscore.py` | `scripts/hookscore.py` & `.agents/skills/ig-reel/hookscore.py` | Migrated | Added cross-platform UTF-8 console output |
| `skills/ig-reel/hooks.json` | `references/hooks.json` & `.agents/skills/ig-reel/hooks.json` | Migrated | 26 hook formulas, examples, regex matchers |
| `skills/ig-reply/SKILL.md` | `.agents/skills/ig-reply/SKILL.md` | Migrated | Preserved comment triage buckets & Reel replies |
| `skills/ig-repurpose/SKILL.md` | `.agents/skills/ig-repurpose/SKILL.md` | Migrated | Preserved long-form extraction rules |
| `skills/ig-story/SKILL.md` | `.agents/skills/ig-story/SKILL.md` | Migrated | Preserved daily story sequencing & stickers |
| `skills/ig-viral/SKILL.md` | `.agents/skills/ig-viral/SKILL.md` | Migrated | Updated output path to `instagram/swipe.md` |
| `skills/ig-viral/swipe.py` | `scripts/swipe.py` & `.agents/skills/ig-viral/swipe.py` | Migrated | Dynamic path resolution for `hooks.json` and `hookscore` |
| `templates/voice.md` | `templates/voice.md` | Migrated | Updated guidance for Codex |
| `.claude-plugin/` | *Removed* | Removed | Replaced by Codex standard `.agents/skills/` & `AGENTS.md` |
| `.gitignore` | `.gitignore` | Migrated | Enhanced for Python virtualenvs, caches & runtime logs |
| `LICENSE` | `LICENSE` | Preserved | Retained original 2026 MIT License by Jake Schincariol |
| `README.md` | `README.md` | Rewritten | Full Codex documentation, examples & architecture |
| *(None in source)* | `AGENTS.md` | Added | Project instructions and operational rules for Codex |
| *(None in source)* | `CONTRIBUTING.md` | Added | Contribution guidelines |
| *(None in source)* | `examples/` | Added | 6 realistic sample files for testing |
| *(None in source)* | `tests/` | Added | Automated unit and integration test suite |

---

## 2. Claude Components Removed

1. **Claude Plugin Directory (`.claude-plugin/`)**:
   - `marketplace.json`: Removed schema reference to `https://anthropic.com/claude-code/marketplace.schema.json`.
   - `plugin.json`: Removed Anthropic plugin descriptor.
2. **Claude-Specific File Paths (`~/.claude/instagram/`)**:
   - Original instructions hardcoded `~/.claude/instagram/voice.md`, `swipe.md`, `log.md`, and `plan.md`.
   - Replaced with workspace-relative default paths: `instagram/voice.md`, `instagram/swipe.md`, `instagram/log.md`, and `instagram/plan.md` (with fallback to `~/.codex/instagram/`).
3. **Claude Code Installation & Slash Command Setup**:
   - Removed instructions referencing `cp -r ... ~/.claude/skills/`, `/plugin marketplace add...`, `/plugin install...`, and "Paste this into Claude".
   - Replaced with standard Codex project cloning, skill discovery under `.agents/skills/`, and conversational skill invocation.

---

## 3. Codex Equivalents Implemented

1. **Codex Skill Discovery Structure**:
   - All 13 skills are located in `.agents/skills/<skill-name>/SKILL.md` with complete YAML frontmatter (`name`, `description`).
   - Backward-compatible mirror created at root `skills/<skill-name>/`.
2. **`AGENTS.md` Root Instruction Specification**:
   - Contains complete project capabilities, discovery guidelines, CLI execution syntax, operating rules, safety boundaries, and validation workflows.
3. **Central `scripts/` and `references/` Architecture**:
   - Standalone CLI utilities consolidated into `scripts/`.
   - Reference datasets (`hooks.json`, `rubric.json`, `slop.json`) placed in `references/`.
   - Dynamic path discovery implemented in `detect.py`, `humanize.py`, and `swipe.py` so scripts run smoothly from any directory.
4. **Cross-Platform UTF-8 Console Support**:
   - Added standard library `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` to avoid Windows cp1252 character mapping errors on emojis and unicode punctuation.

---

## 4. Preservation of Original Algorithms and Scoring Logic

- **Hook Scoring Weights**: 60% mean, 40% minimum check score, -15 penalty per dealbreaker. Exactly preserved.
- **Beat Sheet Timing**: 165 wpm default, 3.0s hook window, 4.0s max beat, 3-beat abstract run, loop detection. Exactly preserved.
- **Caption Linter Thresholds**: 2200 char hard limit, 125 char feed truncation, 5 hashtag maximum (Dec 2025 rule), 4% emoji density warning. Exactly preserved.
- **AI Detection Panel**: 60% mean, 40% minimum check score, human/machine scaling equations for Burstiness (0.70/0.22), Specificity (6.0/0.5), Slop (0.0/4.0), Fingerprint (0.0/12.0), and Voice. Exactly preserved.
- **Humanizer Cleaning Sequence**: Pass 1 (Invisible characters) -> Pass 2 (Typography) -> Pass 3 (Lexical slop) -> Capital restoration -> URL restoration -> Structural tells report. Exactly preserved.
- **Swipe Outlier Calculation**: `views / baseline` (account median or follower count), formula matching against regexes in `hooks.json`. Exactly preserved.

---

## 5. Tests Executed & Actual Results

Test Suite Command:
```bash
py -3 -m unittest discover tests -v
```

### Execution Log (Actual Output):
```
test_analyse_script_basic (test_beats.TestBeats.test_analyse_script_basic) ... ok
test_hook_too_long_flag (test_beats.TestBeats.test_hook_too_long_flag) ... ok
test_target_length_note (test_beats.TestBeats.test_target_length_note) ... ok
test_caption_dead_link_warning (test_caption.TestCaption.test_caption_dead_link_warning) ... ok
test_caption_over_hashtag_cap (test_caption.TestCaption.test_caption_over_hashtag_cap) ... ok
test_caption_valid (test_caption.TestCaption.test_caption_valid) ... ok
test_visible_window_cut (test_caption.TestCaption.test_visible_window_cut) ... ok
test_run_clean_text (test_detect.TestDetect.test_run_clean_text) ... ok
test_run_dirty_text_flags (test_detect.TestDetect.test_run_dirty_text_flags) ... ok
test_dealbreaker_emoji_and_hashtag (test_hookscore.TestHookScore.test_dealbreaker_emoji_and_hashtag) ... ok
test_dealbreaker_greeting (test_hookscore.TestHookScore.test_dealbreaker_greeting) ... ok
test_dealbreaker_stop_scrolling (test_hookscore.TestHookScore.test_dealbreaker_stop_scrolling) ... ok
test_strong_hook (test_hookscore.TestHookScore.test_strong_hook) ... ok
test_weak_opener_penalty (test_hookscore.TestHookScore.test_weak_opener_penalty) ... ok
test_invisible_characters_removal (test_humanize.TestHumanize.test_invisible_characters_removal) ... ok
test_slop_words_replacement (test_humanize.TestHumanize.test_slop_words_replacement) ... ok
test_structural_tells_flagged (test_humanize.TestHumanize.test_structural_tells_flagged) ... ok
test_typographic_replacements (test_humanize.TestHumanize.test_typographic_replacements) ... ok
test_url_protection (test_humanize.TestHumanize.test_url_protection) ... ok
test_all_13_skills_exist (test_skills_metadata.TestSkillsMetadata.test_all_13_skills_exist) ... ok
test_all_scripts_exist (test_skills_metadata.TestSkillsMetadata.test_all_scripts_exist) ... ok
test_no_stale_claude_paths_in_skills (test_skills_metadata.TestSkillsMetadata.test_no_stale_claude_paths_in_skills) ... ok
test_references_valid_json (test_skills_metadata.TestSkillsMetadata.test_references_valid_json) ... ok
test_skills_frontmatter (test_skills_metadata.TestSkillsMetadata.test_skills_frontmatter) ... ok
test_analyse_and_outlier (test_swipe.TestSwipe.test_analyse_and_outlier) ... ok
test_load_formulas (test_swipe.TestSwipe.test_load_formulas) ... ok
test_read_rows (test_swipe.TestSwipe.test_read_rows) ... ok
test_to_markdown (test_swipe.TestSwipe.test_to_markdown) ... ok

----------------------------------------------------------------------
Ran 28 tests in 0.067s

OK
```

All 28 tests executed and passed with 0 failures and 0 errors.

---

## 6. Manual Steps & GitHub Publishing

To publish the migrated repository to GitHub:

```bash
cd "C:\Users\rohit\.gemini\antigravity-ide\scratch\instagram-agent-codex"

# If not already initialized:
git init
git add .
git commit -m "Initial commit: port Instagram Agent Skills to Codex"

# Create and push to remote (using GitHub CLI or manual remote):
# Option A: via GitHub CLI (gh)
gh repo create instagram-agent-codex --public --source=. --remote=origin --push

# Option B: via existing remote URL
git remote add origin https://github.com/<your-username>/instagram-agent-codex.git
git branch -M main
git push -u origin main
```
