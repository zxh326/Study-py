import requests
from bs4 import BeautifulSoup
import re
base_url = 'https://movie.douban.com/top250?start='
page = [0,25,50,75,100,125,150,175,200,225]
#page = [0]
relink = '">\n<span class="title">(.*)</span>'
count = 0
for i in page:
	url = base_url + str(i)
	html = requests.get(url)
	soup = BeautifulSoup(html.text,'html.parser')	
	title = re.findall(relink,str(soup))
	movie_url = soup.select('div.hd')
	dp = soup.select('span.inq')
	for i in range(25):
		count=count+1
		print ("TOP%-4d%-15s%-30s %-10s"%(count,title[i],movie_url[i].a['href'],dp[i].text))