from PIL import Image, ImageDraw, ImageFont

def _draw_number(picture, number):
	img = Image.open(picture)
	imgd = ImageDraw.Draw(img)
	ifont = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSansMono.ttf',size=50)

	imgd.text((130,5), str(number), fill=(255,0,0), font=ifont)
	img.save('0000_draw.jpg')

if __name__ == '__main__':
	_draw_number('0000.jpg', 4)

