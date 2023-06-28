import unittest, pathlib
from main.resources import DataAnalyzer, IncorrectFileFormat

class DataAnalyzerMainTests(unittest.TestCase):
    def initApp(self, path = None):
        if not path:
            path = pathlib.Path.cwd().joinpath("main", "data", "test_files", "test_data.csv")
        app = DataAnalyzer(path)
        return app

    # 'validate' method tests:

    def test_fileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main", "test", "data.csv"))
            app.validate()
    
    def test_InvalidDirectory(self):
        with self.assertRaises(NotADirectoryError):
            app = self.initApp(pathlib.Path.cwd().joinpath("test", "data.csv"))
            app.validate()

    def test_IsADirectoryError(self):
        with self.assertRaises(IsADirectoryError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main", "test"))
            app.validate()

    def test_IncorrectFileFormat(self):
        with self.assertRaises(IncorrectFileFormat):
            app = self.initApp(pathlib.Path.cwd().joinpath("main", "data", "test_files", "test_data_false.doc"))
            app.validate()

    def test_NoErrorsInFile(self):
        self.assertEqual(self.initApp().validate(), {})

    def test_ErrorsInLines(self):
        erroresDict = {
            1: ["60a877,5AA0184E000001CA,d6104707df0cd3153,invitado-deca,192.168.24711,Wireles-802.11,2019--07,19:4608,20-03-13,11:2757,25a,39517b,505219c,DC-9F-DB12-F3-EA:HDD,DC-BF-E9-1-B5-D0,Usr-Request"],
            2: ["000000a19-00000379,69d4677fa7a8fe,Wireless-80211,12:46:a57,04-18-D6-C2-0A-F7:HC,A8-51-5B-68a-5D-F6,i dont know,,"],
            3: ["2019-14-26"]
        }
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files", "test_data_error.csv")
        self.assertEqual(self.initApp(path).validate(), {erroresDict})

    # 'generateFile' method tests:

    def test_generateFile(self):
        app = self.initApp()
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files")
        app.generateFile(path, ())
        self.assertTrue(path.joinpath("test_data_filtered.csv").exists())
        with open(path.joinpath("test_data.csv"), "r") as originalFile:
            with open(path.joinpath("test_data_filtered.csv")) as filteredFile:
                originalLines = originalFile.readlines()
                filteredLines = filteredFile.readlines()
        diff = set(originalLines).difference(set(filteredLines))
        self.assertEqual(diff, ())

    def test_generateFile_removeLines(self):
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files")
        app = self.initApp(path.joinpath("test_copyFile.csv"))
        app.generateFile(path, (2, 4))
        self.assertTrue(path.joinpath("test_data_filtered.csv").exists())
        with open(path.joinpath("test_data.csv"), "r") as originalFile:
            with open(path.joinpath("test_data_filtered.csv")) as filteredFile:
                originalLines = originalFile.readlines()
                filteredLines = filteredFile.readlines()
        diff = set(originalLines).difference(set(filteredLines))
        self.assertEqual(diff, ("Eliminate, me", "Also, me"))

    def test_generateFile_LinesIndexesOutOfRange(self):
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files")
        app = self.initApp(path.joinpath("test_copyFile.csv"))
        app.generateFile(path, (-5, 0, 2, 4, 6, 9))
        self.assertTrue(path.joinpath("test_data_filtered.csv").exists())
        with open(path.joinpath("test_data.csv"), "r") as originalFile:
            with open(path.joinpath("test_data_filtered.csv")) as filteredFile:
                originalLines = originalFile.readlines()
                filteredLines = filteredFile.readlines()
        diff = set(originalLines).difference(set(filteredLines))
        self.assertEqual(diff, ("Eliminate, me", "Also, me"))

    # 'filterUsers' method tests:

    