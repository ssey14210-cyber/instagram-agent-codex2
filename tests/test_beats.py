import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(HERE, "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

import beats


class TestBeats(unittest.TestCase):
    def test_analyse_script_basic(self):
        script = (
            "I lost $18,000 because of one missing contract.\n"
            "Here is the exact clause I put in every single agreement.\n"
            "Section 4. Payment on delivery, not on approval.\n"
            "Approval is a feeling. Delivery is a date.\n"
            "That one word change was worth $18,000 to me."
        )
        res = beats.analyse(script, wpm=165, target=30)
        self.assertIsNotNone(res)
        self.assertEqual(res["wpm"], 165)
        self.assertEqual(res["target"], 30)
        self.assertGreater(len(res["beats"]), 0)
        # Check first beat is HOOK
        self.assertEqual(res["beats"][0]["label"], "HOOK")
        # Check last beat is CTA
        self.assertEqual(res["beats"][-1]["label"], "CTA")
        # Check loop detection: last beat repeats $18,000 or 18,000
        self.assertTrue(any("Loops" in n for n in res["notes"]))

    def test_hook_too_long_flag(self):
        long_hook = (
            "Today I am going to walk you through a very detailed sixty second "
            "breakdown of how we scaled an agency to thirty clients in six months."
        )
        res = beats.analyse(long_hook, wpm=165)
        self.assertIsNotNone(res)
        self.assertTrue(any("hook runs" in f for f in res["beats"][0]["flags"]))

    def test_target_length_note(self):
        script = "Line one.\nLine two.\nLine three."
        res = beats.analyse(script, wpm=165, target=60)
        self.assertIsNotNone(res)
        self.assertTrue(any("under target" in n for n in res["notes"]))


if __name__ == "__main__":
    unittest.main()
