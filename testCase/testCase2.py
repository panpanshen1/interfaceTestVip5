import unittest
from ddt import ddt,data,unpack
@ddt
class MyTestCase2(unittest.TestCase):
    @data((2,4),(2,6))
    @unpack
    def test_tuple(self,value1,value2):
        print('---1',value1,value2)
        self.assertEqual(value1,value2)
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