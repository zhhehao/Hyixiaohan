# -*- coding: utf-8 -*-
import xlwt, json

with open('numbers.txt') as f:
	content = f.read()
L = json.loads(content)

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('numbers')

row = 0
for li in L:
	sheet.write(row, 0, li[0])
	sheet.write(row, 1, li[1])
	sheet.write(row, 2, li[2])
	row = row + 1

wbk.save('numbers.xls')
