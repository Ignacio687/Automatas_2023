import unittest, pathlib
from main.resources import UserInterface

class UserInterfaceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = UserInterface()

    def test_1(self) -> None:
        pass