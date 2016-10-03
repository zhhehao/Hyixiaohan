import random
import redis

def _gen_code(number):
	_code_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	_result = []

	for n in range(number):
		_code = ''
		for m in range(8):
			_code = _code + _code_list[random.randint(0, 35)]
		_result.append(_code)

	return _result

pool = redis.ConnectionPool(host='127.0.0.1', port='6379', db=0)
r = redis.Redis(connection_pool=pool)

codes = _gen_code(200)

# key-value string
# i = 1
# for c in codes:
# 	r.set(str(i), c)
# 	i = i + 1

# for i in range(201):
# 	print(r.get(str(i)))


# put strings in a list
# for c in codes:
# 	r.lpush('code', c)

# print(r.lrange('code', 1, 200))


