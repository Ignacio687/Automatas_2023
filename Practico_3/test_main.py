import unittest
from parameterized import parameterized
from main import PredictiveSyntaxAnalyzer, InvalidSyntax, InvalidCharacter

class PredictiveSyntaxAnalyzerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = PredictiveSyntaxAnalyzer()

    def test_emptystring(self):
        with self.assertRaises(InvalidSyntax):
            self.app.analyze("")

    @parameterized.expand(["+2$", "-2$", "%2$", "2++2$", "2--2$", 
                           "2%%2$", "()$", "2+$", "2-$", "2%$"])
    def test_invalidSyntax(self, param):
        with self.assertRaises(InvalidSyntax):
            self.app.analyze(param)

    @parameterized.expand(["2+a$", "2+2*b$", "8#4$", "8+8!$"])
    def test_invalidCharacter(self, param):
        with self.assertRaises(InvalidCharacter):
            self.app.analyze(param)

    @parameterized.expand(["10+5", "((90+5)+77)%3+22", "28876+28"])
    def test_validSyntax(self, param):
        self.assertTrue(self.app.analyze(param))

if __name__ == "__main__":
    unittest.main(failfast=True)