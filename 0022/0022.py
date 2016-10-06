import logging
logging.basicConfig(level=logging.INFO)

import os
from PIL import Image

iphone_weight = 1920
iphone_height = 1080

for pic in os.listdir('.'):
	if pic[-1] == 'g':
		img = Image.open(os.path.join(os.path.abspath('.'), pic))
		if img.width > iphone_weight:
			img.resize((iphone_weight, img.width*iphone_height//iphone_weight))
			path = os.path.join(os.path.abspath('.'), 'resize_' + pic)
			img.save(path)
			logging.info('resize new pic: %s' % path)
		elif img.height > iphone_height:
			img.resize((img.height*iphone_weight//iphone_height, iphone_height))
			path = os.path.join(os.path.abspath('.'), 'resize_' + pic)
			img.save(path)
			logging.info('resize new pic: %s' % path)

