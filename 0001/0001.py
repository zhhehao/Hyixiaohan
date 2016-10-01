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

if __name__ == '__main__':
	print(_gen_code(200))
