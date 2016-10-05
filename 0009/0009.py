import logging; logging.basicConfig(level=logging.INFO)

from html.parser import HTMLParser

class _HTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for link in attrs:
				if link[0] == 'href':
					logging.info('Found a link: %s' % link[1])

parser = _HTMLParser()

with open('index.html') as f:
	parser.feed(f.read())
