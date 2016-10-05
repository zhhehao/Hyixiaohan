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
		print('Please enter a word(enter \'q\' quit script.):')
		word = input().strip()
		if word == 'q':
			break
		if word in badwords:
			print('Freedom')
		else:
			print('Human Rights')
