import unittest, pathlib

if __name__ == "__main__":
    suite = unittest.TestLoader().discover(pathlib.Path.cwd().joinpath("main", "test"))
    unittest.TextTestRunner(failfast=True).run(suite)
