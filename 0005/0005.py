import logging
logging.basicConfig(level=logging.INFO)

import os
from PIL import Image

for pic in os.listdir('.'):
	if pic[-1] == 'g':
		img = Image.open(os.path.join(os.path.abspath('.'), pic))
		if img.width > 1360:
			img.resize((1360, img.width*640//1360))
			path = os.path.join(os.path.abspath('.'), 'resize_' + pic)
			img.save(path)
			logging.info('resize new pic: %s' % path)
		elif img.height > 640:
			img.resize((img.height*1360//640, 640))
			path = os.path.join(os.path.abspath('.'), 'resize_' + pic)
			img.save(path)
			logging.info('resize new pic: %s' % path)

