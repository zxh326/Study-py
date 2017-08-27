# coding:utf-8
import json
import requests
import math
import time
import hashlib
from bs4 import BeautifulSoup
base_url = 'https://www.toutiao.com/api/article/feed/?category=essay_joke&utm_source=toutiao&widen=1'
next_time = '0'
'''
Get as cp
参考原版JavaScript代码写的算法
'''
def getASCP():
    t = int(math.floor(time.time()))
    e = hex(t).upper()[2:]
    m = hashlib.md5()
    m.update(str(t).encode(encoding='utf-8'))
    i = m.hexdigest().upper()
    if len(e) != 8:
        AS = '479BB4B7254C150'
        CP = '7E0AC8874BB0985'
        return AS,CP
    n = i[0:5]
    a = i[-5:]
    s = ''
    r = ''
    for o in range(5):
        s += n[o] + e[o]
        r += e[o + 3] + a[o]

    AS = 'A1' + s + e[-3:]
    CP = e[0:3] + r + 'E1'
    return AS,CP
#fp = open("joke.txt",'a+')
for x in range(500):
	a,c=getASCP()
	session = requests.Session()
	url = base_url + '&max_behot_time=' + str(next_time) +'&max_behot_time_tmp=' + str(next_time) + '&tadrequire=true' + '&as='+ a +'&cp='+ c
#	print (url)
	data = session.get(url,cookies={'tt_webid':'6454870613295613454'}).text
	cdata = json.loads(data)
	duanzi = cdata['data']
#	next_time = cdata['next']['max_behot_time']
	for i in duanzi:
		user = i['group']['user']['name']
		con = i['group']['content']
		dian = i['group']['digg_count']
		cai = i['group']['bury_count']
		resu = '网友@'+user+':'+con
		print (resu)
#		fp.write(resu)