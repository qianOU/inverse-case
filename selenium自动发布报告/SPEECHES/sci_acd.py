import requests
import re
import pandas as pd
from collections import OrderedDict
from concurrent import futures
import queue
from settings import PUNCTUATION

class Text:
	def __init__(self, param='34748'):
		#开启数据库操作
		self.session=requests.Session()
		self.url = 'http://www.scicol.shu.edu.cn/Default.aspx?tabid=34748'
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			}

	def get_text(self):
		response = self.session.post(self.url, headers=self.headers)
		if response.status_code == 200:
			response.encoding = 'utf8'
			return response.text

class Speaches:

	def __init__(self, text):
		self.text = text
		self.base_url = 'http://www.scicol.shu.edu.cn'
		self.url_list = []
		self.repr = '数学系'
		self.session=requests.Session()
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			}
		self.queue = queue.Queue(20)
		self.sets_dict = []
		self.list_name = []

	#将数学系的所有讲座放入列表中
	def to_list(self):
		for i in re.findall(r'<a\sid=.*?title="数学系(.*?)"\shref="(.*?)"', self.text):
			temp = self.base_url + i[1].replace('amp;','')
			self.url_list.append((i[0], temp))
			self.list_name.append(i[0])
		print('第一步完成！，数学系讲座所有链接收集完成')

	#算法用于去重
	# def title(self, text):
	# 	for i in PUNCTUATION:
	# 		text = text.replace(i, '')
	# 	return text


	def parse(self, param):
		temp, url =param
		# print(url)
		response = self.session.get(url, headers=self.headers)
		text = response.text
		text = text.replace('&nbsp;','').replace('amp;', '')
		# print(temp)
		rep = '创建日期.*?class="normal">(.*?)<.*?报告主题：(.*?)<.*?报告人：(.*?)<.*?报告时间：(.*?)<.*?'\
			+ '报告地点：(.*?)<.*?邀请人：(.*?)<.*?主办部门：(.*?)<.*?报告摘要：(.*?)<'
		rep = re.compile(rep, re.S)
		s = re.search(rep, text)
		list_1 = ['标题','创建日期','报告主题', '报告人', '报告时间', 
			'报告地点', '邀请人','主办部门',  '报告摘要', 'html代码']
		#获取HTML代码
		re_rule = re.compile(r'<table id="[\w_\d]*?Table3"(.*?)</table>', re.S)
		text2 = re.search(re_rule, text)
		text2 = text2.group(0)
		text2 = text2.replace('src="', 'src="'+self.base_url).replace('\t', '').replace('\r', '').replace('\n', '').replace('主办部门：理学院数学系', '')
		# print(text2)
		if s is None:
			raise AttributeError('%s没有匹配到!' %url)
		temp_list = [s.group(i) if i else temp for i in range(9)]+[text2]
		self.queue.put(OrderedDict(zip(list_1, temp_list)))



# if __name__ == "__main__":
def sci_speech_main():
	a = Text()
	text = a.get_text()
	w = Speaches(text)
	w.to_list()
	with futures.ThreadPoolExecutor(8) as executor:
		res = executor.map(w.parse, w.url_list)
	while not w.queue.empty():
		w.sets_dict.append(w.queue.get())
	df = pd.DataFrame(w.sets_dict)
	# print(w.sets_dict[1])
	df.to_excel(excel_writer=r'./documents/学术报告/理学院获取的详细学术报告信息.xlsx',index = False)
	df = pd.Series(w.list_name)
	df.to_excel(excel_writer=r'./documents/学术报告/理学院的讲座列表.xlsx',index = False)
	return w.list_name, w.sets_dict


if __name__ == '__main__':
	sci_speech_main()