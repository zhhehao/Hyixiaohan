import logging; logging.basicConfig(level=logging.INFO)
import os

def _stat_code(foldername):
	_total_row, _total_comment, _total_space = 0, 0, 0
	for file in os.listdir(foldername):
		_fname = os.path.join(os.path.abspath(foldername), file)
		with open(_fname, 'r') as f:
			for line in f.readlines():
				_total_row = _total_row + 1
				if line[0] == '#':
					_total_comment = _total_comment + 1
				elif len(line.strip()) == 0:
					_total_space = _total_space + 1

	return _total_row, _total_comment, _total_space

if __name__ == '__main__':
	r, c, s = _stat_code('codefolderpath')
	logging.info('You complete %d rows code, include %d rows comments and %d rows space.' % (r, c, s))
