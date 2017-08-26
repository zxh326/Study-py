'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
2017.7.1
'''
from PIL import Image,ImageDraw,ImageFont
def addType(image,Type = '1211'):
	draw = ImageDraw.Draw(image)
	myfont = ImageFont.truetype('C:\Windows\Fonts\XHei_iOS7.TTC',size = 60)
	fillcolor = "#ff0000"
	wid , hig= image.size
	draw.text((0,0),Type,fill=fillcolor,font=myfont)
	image.save('result.jpg','jpeg')
if __name__ == '__main__':
	image = Image.open('captchar.jpg')
	'''font = input("Scanf you wang to add som")'''
	addType(image)