import requests
import re
from lxml import etree
from concurrent import futures

class Photos:

	def __init__(self):
		#开启数据库操作
		self.session=requests.Session()
		self.url = 'http://www.scicol.shu.edu.cn'
		self.headers = {
			'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			}
		self.list = []

	def get_text(self):
		response = self.session.get(self.url, headers=self.headers, timeout=4)
		if response.status_code == 200:
			response.encoding = 'utf8'
			self.text = response.text


	def Links(self):
		"""
		获取每一个图片新闻的详细链接
		"""
		self.get_text()
		html = etree.HTML(self.text)
		length = len(html.xpath('//a[@class="Record"]'))
		print('-'*10, length, '-'*10)
		result = html.xpath('//a[@class="Record"]/@href')
		results = map(lambda x:self.url+str(x).replace('&nbsp;', ''), result)
		self.list, self.length = list(results), length


	def parse(self, tuple1):
		rank, link = tuple1
		response = self.session.get(link, headers=self.headers, timeout=4)
		text = response.text
		temp = {'标题':None, '创建日期':None, '图片内容':None}
		temp['标题'] = re.search(r'class="Head">([^&nbsp;].*?)<', text, re.S).group(1)
		temp['创建日期'] = re.search(r'\d+/\d+/\d', text, re.S).group(0)
		photo_url = self.url + re.search(r'<td align="center"><img.*?src="(.*?)"', text, re.S).group(1).replace('\n', '')
		# print(photo_url)
		photo_url = photo_url.replace('&amp;', '&')
		response = self.session.get(photo_url, headers=self.headers, timeout=4)
		temp['图片内容'] = response.content
		print(temp['标题'])
		self.writer(temp, rank)



	def writer(self, temp, rank):
		str1 = '%s-%s--%s' % (rank, temp['创建日期'].replace('/', '-'), temp['标题'])
		str1 = './documents/%s.jpg' % str1
		with open(str1, 'wb') as f:
			f.write(temp['图片内容'])


	def run(self):
		self.Links()
		with futures.ThreadPoolExecutor(6) as excutor:
			excutor.map(self.parse, zip(range(1, len(self.list)+1), self.list))
		print('图片内容创建完毕')





def prepare():
	import shutil,os
	try:
		shutil.rmtree('documents')
	except:
		pass
	os.mkdir('documents')

def main():
	prepare()
	w = Photos()
	w.run()

if __name__ == '__main__':
	main()