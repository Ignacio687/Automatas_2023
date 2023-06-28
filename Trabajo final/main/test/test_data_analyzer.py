import unittest, pathlib
from main.resources import DataAnalyzer

class DataAnalyzerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = DataAnalyzer(pathlib.Path.cwd().joinpath("data.csv"))

    def test_1(self):
        pass