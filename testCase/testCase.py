'''
功能描述：
将表格中的数据进行接口的请求,并判断返回值是否正确
获取测试数据，完成接口测试的请求，断言结果
解析：
# 1。找到刚刚存储的表格并打开
# 2。确认/定位list
# 3。将表格中的参数取出来
# 4。将参数带入请求，进行请求
# 5。判断返回值是否正确
1。调用readexcel模块，获取测试数据

2。根据接口测试数据，进行请求
  2。1 get请求==get方法
  2。2 post请求==post方法
3。断言每个接口返回的结果
 3。1 成功
 3。2失败
4。写入我们的excel



'''
from ddt import ddt,data,unpack
from common.readExcel import readExcel
import common,requests,unittest
#python编写的测试用例必须继承unittest.Testcase
@ddt
class  testCase(unittest.TestCase):
        # 1。调用readexcel模块，获取测试数据
    def setUp(self) -> None:
        pass
    re = readExcel()
    test_data = re.read()

    @data(*test_data)
    @unpack
    def testRun(self,id,url,name,method,param,expect,real,status):
        print(id,url,name,method,param,expect,real,status)
            # 2。根据接口测试数据，进行请求
        #根据请求方法调用不同的请求方式
        if method  == 'get':
            pass
            #   2。1 get请求==get方法
        elif method == 'post':
            result  = requests.get(url = url,params=param)
            status = result.status_code
            pass
            #   2。2 post请求==post方法
            # 3。断言每个接口返回的结果
        assert(except,real)
            #  3。1 成功
            #  3。2失败
            # 4。写入我们的excel
        writeExcel()
    def tearDown(self):
        #释放数据库
        pass
#testcase的特点，运行测试类，先走setup，走test开头的方法,当有多个方法，一个方法走完，会走setup，之后会跑teardown
if __name__ == '__main__':
    tc = testCase()
    print(tc.test_data())