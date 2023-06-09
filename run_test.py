import unittest, pathlib

if __name__ == "__main__":
    loader = unittest.TestLoader()
    loader.testMethodPrefix = "test"  
    suite = loader.discover(str(pathlib.Path.cwd().joinpath("main", "test")))
    unittest.TextTestRunner(failfast=True).run(suite)
