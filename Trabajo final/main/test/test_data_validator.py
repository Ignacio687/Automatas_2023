import unittest, pathlib
from main.resources import DataValidator

class DataValidatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = DataValidator(pathlib.Path.cwd().joinpath("data.csv"))

    def test_1(self) -> None:
        pass