import requests
import re
import pandas as pd


class MathSeries:
	def __init__(self):
		#开启数据库操作
		self.session=requests.Session()
		self.url = 'http://www.math.shu.edu.cn/Default.aspx?tabid=37909'
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			}
		self.url_list = []

	def get_text(self):
		response = self.session.post(self.url, headers=self.headers)
		if response.status_code == 200:
			response.encoding = 'utf8'
			self.text = response.text


	#将数学系的所有讲座放入列表中
	def to_list(self):
		self.get_text()
		for i in re.findall(r'<a\sid=.*?title="(.*?)".href="(.*?)"', self.text):
			self.url_list.append(i[0].replace('我系','数学系'))
		print('第一步完成！，数学系综合新闻所有链接收集完成')




def math_news():
	a = MathSeries()
	a.to_list()
	w = dict.fromkeys(a.url_list, None)
	df = pd.Series(a.url_list)
	df.to_excel(excel_writer=r'./documents/数学系已经登记的新闻列表.xlsx',index = False)
	# print(a.url_list)
	return a.url_list

if __name__ == "__main__":
	math_news()