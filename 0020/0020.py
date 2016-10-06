# -*- coding: utf-8 -*-
import re, xlrd

wbk = xlrd.open_workbook('201609.xls')

table = wbk.sheets()[0]

call_stat = {}
for row in range(table.nrows):
	v = table.row_values(row)
	if v[2][0] == '2':
		if '分' in v[3]:
			call_time_match = re.match(r'^(\d*)分(\d+)秒$', v[3])
			call_time = int(call_time_match.group(1)) * 60 + int(call_time_match.group(2))
		else:
			call_time_match = re.match(r'^(\d+)秒$', v[3])
			call_time = int(call_time_match.group(1))
		call_date = v[2][:10]
		if call_date in call_stat:
			call_stat[call_date] = call_stat[call_date] + call_time
		else:
			call_stat[call_date] = call_time

for k, v in call_stat.items():
	print('%s: %s' % (k, v))
