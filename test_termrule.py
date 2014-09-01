from tr import TermRule
import unittest


class TermRuleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = TermRule._parse_args()

    def test_with_empty_args(self):
        args = self.parser.parse_args([])
        self.assertEqual(args.color, None)
        self.assertEqual(args.symbol, [])

    def test_with_symbol(self):
        args = self.parser.parse_args(["*"])
        self.assertEqual(args.color, None)
        self.assertEqual(args.symbol, ['*'])

    def test_with_color(self):
        args = self.parser.parse_args(["-c=cyan"])
        self.assertEqual(args.color, ['cyan'])
        self.assertEqual(args.symbol, [])

    def test_with_color_symbol(self):
        args = self.parser.parse_args(["*", "-c=red"])
        self.assertEqual(args.symbol, ["*"])
        self.assertEqual(args.color, ["red"])

    def test_with_two_symbols(self):
        args = self.parser.parse_args(["*", "%"])
        self.assertEqual(args.symbol, ["*", "%"])


if __name__ == "__main__":
    unittest.main()
