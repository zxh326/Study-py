'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
2017.7.2
'''
import random
import string
ssrt = string.ascii_letters+string.digits
def get(count = 100,length = 18):
	fp = open('test.txt','w')
	for i in range(count):
		res = ""
		for x in range(length):
			res += random.choice(ssrt)
		print(res)
		fp.write(res+'\n')

if __name__ == '__main__':
	get(100,60)