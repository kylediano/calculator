import unittest
from calculator import Calculator as calc
import array as arr

class UnitTests(unittest.TestCase):
    
    def test_add(self):
        self.assertEquals(4,calc.add(self,2,2))
    
    def test_subtract(self):
        self.assertEquals(0,calc.subtract(self,2,2))

    def test_multiply(self):
        self.assertEquals(4,calc.multiply(self,2,2))

    def test_divide(self):
        self.assertEquals(3,calc.divide(self,9,3))

if __name__ == '__main__':
    unittest.main()