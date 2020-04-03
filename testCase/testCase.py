'''
功能描述：
将表格中的数据进行接口的请求,并判断返回值是否正确
获取测试数据，完成接口测试的请求，断言结果
解析：

1。调用readexcel模块，获取测试数据

2。根据接口测试数据，进行请求
  2。1 get请求==get方法
  2。2 post请求==post方法
3。断言每个接口返回的结果
 3。1 成功
 3。2失败
4。写入我们的excel



'''
import unittest,json
from ddt import unpack,data
from ddt import  ddt
from common.configHttp import configHttp
from common.readExcel import readExcel
import requests



re = readExcel()
test_data =  re.read()


c  = configHttp()


@ddt
class  testCase(unittest.TestCase):
    def setUp(self):
        #执行case前面的初始化，
        pass
    #python编写测试用例必须集成unittese或者pytest


    #id, url, name, method, value, expect, real, status =  test_data
    #test_data[0]

    @data(*test_data)
    @unpack
    def testRun(self,id, url, name, method, value, expect, real, status):
        print('传入参数',id, url, name, method, value, expect, real, status)
        #处理数据格式
        value = value[0]
        
        #test_data1  = (test_data[0][1],test_data[0][3],test_data[0][4],test_data[0][6])
        #接口地址，接口请求方法，接口参数，预期结果
        if method == 'get' or method == 'GET':

            da =  c.get(url,  value)
            #接受数据
            try:
                self.assertEqual(str(da),str(expect))
                status  =  'success'
            except AssertionError as f:
                status  =  'fail'
                print(f)





            #pass


        elif method  == 'post'  or method == 'POST':
            post1 = c.post(url,value)
            try:
                self.assertEqual(str(post1),str(expect))
                #status = 'successs'
            except  AssertionError as e:
                print(type(e))
                #status = 'fail'






        elif method == 'put' or method == 'PUT':
            pass
        elif method == 'delete' or method  == 'DELETE':
            pass

            pass
        # elif method  == 'put':
        #     value = json.dumps(value)
        #     re1 = requests.post(url=url, data=value)
        #     real_sign1 = re1.json()['errorCode']
        #
        #     res = re1.status_code
        #     self.assertEqual(real_sign1, value)
        #     print(real_sign1)
        #     pass
        # assert(expect,real)




    def tearDown(self):
        #链接数据库，断开数据库等
        pass




    #return test_data






if __name__ == '__main__':
    #t = testCase()
    #t.testRun()
    #print(t.test_data)
    #print(t.test_data1)
    unittest.main()



#unittest







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
'''