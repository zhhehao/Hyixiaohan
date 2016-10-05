import logging; logging.basicConfig(level=logging.INFO)

from html.parser import HTMLParser

class _HTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self._result = []

	def handle_data(self, data):
		content = data.strip()
		if len(content) != 0:
			self._result.append(content)

	def get_result(self):
		return self._result

parser = _HTMLParser()

with open('index.html') as f:
	parser.feed(f.read())

for text in parser.get_result():
	print(text)
