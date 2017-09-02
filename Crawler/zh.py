import os
import requests
from bs4 import BeautifulSoup
import json
import urllib
# 26380154 29814297 62692821
Question_id = '62692821'
Question_url = 'https://www.zhihu.com/api/v4/questions/'+Question_id+'/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=3&limit=20&sort_by=default'
AnswerCount = 1
header = {	
	'Connection': 'Keep-Alive',
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
cookie = {
   'aliyungf_tc':'AQAAAJZgTE/ehwsAF8RdfMpVGqySL04S',
   'cap_id':'NDVmMTA5NWU5ODBlNGVkM2I5MjdkYWFiMDZhYTU0MWE=|1502347783|584ba2bd674166f0f1bc444162ab7c4d994d2334',
   'd_c0':'ADBCy6bNMgyPTifFIfAmQWEEblOGLOlF7c0=|1502347783',
   'q_c1':'f203e690d72e49079fcc368660153629|1502335516000|1502335516000',
   'q_c1':'a9635deab0004763bbac36a74a459068|1502335516000|1502335516000',
   'r_cap_id':'MzJhYzg4M2YzOWZjNDUxYThhZDNhMDQ5NDUwMGZiMTA=|1502347783|89dab2b2df4371cadf225e0b36d0d340929aabc4',
   'z_c0':'Mi4wQURERFlWQ28xd2NBTUVMTHBzMHlEQmNBQUFCaEFsVk5JWS16V1FDWGlsa2JHRDJmZFBKQlRLRm1JQkkxRVpuNVBR|1502347809|37af63c2c66b6602816dd24fc5e0ebf24997716c'
 }
def Getdata(url):
	data = requests.get(url,headers=header,cookies=cookie).text
	data = json.loads(data)
	return data
def Getimg(x):
	soup = BeautifulSoup(x['content'],'html.parser')
	img = soup.findAll('img',class_='origin_image zh-lightbox-thumb')
	return img
def main():
	for page in range(1000):
		data = Getdata(Question_url)
		Content = data['data']
		for x in Content:
			img = Getimg(x)
			tmp = 1
			for imgsrc in img:
				imgurl = imgsrc['src']
				urllib.request.urlretrieve(imgurl,'E:\zhihu\cj62692821\%s.jpg' %(x['author']['name']+str(tmp)))
				tmp += 1
			print(AnswerCount)
			AnswerCount += 1
		if data['paging']['is_end']:
			break
		Question_url = data['paging']['next']
if __name__ == '__main__':
	main()