import requests
from bs4 import BeautifulSoup
import os
import pymysql
zhihu = pymysql.connect(host='xx.xx.xx.xx',port=3306,user='root',passwd='123456',db='zhihu',use_unicode = True,charset ='utf8')
cur = zhihu.cursor()
base_url ='https://www.zhihu.com/collection/26489045?page='

header = {	
	'Connection': 'Keep-Alive',
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
#依据自己cookie改一下
cookie = {

}
def insetSql(question,user,answer,con):
	cur.execute("INSERT INTO zhihu.duanzi (question,user,answer,likeCount)VALUES(%s,%s,%s,%s);",(question,user,answer,con))
	zhihu.commit()
def getSoup(url):
	html = requests.get(url,headers=header,cookies=cookie)
	soup = BeautifulSoup(html.text,'html.parser')
	return soup
def get():
	for page in range(1,300):
		print (page)
		url  = base_url + str(page)
		soup = getSoup(url)
		os.system("cls")
		print ("进度%.2f%%"%(page*100/300.0))
		try:
			title =soup.select('h2 a')
			author = soup.find_all('a',class_='author-link')
			context = soup.select('textarea.content')
			count = soup.select('span.count')
			for i in range(10):
				question = title[i].text
				user = author[i].text
				answer = context[i].text
				con = count[i].text
#				insetSql(question,user,answer,con)
				print(question,user,answer,con)
		except:
			continue
if __name__ == '__main__':
	get()
	cur.close()
	zhihu.close()