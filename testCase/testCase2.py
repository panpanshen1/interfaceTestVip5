import unittest
from ddt import ddt,data,unpack
@ddt
class MyTestCase2(unittest.TestCase):
    @data([2,3,4,5,6],[4,2,3,4,5])
    @unpack
    def test1(self,value1,value2,value3,value4,value5):
        print(value1,value2,value3,value4,value5)
        self.assertEqual(value1,value2)
    @data((2,4),(2,6))
    @unpack
    def test_tuple(self,value8,value9):
        print('---1',value8,value9)
        self.assertEqual(value8,value9)
    @data([1,2],[3,4])
    @unpack
    def test_list(self,value1,value2):
        print('---2',value1,value2)
        self.assertEqual(value1,value2)
    @data({'value1':1,'value2':2},{'value1':4,'value2':5})
    @unpack
    def test_dict(self,value1,value2):
        print('---3',value1,value2)
        self.assertEqual(value1,value2)
if __name__ == '__main__':
    unittest.TestCase2