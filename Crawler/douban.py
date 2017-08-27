import requests
from bs4 import BeautifulSoup
import re
import os
movie_id = 26363254
page = '0'
head = {
   'Connection':'Keep-Alive',
   'Host':'movie.douban.com',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
#依据自己cookie改一下
cookie ={
	'_pk_id.100001.4cf6': '11f49aa79faa6de3.1503542460.1.1503542460.1503542460.',
	'_pk_ses.100001.4cf6': '*',
	'bid':'riefSZhz0Qk',
   	'ap':'1',
   	'bid': 'riefSZhz0Qk',
   	'ck': 'mm67',
   	'dbcl2': '81629001:tBUh2FhUpB4',
   	'ps': 'y',
   	'push_doumail_num':'0',
   	'push_noty_num': '0'
}
fp = open('zl.txt','w+',encoding='utf-8')
def geSoup(url):
	html = requests.get(url,headers=head,cookies=cookie)
	soup = BeautifulSoup(html.text,'html.parser')
	return soup
for sd in range(100):
	url = 'https://movie.douban.com/subject/'+str(movie_id)+'/comments?start=' + page +'&limit=20&sort=new_score&status=P'
	soup = geSoup(url)
	cont = soup.select('p.')
	next_page = soup.select('div.center a.next')
	temp = re.findall(".*start=(.*)&amp;l.*",str(next_page))
	page = temp[0]
	os.system("cls")
	for i in range(20):
#		print(cont[i].text)
		fp.write(cont[i].text)
	print("进度%.4f%%"%(sd*100/100.0))
fp.close()