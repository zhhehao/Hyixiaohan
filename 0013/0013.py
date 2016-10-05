from urllib import request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self._result = []

	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			for attr in attrs:
				if attr[0] == 'src' and attr[1][:23] == 'http://imgsrc.baidu.com':
					self._result.append(attr[1])
					break

	def get_url(self):
		return self._result

req = request.Request('http://tieba.baidu.com/p/2166231880')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0')

parser = MyHTMLParser()

with request.urlopen(req) as f:
	parser.feed(f.read().decode('utf-8'))

imgurls = parser.get_url()

imgname = 1
for imgurl in imgurls:
	request.urlretrieve(imgurl, '%s.jpg' % imgname)
	imgname = imgname + 1
