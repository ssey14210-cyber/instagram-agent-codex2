import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(HERE, "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

import swipe


class TestSwipe(unittest.TestCase):
    def setUp(self):
        self.tsv_path = os.path.join(HERE, "..", "examples", "sample_swipe.tsv")
        self.formulas = swipe.load_formulas(swipe.HOOKS)

    def test_load_formulas(self):
        self.assertIsNotNone(self.formulas)
        self.assertGreaterEqual(len(self.formulas), 20)

    def test_read_rows(self):
        rows = swipe.read_rows(self.tsv_path)
        self.assertGreater(len(rows), 0)
        self.assertIn("views", rows[0])
        self.assertIn("hook", rows[0])

    def test_analyse_and_outlier(self):
        rows = swipe.read_rows(self.tsv_path)
        a = swipe.analyse(rows, self.formulas)
        self.assertIsNotNone(a)
        self.assertEqual(a["n"], len(rows))
        # Top reel has views 412,000 against median 11,000 -> outlier ~37.45x
        top = a["reels"][0]
        self.assertGreater(top["outlier"], 10.0)
        self.assertIsNotNone(top["formula"])

    def test_to_markdown(self):
        rows = swipe.read_rows(self.tsv_path)
        a = swipe.analyse(rows, self.formulas)
        md = swipe.to_markdown(a)
        self.assertIn("# Swipe file", md)
        self.assertIn("reels across", md)


if __name__ == "__main__":
    unittest.main()
