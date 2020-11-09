import requests
import re
import pandas as pd
from collections import OrderedDict
from concurrent import futures
import queue
from settings import STR_FORMAT_1, KEY_WORDS

class Text:
	def __init__(self, param='34748'):
		#开启数据库操作
		self.session=requests.Session()
		self.url = 'http://www.scicol.shu.edu.cn/Default.aspx?tabid=34451'
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			}

	def get_text(self):
		response = self.session.post(self.url, headers=self.headers)
		if response.status_code == 200:
			response.encoding = 'utf8'
			return response.text

class Notes:

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
		for i in re.findall(r'<a\sid=.*?title="(.*?)"\shref="(.*?)".*?class="linkfont1">(.*?)<', self.text, re.S):
			#防止有遗漏
			temp = self.base_url + i[1].replace('amp;','')
			#删选出有关数学的内容
			# if '数学' in i[0] or 'math' in i[0].lower() or '矩阵' in i[0].lower() or '代数' in i[0].lower():
			if any([t in i[0].lower() for t in KEY_WORDS]):
				# temp = (self.base_url + i[1].replace('amp;','')) if i[1].startswith('/') else i[1].replace('amp;','')
				# print(temp)
				self.url_list.append((i[0], temp, i[2]))
				self.list_name.append(i[0])
		print('第一步完成！，数学系本科生所有链接收集完成')

	def parse(self, param):
		temp, url, date =param
		if url.endswith(('.pdf', '.doc', '.xls', '.xlsx')):
			text = STR_FORMAT_1.format(title=temp, link=url)
		else:
			response = self.session.get(url, headers=self.headers)
			re_rule = re.compile(r'<table id="[\w_\d]*?Table3"(.*?)</table>', re.S)
			text = re.search(re_rule, response.text)
			text = text.group(0)
			text = text.replace('src="', 'src="'+self.base_url).replace('\t', '').replace('\r', '').replace('\n', '')
			# print('--------'*50)
		dict1 ={'标题':temp, '创建日期':date, 'URL':url, 'html代码':text}
		# print(dict1)
		self.queue.put(dict1)



def sci_undergraduate_main():
	a = Text()
	text = a.get_text()
	w = Notes(text)
	w.to_list()
	with futures.ThreadPoolExecutor(8) as executor:
		res = executor.map(w.parse, w.url_list)
	while not w.queue.empty():
		w.sets_dict.append(w.queue.get())
	df = pd.DataFrame(w.sets_dict)
	df.to_excel(excel_writer=r'./documents/本科生教育/理学院获取的有关数学本科生教育详细信息.xlsx',index = False)
	df = pd.Series(w.list_name)
	df.to_excel(excel_writer=r'./documents/本科生教育/理学院的有关数学本科生教育列表.xlsx',index = False)
	return w.list_name, w.sets_dict

if __name__ == "__main__":
	sci_undergraduate_main()