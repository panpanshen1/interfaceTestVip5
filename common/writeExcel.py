from xlutils.copy  import copy
import xlrd,os

# path1  = os.path.abspath(__file__)
# path2 = os.path.dirname(os.path.dirname(path1))+'/testData/data.xls'
# print(path2)
# rd  = xlrd.open_workbook(path2)
# print(rd)
# wb = copy(rd)

class writeExcel(object):
    def __init__(self):
        print('将实际结果和执行状态写入excel')
