'''
任一个英文的纯文本文件，统计其中的单词出现的个数
'''
import re
def count(path):
    with open(path) as f:
        text = f.read()
        words_list = re.findall(r'[a-zA-Z0-9]+', text)
        count = len(words_list)
    return count
if __name__ == '__main__':
	print (count('test.txt'))