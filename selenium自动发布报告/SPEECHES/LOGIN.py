import requests
import re
import time
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome,ChromeOptions

# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 10)
class Login:
	def __init__(self, browser, wait, username, password):
		self.url = 'http://www.math.shu.edu.cn/Default.aspx?tabid=35743&ctl=login'
		self.username, self.password = username, password
		self.wait = wait
		self.browser = browser

	def first_login(self):
		try:
			self.browser.get(self.url)
			self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr-1_Signin_txtUsername"]')))
			input_1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr-1_Signin_txtUsername"]')
			input_1.send_keys(self.username)
			input_2 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr-1_Signin_txtPassword"]')
			input_2.send_keys(self.password)
			bottom = self.browser.find_element_by_xpath('//*[@id="dnn_ctr-1_Signin_ImageButton1"]')
			bottom.click()
		except:
			raise

	def prepare(self):
		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67556_DD"]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[1]')))
		bottom1 = self.browser.find_element_by_xpath('//*[@id="tddnn_ctr67556_dnnSOLPARTACTIONS_ctldnnSOLPARTACTIONS0"]/td/img')
		bottom1.click()
		bottom2 = self.browser.find_element_by_xpath('//*[@id="tddnn_ctr67556_dnnSOLPARTACTIONS_ctldnnSOLPARTACTIONS1"]')
		bottom2.click()
		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67556_ArtEdit_txtKeywords"]')))

	def draft(self, test):
		item = dict(test)
		#标题
		text1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtTitle"]')
		text1.send_keys(item['标题'])
		#以下的两个click是模拟点击分类
		bottom1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_ctlCategories_lstAvailable"]/option[10]')
		bottom1.click()
		bottom1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_ctlCategories_cmdAdd"]')
		bottom1.click()
		# self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_pnlRichTextBox"]/table/tbody/tr[1]/td/div/textarea')))

		#点击html代码按钮，排除由纯文本编辑器与编辑器形成的异常
		#bottom22是html代码按钮， bottom2是纯文本编辑器按钮
		try:
			bottom22 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_optRender_1"]')
		except:
			bottom2 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_optView_0"]')
			bottom2.click()
			self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_optRender_1"]')))
			bottom22 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_optRender_1"]')
		finally:
			bottom22.click()
		#点击html代码按钮
		# bottom22 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_optRender_1"]')

		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_txtDesktopHTML"]')))
		#html文本框
		string = item['html代码']
		text2 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtEditor1_txtDesktopHTML"]')
		text2.send_keys(string)
		#发布时间
		text3 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtPublishDate"]')
		text3.clear()
		text3.send_keys(item['创建日期'])
		#以下为   活动时间
		# text4  = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtTime"]')
		# text4.clear()
		# #找到活动日期
		# str1 = re.search(r'(.*?)（', item['报告时间']).group(1)
		# text4.send_keys(str1)
		# #找到具体小时与分钟
		# hour, minute = re.findall(r'(\d+):(\d+)', item['报告时间'])[0]
		# # 构造小时的xpath
		# bottom3 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_ddlH"]')
		# bottom3.click()
		# str_1 = '//*[@id="dnn_ctr67556_ArtEdit_ddlH"]/option[%s]' % (int(hour)+1)
		# bottom3_1 = self.browser.find_element_by_xpath(str_1)
		# bottom3_1.click()
		# #构造分钟的xpath
		# bottom4 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_ddlM"]')
		# bottom4.click()
		# str_2 = '//*[@id="dnn_ctr67556_ArtEdit_ddlM"]/option[%s]' % (int(minute)+1)
		# bottom4_1 = self.browser.find_element_by_xpath(str_2)
		# bottom4_1.click()
		#以下为    活动地点
		text5 =  self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_txtPlace"]')
		text5.clear()
		text5.send_keys(item['报告地点'])
		#提交按钮
		submit = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67556_ArtEdit_cmdUpdate"]')
		submit.click()
		# q = input('是否提交【y/n】')
		# if q in ('Y', 'y', 'yes', 'Yes', 'YES'):
		# 	submit.click()
		# else:
		# 	self.browser.back()
		# 	self.browser.back()
		self.prepare()
		# submit.click()

	def close(self):
		time.sleep(10)
		self.browser.close()


if __name__ == "__main__":
	from settings import BROWSER, WAIT
	test = dict([('标题', 'Seminar第1888期 Completely Positive Binary Tensors'), ('创建日期', '2019/6/25'), ('报告主题', 'Completely Positive Binary Tensors'), ('报告人', '范金燕 教授 （ 上海交通大学）'), ('报告时间', '2019年7月1日（周一）16:00'), ('报告地点', '校本部GJ410'), ('邀请人', '周安娃'), ('主办部门', '理学院数学系'), ('报告摘要', 'A symmetric tensor is completely positive (CP) if it is a sum of tensor powers of nonnegative vectors. In this talk, we characterize completely positive binary tensors. We show that a binary tensor is completely positive if and only if it satisfies two linear matrix inequalities. This result can be used to determine whether a binary tensor is completely positive or not. When it is, we give an algorithm for computing its cp-rank and the decomposition. When the order is odd, we show that the cp-rank decomposition is unique. When the order is even, we completely characterize when the cp-rank decomposition is unique. '),('html代码','nihao1eadasdasdasdasdasdasdasdadasdas')])
	a = Login(BROWSER, WAIT,'10002833', 'tanfp321')
	a.first_login()
	a.prepare()
	#test为每一条记录
	a.draft(test)


