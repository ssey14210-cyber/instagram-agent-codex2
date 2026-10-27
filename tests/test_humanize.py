import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(HERE, "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

import humanize


class TestHumanize(unittest.TestCase):
    def setUp(self):
        self.lex = humanize.load_lexicon(humanize.LEX)

    def test_invisible_characters_removal(self):
        # zero-width space \u200b and byte-order mark \ufeff
        text = "Hello\u200b world\ufeff."
        clean, report = humanize.humanize(text, self.lex)
        self.assertNotIn("\u200b", clean)
        self.assertNotIn("\ufeff", clean)
        self.assertTrue(any("ZERO WIDTH" in h["name"] for h in report["invisible"]))

    def test_typographic_replacements(self):
        # em dash -> comma, curly quotes -> straight
        text = "This strategy—which works—is “great”."
        clean, report = humanize.humanize(text, self.lex)
        self.assertNotIn("—", clean)
        self.assertNotIn("“", clean)
        self.assertNotIn("”", clean)
        self.assertIn(",", clean)

    def test_slop_words_replacement(self):
        text = "We delve into robust solutions and leverage AI."
        clean, report = humanize.humanize(text, self.lex)
        self.assertNotIn("delve into", clean.lower())
        self.assertNotIn("leverage", clean.lower())
        self.assertTrue(len(report["lexical"]) > 0)

    def test_url_protection(self):
        text = "Check out https://example.com/delve-into-robustness for details."
        clean, report = humanize.humanize(text, self.lex)
        self.assertIn("https://example.com/delve-into-robustness", clean)

    def test_structural_tells_flagged(self):
        text = "It's not just about ideas, it's about execution.\nFollow for more!\nStop scrolling."
        clean, report = humanize.humanize(text, self.lex)
        self.assertTrue(len(report["structures"]) > 0)


if __name__ == "__main__":
    unittest.main()
