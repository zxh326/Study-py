# 0010
''''
使用 Python 生成类似于下图中的字母验证码图片
'''
import string,random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
size = (480,60)
ranstr = string.ascii_letters + string.digits
res = ''
def getchar(num):
	global res 
	for i in range(num):
		res += random.choice(ranstr)
	print (res)
	return res
def getrgb():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def Gen_code(num):
	#first
	im = Image.new('RGBA',size,color = 0)
	draw = ImageDraw.Draw(im)
	## Draw background
	for w in range(size[0]):
		for h in range(size[1]):
			draw.point((w,h),getrgb())
	#Draw text
	testr = getchar(num)
	fnt = ImageFont.truetype('arial.ttf',int(size[1]*0.9))
	x = 0
	y = size[1]*0.1
	for i in range(num):
		x += size[0]*0.2
		draw.text((x,y),testr[i],font = fnt ,fill = getrgb())
	im = im.filter(ImageFilter.BLUR)
	im.show()
	im.save('captchar.jpg')
if __name__ == '__main__':
	Gen_code(4)
	testchar = input()
	print (testchar.lower()==(res.lower()))