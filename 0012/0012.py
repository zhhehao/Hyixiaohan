# -*- coding: utf-8 -*-

def _get_bad_words():
	_result = []

	with open('filtered_words.txt') as f:
		for line in f.readlines():
			_result.append(line.strip())

	return _result

if __name__ == '__main__':
	badwords = _get_bad_words()

	while True:
		userinput = input('Please enter some words(enter \'q\' to quit):')
		if userinput == 'q':
			break
		for bw in badwords:
			if bw in userinput:
				userinput = userinput.replace(bw, len(bw)*'*')
		print(userinput)
