import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(HERE, "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

import hookscore


class TestHookScore(unittest.TestCase):
    def test_strong_hook(self):
        hook = "I lost $18,000 because of one missing contract clause."
        results, overall, verdict, flags = hookscore.run(hook)
        self.assertGreaterEqual(overall, 70.0)
        self.assertEqual(verdict, "STRONG")
        self.assertEqual(len(flags), 0)
        self.assertIn("LENGTH", results)
        self.assertIn("SPECIFICITY", results)
        self.assertIn("STAKES", results)
        self.assertIn("FRONTLOAD", results)
        self.assertIn("ADDRESS", results)

    def test_dealbreaker_stop_scrolling(self):
        hook = "Stop scrolling if you want to grow on Instagram!"
        results, overall, verdict, flags = hookscore.run(hook)
        self.assertTrue(any("stop scrolling" in f.lower() for f in flags))
        self.assertNotEqual(verdict, "STRONG")

    def test_dealbreaker_greeting(self):
        hook = "Hey guys, today I want to talk about marketing."
        results, overall, verdict, flags = hookscore.run(hook)
        self.assertTrue(any("greeting" in f.lower() for f in flags))
        self.assertLess(overall, 50.0)
        self.assertEqual(verdict, "WEAK")

    def test_dealbreaker_emoji_and_hashtag(self):
        hook = "Save this right now 🔥 #marketing"
        results, overall, verdict, flags = hookscore.run(hook)
        self.assertTrue(any("emoji" in f.lower() for f in flags))
        self.assertTrue(any("hashtag" in f.lower() for f in flags))

    def test_weak_opener_penalty(self):
        hook = "So basically this tool helps you write better."
        results, overall, verdict, flags = hookscore.run(hook)
        score, detail = results["FRONTLOAD"]
        self.assertIn("weak opener", detail)


if __name__ == "__main__":
    unittest.main()
