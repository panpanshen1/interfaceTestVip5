'''
功能：
封装requests方法，接受用例传来的参数，进行请求。返回用例需要的数据

解析：
get
post
statuscode
real
'''
import requests,json
from common import readExcel


class configHttp(object):
    def __init__(self):
        print('开始请求接口')
    def run(self,url,  method, value):
        if  method == 'get' or method == 'GET':
            self.get(url,value)
            print(type(value))
        elif method  == 'post'  or method == 'POST':
            self.post(url, value)

    def get(self,url,value):
        print('get接口请求完成')
        result = requests.get(url=url,params= value)
        print(result)
        #re = result.json()['errorCode']
        # if re ==  expect:
        #     pass
        # else:
        #     pass
        return
    def post(self,url,value):
        #print(type(eval(value)),value,type(value))
        #v1 = json.loads(value)
        #a = eval(value)
        result = requests.post(url=url, data=eval(value))
        print(value)
        print(result)

        #print(type(result.text))\

        r1 = json.loads(result.text)
        errorCode = r1['errorCode']

        print(errorCode)
        print(result.text)
        print('post接口请求完成')
        return errorCode
    def put(self):
        print('put接口请求完成')

if __name__ ==  '__main__':
    c = configHttp()
    payload =str({'username':'liangchao','password':'123456','repassword':'123456'})
    c.post('https://www.wanandroid.com/user/register',payload)
#     #print(c.run('https://www.wanandroid.com/user/register','post',payload))
