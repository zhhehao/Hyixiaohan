# -*- coding: utf-8 -*-
import xlwt, json

with open('student.txt') as f:
	content = f.read()
d = json.loads(content)

L = []
index = 0
for k, v in d.items():
	L.append(v)
	L[index].insert(0, int(k))
	index = index + 1

Ls = sorted(L, key=lambda x: x[0])

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('student')

row = 0
for r in Ls:
	col = 0
	for cell in r:
		sheet.write(row, col, cell)
		col = col + 1
	row = row + 1

wbk.save('student.xls')
