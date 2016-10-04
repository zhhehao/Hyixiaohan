import logging
logging.basicConfig(level=logging.INFO)
import re, os

def _get_important(filename):
	d = {}
	with open(filename, 'r') as f:
		for line in f.readlines():
			for word in line.split():
				if re.match(r'^[a-zA-Z]+[.:?]?$',word):
					if word.lower() in d:
						d[word.lower()] = d[word.lower()] + 1
					else:
						d[word.lower()] = 1

	_important_word = []
	_max_word_count = 0

	for k, v in d.items():
		if v == _max_word_count:
			_important_word.append(k)
		elif v > _max_word_count:
			_important_word = []
			_important_word.append(k)
			_max_word_count = v

	return _important_word

if __name__ == '__main__':
	for file in os.listdir('.'):
		if file[-1] == 't':
			filename = os.path.join(os.path.abspath('.'), file)
			_iword = _get_important(filename)
			logging.info('The important word for %s is %s' % (filename, _iword))

