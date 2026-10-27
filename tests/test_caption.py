import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(HERE, "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

import caption


class TestCaption(unittest.TestCase):
    def test_caption_valid(self):
        text = (
            "I lost $18,000 on one missing clause in a contract.\n\n"
            "Payment on delivery, not approval.\n\n"
            "Comment CONTRACT to get our proposal template.\n\n"
            "#freelance #contracts #agency"
        )
        res = caption.analyse(text, keywords=["proposal template"])
        self.assertIn(res["verdict"], ["READY", "REVIEW"])
        self.assertEqual(len(res["hashtags"]), 3)
        self.assertIn("comment a keyword", res["asks"])

    def test_caption_over_hashtag_cap(self):
        text = (
            "A short caption with too many hashtags.\n\n"
            "#one #two #three #four #five #six"
        )
        res = caption.analyse(text)
        fail_checks = [c for c in res["checks"] if c["check"] == "HASHTAGS" and c["status"] == "FAIL"]
        self.assertEqual(len(fail_checks), 1)
        self.assertEqual(res["verdict"], "FIX")

    def test_caption_dead_link_warning(self):
        text = "Visit https://example.com/guide for details."
        res = caption.analyse(text)
        link_checks = [c for c in res["checks"] if c["check"] == "LINKS" and c["status"] == "WARN"]
        self.assertEqual(len(link_checks), 1)

    def test_visible_window_cut(self):
        long_line = "A" * 150
        cut = caption.visible_window(long_line, 125)
        self.assertEqual(len(cut), 125)


if __name__ == "__main__":
    unittest.main()
