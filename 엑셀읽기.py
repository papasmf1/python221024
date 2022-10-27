# coding:utf-8
#설치를 먼저 진행
# pip install xlrd
# pip install xlwt
import xlrd

workbook = xlrd.open_workbook('c:\\work\\example.xls')
worksheet = workbook.sheet_by_index(0)
nrows = worksheet.nrows

row_val = []
for row_num in range(nrows):
    row_val.append(worksheet.row_values(row_num))
    
for item in row_val:
    print(item)
    
