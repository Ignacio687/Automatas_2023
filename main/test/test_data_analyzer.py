import unittest, pathlib, os
from parameterized import parameterized
from main.resources import DataAnalyzer, IncorrectFileExtensionError, modeIndexOutOfRangeError

class DataAnalyzerMainTests(unittest.TestCase):
    def initApp(self, path = None):
        if not path:
            path = pathlib.Path.cwd().joinpath("main", "data", "test_files", "test_data.csv")
        app = DataAnalyzer(str(path))
        return app

    # 'validate' method tests:

    def test_validate_fileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main", "test", "data.csv"))
            app.validate()

    def test_validate_IsADirectoryError(self):
        with self.assertRaises(IsADirectoryError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main", "test"))
            app.validate()

    def test_validate_IncorrectFileExtension(self):
        with self.assertRaises(IncorrectFileExtensionError):
            app = self.initApp(pathlib.Path.cwd().joinpath("main", "data", "test_files", "test_data_false.doc"))
            app.validate()

    def test_validate_NoErrorsInFile(self):
        self.assertEqual(self.initApp().validate(), {})

    def test_validate_ErrorsInLines(self):
        erroresDict = {
            2: ("ID", "60a877"),
            3: ('Tipo__conexión', 'Wireless-80211'),
            4: ("Inicio_de_Conexión_Dia", "2019-14-26"),
            5: ("IP_NAS_AP", "Wireless-802.11"),
            6: ("ID_Conexión_unico", "invitado-deca")
        }
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files", "test_data_error.csv")
        self.assertEqual(self.initApp(path).validate(), erroresDict)

    # 'expValidation' method tests:

    @parameterized.expand([-1, 20,])
    def test_expValidation(self, mode):
        with self.assertRaises(modeIndexOutOfRangeError):
            app = self.initApp()
            app.expValidation("", mode)

    @parameterized.expand(["605055", "1616268", "890150"])
    def test_expValidation_ID(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 0))

    @parameterized.expand(["605a55", "161626*", ""])
    def test_expValidation_ID_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 0))

    @parameterized.expand(["5C9CAF5E-00000EAC", "3E32A6CDB36F8B0B", "60F18D74-0000312E"])
    def test_expValidation_ID_Sesion(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 1))

    @parameterized.expand(["5C9CAF5E-0000GEAC", "-3E32A6CDB36F8B0B", "60F18D74-000312E-", "60F18D74-0000312E8"])
    def test_expValidation_ID_Sesion_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 1))

    @parameterized.expand(["ae9e2a3429a0e537", "0ff79346fcc34ada", "07f2e67b15fc9eab"])
    def test_expValidation_ID_Conexión_unico(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 2))

    @parameterized.expand(["ae9e2a3429a0e5372", "0ff79", "07f2e67b15fc9eag"])
    def test_expValidation_ID_Conexión_unico_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 2))
   
    @parameterized.expand(["invitado-deca", "rezle-", "txenaziattrdu"])
    def test_expValidation_Usuario(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 3))

    @parameterized.expand(["invitado-deca*", "", "txenaziattrdu "])
    def test_expValidation_Usuario_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 3))

    @parameterized.expand(["192.168.247.14", "255.255.255.255", "0.0.0.0"])
    def test_expValidation_IP_NAS_AP(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 4))

    @parameterized.expand(["192.168.247.1454", "255.255.255.256", "0.0.0"])
    def test_expValidation_IP_NAS_AP_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 4))

    @parameterized.expand(["Wireless-802.11",])
    def test_expValidation_Tipo__conexión(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 5))

    @parameterized.expand(["Wireless-802.11a", ""])
    def test_expValidation_Tipo__conexión_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 5))

    @parameterized.expand(["2023-02-09", "2019-11-06", "2020-11-26"])
    def test_expValidation_Inicio_de_Conexión_Dia(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 6))

    @parameterized.expand(["2023-02-59", "202-02-09", "2023/02/09"])
    def test_expValidation_Inicio_de_Conexión_Dia_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 6))

    @parameterized.expand(["24:60:60", "00:00:00", "18:05:45", "19:46:08"])
    def test_expValidation_Inicio_de_Conexión_Hora(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 7))

    @parameterized.expand(["25:64:64", "00:0000", "18:05:45a"])
    def test_expValidation_Inicio_de_Conexión_Hora_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 7))

    @parameterized.expand(["0", "2456154", "1"])
    def test_expValidation_Session_Time(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 8))

    @parameterized.expand(["01", "00", "154a"])
    def test_expValidation_Session_Time_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 8))

    @parameterized.expand(["DC-9F-DB-12-F3-EA:HCDD", "FF-FF-FF-FF-FF-FF:HCDD", "00-00-00-00-00-00:HCDD"])
    def test_expValidation_MAC_AP(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 9))

    @parameterized.expand(["DC-9F-DB-12-F3-EG:HCDD", "FF-FF-FF-FF-FF-FFF", "-00-00-00-00-0000:HCDD"])
    def test_expValidation_MAC_AP_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 9))

    @parameterized.expand(["DC-9F-DB-12-F3-EA", "FF-FF-FF-FF-FF-FF", "00-00-00-00-00-00"])
    def test_expValidation_MAC_Cliente(self, regExp):
        app = self.initApp()
        self.assertTrue(app.expValidation(regExp, 10))

    @parameterized.expand(["DC-9F-DB-12-F3-EG:HCDD", "FF-FF-FF-FF-FF-FFF", "-00-00-00-00-0000:HCDD"])
    def test_expValidation_MAC_Cliente_False(self, regExp):
        app = self.initApp()
        self.assertFalse(app.expValidation(regExp, 10))

    # 'generateFile' method tests:

    def test_generateFile_generateFile(self):
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files")
        try:
            os.remove(path.joinpath("test_data_filtered.csv"))
        except:
            pass        
        app = self.initApp()
        app.generateFile(path, None)
        self.assertTrue(path.joinpath("test_data_filtered.csv").exists())
        with open(path.joinpath("test_data.csv"), "r") as originalFile:
            with open(path.joinpath("test_data_filtered.csv")) as filteredFile:
                originalLines = originalFile.readlines()
                filteredLines = filteredFile.readlines()
        diff = set(originalLines).difference(set(filteredLines))
        self.assertEqual(diff, set())

    def test_generateFile_generateFile_removeLines(self):
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files")
        try:
            os.remove(path.joinpath("test_data_filtered.csv"))
        except:
            pass    
        app = self.initApp(path.joinpath("test_copyFile.csv"))
        app.generateFile(path, (3, 5))
        self.assertTrue(path.joinpath("test_copyFile_filtered.csv").exists())
        with open(path.joinpath("test_copyFile.csv"), "r") as originalFile:
            with open(path.joinpath("test_copyFile_filtered.csv"), "r") as filteredFile:
                originalLines = originalFile.readlines()
                filteredLines = filteredFile.readlines()
        diff = set(originalLines).difference(set(filteredLines))
        self.assertEqual(diff, {'Also, me', 'Eliminate, me\n'})

    def test_generateFile_generateFile_LinesIndexesOutOfRange(self):
        path = pathlib.Path.cwd().joinpath("main", "data", "test_files")
        try:
            os.remove(path.joinpath("test_copyFile_filtered.csv"))
        except:
            pass
        app = self.initApp(path.joinpath("test_copyFile.csv"))
        app.generateFile(path, (-5, 0, 3, 5, 6, 9))
        self.assertTrue(path.joinpath("test_copyFile_filtered.csv").exists())
        with open(path.joinpath("test_copyFile.csv"), "r") as originalFile:
            with open(path.joinpath("test_copyFile_filtered.csv"), "r") as filteredFile:
                originalLines = originalFile.readlines()
                filteredLines = filteredFile.readlines()
        diff = set(originalLines).difference(set(filteredLines))
        self.assertEqual(diff, {'Also, me', 'Eliminate, me\n'})

    # 'filterUsers' method tests:

    