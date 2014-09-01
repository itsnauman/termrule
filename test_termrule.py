from tr import TermRule
import unittest


class TermRuleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup the argparse parser"""
        cls.parser = TermRule._parse_args()

    def test_with_empty_args(self):
        """Test with no args"""
        args = self.parser.parse_args([])
        self.assertEqual(args.color, None)
        self.assertEqual(args.symbol, [])

    def test_with_symbol(self):
        """Test with one symbol, no color"""
        args = self.parser.parse_args(["*"])
        self.assertEqual(args.color, None)
        self.assertEqual(args.symbol, ['*'])

    def test_with_color(self):
        """Test with color only, default symbol"""
        args = self.parser.parse_args(["-c=cyan"])
        self.assertEqual(args.color, ['cyan'])
        self.assertEqual(args.symbol, [])

    def test_with_color_symbol(self):
        """Test with both symbol and color"""
        args = self.parser.parse_args(["*", "-c=red"])
        self.assertEqual(args.symbol, ["*"])
        self.assertEqual(args.color, ["red"])

    def test_with_two_symbols(self):
        """Test with multiple symbols"""
        args = self.parser.parse_args(["*", "%"])
        self.assertEqual(args.symbol, ["*", "%"])


if __name__ == "__main__":
    unittest.main()
