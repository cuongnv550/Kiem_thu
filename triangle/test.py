import unittest
from math import sqrt
from triangle import detect_triangle
class TestTriangle(unittest.TestCase):
    def test_1(self):
        self.assertEqual(detect_triangle(-1,1,3),-1)
    def test_2(self):
        self.assertEqual(detect_triangle(1,-1,3),-1)
    def test_3(self):
        self.assertEqual(detect_triangle(1,1,-3),-1)
    def test_4(self):
        self.assertEqual(detect_triangle(-1,-1,-3),-1)
    def test_5(self):
        self.assertEqual(detect_triangle(1,2,2**32),-1)
    def test_6(self):
        self.assertEqual(detect_triangle(1,2**32,2),-1)
    def test_7(self):
        self.assertEqual(detect_triangle(2**32,1,2),-1)
    def test_8(self):    
        self.assertEqual(detect_triangle(1,1,3),0)
    def test_9(self): 
        self.assertEqual(detect_triangle(1,3,1),0)
    def test_10(self): 
        self.assertEqual(detect_triangle(3,1,1),0)
    def test_11(self): 
        self.assertEqual(detect_triangle(1,1,1),1)
    def test_12(self): 
        self.assertEqual(detect_triangle(1,1,float(sqrt(2))),2)
    def test_13(self): 
        self.assertEqual(detect_triangle(2,2,3),3)
    def test_14(self): 
        self.assertEqual(detect_triangle(3,4,5),4)
    def test_15(self): 
        self.assertEqual(detect_triangle(2,3,4),5)
    def test_16(self): 
        self.assertEqual(detect_triangle(1,2,'ab'),-1)
    def test_17(self): 
        self.assertEqual(detect_triangle(1,'ab',3),-1)
    def test_18(self): 
        self.assertEqual(detect_triangle('ab',3,4),-1)
    def main():
        unittest.main()
if __name__ == '__main__':
    unittest.main()     
