import requests
import json
from bs4 import BeautifulSoup
base_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'
songid = '186016'
url = base_url + songid + '?csrf_token='

Surl = 'http://music.163.com/song?id=186016'

head={
	'Cookie': 'appver=1.5.0.75771;',
	'Referer': 'http://music.163.com/'
}
data={
	'params':'B2NdyFLP4cdYtRs457XAF1+hMVlgh5pm++R6ZaFtfNm3bXrDi1j2RRMnWOSDPyRblmlUwLM5Ndvd7C0yg0yC4oLnfB5Skd1P6FBBe9KOf6Ejr8iWba/OcVQ9EL5s6VGC83uXGDhOeskDG1sXS9+aB1iiFC8dCvEOh/951dn0/uDqvPW+n/dRwHKSZHu0y+5c',
	'encSecKey':'c70dcda16b9bd1cedf4cfc0e6f0c502dade3a4a4ad9f6ebba04a5a31d000375273f9f49f5a82ff76f9156c0360e51f8660cf2dc19e5799225ba63a6954d52893d5b1c55d7c01b9c319ff93e3bc5e36d88d5bb3efbef49bf3f6293aefec480934b972819ad90505b8c5312fdba11255903aa7b17af049164b0fd8dc6d3085c099'
}
Sreq = requests.get(Surl,headers=head)
req = requests.post(url,headers=head,data=data)
soup = BeautifulSoup(Sreq.text,'html.parser')
title = soup.select('title')
print (title[0].text)
for i in req.json()['hotComments']:
	con = i['content']
	usern = i['user']['nickname']
	likec = i['likedCount']
	print ('@%s:'%usern,con,likec)