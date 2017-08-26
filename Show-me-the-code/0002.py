'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
import pymysql
yourdb = pymysql.connect(host='xxx.xxx.xx.xx',port=3306,user='root',passwd='123456',db='yourdb')
cur = yourdb.cursor()
fp = open('test.txt','rb')
for line in fp.readlines():
	code = line.strip()
	cur.execute("insert into yourdb.code (code) values(%s);", [code])
yourdb.commit()
cur.close()
yourdb.close()
fp.close()
