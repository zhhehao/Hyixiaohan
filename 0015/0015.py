# -*- coding: utf-8 -*-
import xlwt, json

with open('city.txt') as f:
	content = f.read()
d = json.loads(content)

L = []
for k, v in d.items():
	L.append((int(k), v))

Ls = sorted(L, key=lambda x: x[0])

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('city')

row = 0
for r in Ls:
	sheet.write(row, 0, r[0])
	sheet.write(row, 1, r[1])
	row = row + 1

wbk.save('city.xls')
