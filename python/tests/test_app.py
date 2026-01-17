import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from lib import load_data, validate_items, compute_summary


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.payload = load_data('data/sample.json')
        self.config = load_data('config.json')

    def test_summary_matches_expected(self):
        items = self.payload['items']
        rules = self.payload['rules']
        expected = self.payload['expected']

        issues = validate_items(items, rules, self.config['categories'])
        summary = compute_summary(items, self.config['categories'])

        self.assertEqual(summary.total_amount, expected['total_amount'])
        self.assertEqual(summary.avg_score, expected['avg_score'])
        self.assertEqual(summary.top_item, expected['top_item'])
        self.assertEqual(len(issues), expected['issue_count'])


if __name__ == '__main__':
    unittest.main()
