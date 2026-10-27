import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(HERE, "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

import detect


class TestDetect(unittest.TestCase):
    def setUp(self):
        with open(detect.LEX, encoding="utf-8") as f:
            self.lex = json.load(f)

    def test_run_clean_text(self):
        clean_text = (
            "I lost $18,000 on a single contract clause last March. "
            "Most freelancers wait 30 days for payment approval. "
            "That's a huge mistake. "
            "We switched our terms to delivery rather than approval, and our cash flow turned positive within six weeks. "
            "Comment CONTRACT to get our one-page template."
        )
        results, overall, verdict = detect.run(clean_text, self.lex)
        self.assertGreater(overall, 60.0)
        self.assertIn(verdict, ["PASS", "REVIEW"])

    def test_run_dirty_text_flags(self):
        dirty_text = (
            "In today's fast-paced digital world, it is crucial to delve into robust content strategies — "
            "especially when navigating the algorithm. "
            "Furthermore, we must leverage seamless tools. "
            "It's not just about posting; it's about connecting. "
            "Stop scrolling and double tap if you agree!"
        )
        results, overall, verdict = detect.run(dirty_text, self.lex)
        self.assertLess(overall, 65.0)
        # Slop density should detect stock terms
        slop_score, detail = results["SLOP DENSITY"]
        self.assertIn("stock terms", detail)


if __name__ == "__main__":
    unittest.main()
