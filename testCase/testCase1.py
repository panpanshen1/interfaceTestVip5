import ddt,unittest
from common import readExcel
from ddt import data,unpack,ddt


@ddt
class testCase(unittest.TestCase):
    @data(1,2,3)
    def test_normal(self,value):
        print(value)
        self.assertEqual(value,9)
    @data(1)
    def test_normal2(self,value):
        print(value)
        self.assertEqual(value,2)
if __name__ == '__main__':
    unittest.main()
    # @data(*args)
    # @unpack
    # def test_normal(self,value):
    #     print(value)

