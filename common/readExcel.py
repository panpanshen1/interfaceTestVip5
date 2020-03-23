import xlrd ,xlwt
'''
功能描述：
在excel中取出测试数据，最终以列表的格式存储
解析：
1。找到目标文件，并打开
2。确认/定位sheet页
3。定位目标行
4。读取目标行的的数据格式，进行组装
'''
import xlrd ,xlwt,os

# 当前路径
current_dir = os.path.abspath(__file__)
# 路径的上个文件的路径
base_dir = os.path.dirname(os.path.dirname(current_dir))
excel_dir = base_dir + '/testData/data.xls'
class readExcel(object):
    #属性
    def __init__(self):
        self.readbook = xlrd.open_workbook(excel_dir)
        self.list1 = []


    #读取excel
    #sheet = readbook.sheet_by_index(0)

    #定位sheet页面
    def read(self):
        sheet = self.readbook.sheet_by_index(0)
        max1 = sheet.nrows
    #print(max1)
        for i in range(1,max1):
                row_value = sheet.row_values(i)
        #读取数据
                self.list1.append(row_value)
        return self.list1
            #row_value = sheet.row_values(i)

if __name__ == '__main__':
    re = readExcel()
    print(re.read())