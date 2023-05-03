import unittest
from ejercicio1 import *

class TestTP3(unittest.TestCase):
    def test_00(self):
        self.assertEqual(column("I"),0)
        self.assertEqual(column("%"),3)
        self.assertEqual(column("("),4)
        self.assertEqual(row("E"),0)
        self.assertEqual(row("t"),3)
        self.assertEqual(row("F"),4)
    
    def test_01(self):
        self.assertEqual(analizar("I$"),[])
        self.assertEqual(analizar("I+I$"),[])
        self.assertEqual(analizar("I-I$"),[])
        self.assertEqual(analizar("I%I$"),[])
        self.assertEqual(analizar("(I)$"),[])
    
    def test_02(self):
        self.assertEqual(analizar("$"),"Entrada Vacia")
        self.assertEqual(analizar(""),"Entrada Vacia")

    def test_03(self):
        self.assertEqual(analizar("I+(I-I)%I$"),[])



if __name__ == '__main__':
    unittest.main()