from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def _rndChar():
	return chr(random.randint(65,90))

def _rndColor1():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def _rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 * 4
height = 60
img = Image.new('RGB', (width, height), (255,255,255))
font = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSansMono.ttf', 36)
draw = ImageDraw.Draw(img)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=_rndColor1())

for t in range(4):
	draw.text((60*t+10, 10), _rndChar(), font=font, fill=_rndColor2())

img = img.filter(ImageFilter.BLUR)

img.save('code.jpg', 'jpeg')
