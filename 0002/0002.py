import logging
logging.basicConfig(level=logging.INFO)

import mysql.connector
import random

def _gen_code(number):
	_code_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	_result = []

	for n in range(number):
		_code = ''
		for m in range(8):
			_code = _code + _code_list[random.randint(0, 35)]
		_result.append(_code)

	return _result

# suppose a empty database named "test" is exist.
# connect mysql
conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()

# create table codes
cursor.execute('create table codes (id varchar(10) primary key, code varchar(10))')

# insert code from 0001.py
codes = _gen_code(200)
i = 1
for c in codes:
	cursor.execute('insert into codes (id, code) values (%s, %s)', [str(i), c])
	cursor.rowcount
	conn.commit()
	i = i + 1
logging.info('%d rows has been insert into table codes.' % (int(i)-1))

# disconnect mysql
cursor.close()
conn.close()
