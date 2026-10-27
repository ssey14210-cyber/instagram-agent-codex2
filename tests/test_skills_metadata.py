import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(HERE, ".."))
AGENTS_SKILLS_DIR = os.path.join(BASE_DIR, ".agents", "skills")
REFERENCES_DIR = os.path.join(BASE_DIR, "references")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

EXPECTED_SKILLS = [
    "ig-audit",
    "ig-caption",
    "ig-carousel",
    "ig-comment",
    "ig-dm",
    "ig-human",
    "ig-plan",
    "ig-profile",
    "ig-reel",
    "ig-reply",
    "ig-repurpose",
    "ig-story",
    "ig-viral",
]

EXPECTED_SCRIPTS = [
    "beats.py",
    "caption.py",
    "detect.py",
    "hookscore.py",
    "humanize.py",
    "swipe.py",
]

EXPECTED_REFERENCES = [
    "hooks.json",
    "rubric.json",
    "slop.json",
]


class TestSkillsMetadata(unittest.TestCase):
    def test_all_13_skills_exist(self):
        for skill_name in EXPECTED_SKILLS:
            skill_dir = os.path.join(AGENTS_SKILLS_DIR, skill_name)
            skill_md = os.path.join(skill_dir, "SKILL.md")
            self.assertTrue(os.path.isdir(skill_dir), f"Directory missing: {skill_dir}")
            self.assertTrue(os.path.isfile(skill_md), f"SKILL.md missing: {skill_md}")

    def test_skills_frontmatter(self):
        frontmatter_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
        for skill_name in EXPECTED_SKILLS:
            skill_md = os.path.join(AGENTS_SKILLS_DIR, skill_name, "SKILL.md")
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
            match = frontmatter_re.match(content)
            self.assertIsNotNone(match, f"Missing YAML frontmatter in {skill_name}/SKILL.md")
            yaml_block = match.group(1)
            self.assertIn(f"name: {skill_name}", yaml_block)
            self.assertIn("description:", yaml_block)

    def test_no_stale_claude_paths_in_skills(self):
        for skill_name in EXPECTED_SKILLS:
            skill_md = os.path.join(AGENTS_SKILLS_DIR, skill_name, "SKILL.md")
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertNotIn("~/.claude", content, f"Found stale ~/.claude in {skill_name}/SKILL.md")
            self.assertNotIn(".claude/skills", content, f"Found stale .claude/skills in {skill_name}/SKILL.md")

    def test_references_valid_json(self):
        for ref in EXPECTED_REFERENCES:
            ref_path = os.path.join(REFERENCES_DIR, ref)
            self.assertTrue(os.path.isfile(ref_path), f"Missing reference: {ref_path}")
            with open(ref_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIsInstance(data, dict)

    def test_all_scripts_exist(self):
        for script in EXPECTED_SCRIPTS:
            script_path = os.path.join(SCRIPTS_DIR, script)
            self.assertTrue(os.path.isfile(script_path), f"Missing script: {script_path}")


if __name__ == "__main__":
    unittest.main()
