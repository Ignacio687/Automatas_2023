import unittest, pathlib

if __name__ == "__main__":
    loader = unittest.TestLoader()
    ## por si quieren correr tests especificos, ponen el nombre del test o prefijo comun de varios test, sino lo comentan o lo dejan en test
    loader.testMethodPrefix = "test"  
    suite = loader.discover(str(pathlib.Path.cwd().joinpath("main", "test")))
    unittest.TextTestRunner(failfast=True).run(suite)
