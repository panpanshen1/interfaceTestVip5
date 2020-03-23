import xlrd ,xlwt
readbook = xlrd.open_workbook(r'data.xls')
#读取excel
#sheet = readbook.sheet_by_index(0)
#定位sheet页面
sheet = readbook.sheet_by_name('urlSheet')
max1 = sheet.nrows
#print(max1)

for i in range(1,max1):
    row_value = sheet.row_values(i)
    #读取数据
    print(row_value)
        #row_value = sheet.row_values(i)




