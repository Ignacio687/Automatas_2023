import unittest, pathlib
from main.resources import DataValidator, IncorrectFileFormat

class DataValidatorMainTests(unittest.TestCase):
    def initApp(self, path = None):
        if not path:
            path = pathlib.Path.cwd().joinpath("main").joinpath("data").joinpath("test_data.csv")
        app = DataValidator(path)
        return app

    def test_fileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main").joinpath("test").joinpath("data.csv"))
            app.validate()
    
    def test_InvalidDirectory(self):
        with self.assertRaises(NotADirectoryError):
            app = self.initApp(pathlib.Path.cwd().joinpath("test").joinpath("data.csv"))
            app.validate()

    def test_IsADirectoryError(self):
        with self.assertRaises(IsADirectoryError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main").joinpath("test"))
            app.validate()

    def test_IncorrectFileFormat(self):
        with self.assertRaises(IncorrectFileFormat):
            app = self.initApp(pathlib.Path.cwd().joinpath("main").joinpath("data").joinpath("test_data_false.doc"))
            app.validate()

    def test_NoErrorsInFile(self):
        self.assertEqual(self.initApp().validate(), {})

    def test_ErrorsInLines(self):
        self.assertEqual(self.initApp().validate, {})
    