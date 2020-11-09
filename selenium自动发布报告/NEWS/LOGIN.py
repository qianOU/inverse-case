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

class Login_NEWS:
	def __init__(self, browser1, wait1, username=None, password=None):
		self.url = 'http://www.math.shu.edu.cn/Default.aspx?tabid=35743&ctl=login'
		self.username, self.password = username, password
		self.wait = wait1
		self.browser = browser1

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
			self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tddnn_ctr67554_dnnSOLPARTACTIONS_ctldnnSOLPARTACTIONS0"]/td/img')))
		except:
			raise

	def prepare(self):
		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tddnn_ctr67554_dnnSOLPARTACTIONS_ctldnnSOLPARTACTIONS0"]/td/img')))
		bottom1 = self.browser.find_element_by_xpath('//*[@id="tddnn_ctr67554_dnnSOLPARTACTIONS_ctldnnSOLPARTACTIONS0"]/td/img')
		bottom1.click()
		bottom2 = self.browser.find_element_by_xpath('//*[@id="tddnn_ctr67554_dnnSOLPARTACTIONS_ctldnnSOLPARTACTIONS1"]')
		bottom2.click()
		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67554_ArtEdit_cmdUpdate"]')))

	def draft(self, test):
		item = dict(test)
		text1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_txtTitle"]')
		text1.send_keys(item['标题'])
		bottom1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_ctlCategories_lstAvailable"]/option[9]')
		bottom1.click()
		bottom1 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_ctlCategories_cmdAdd"]')
		bottom1.click()
		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67554_ArtEdit_txtEditor1_optRender_1"]')))
		bottom22 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_txtEditor1_optRender_1"]')
		bottom22.click()
		self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dnn_ctr67554_ArtEdit_txtEditor1_txtDesktopHTML"]')))
		text2 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_txtEditor1_txtDesktopHTML"]')
		text2.send_keys(item['html代码'])
		text3 = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_txtPublishDate"]')
		text3.clear()
		text3.send_keys(item['创建日期'])
		submit = self.browser.find_element_by_xpath('//*[@id="dnn_ctr67554_ArtEdit_cmdUpdate"]')
		submit.click()
		# q = input('是否确定提交[Y/N]')
		# if q in ('Y', 'y', 'yes', 'Yes', 'YES'):
		# 	submit.click()
		# else:
		# 	self.browser.back()
		self.prepare()

	def close(self):
		time.sleep(10)
		browser.close()


if __name__ == "__main__":
	from settings import BROWSER,WAIT
	test = {'标题': '上海大学2018-2019年度百优团员、十佳团支书名单汇总表', '创建日期': '2019-05-09', 'URL': 'http://www.science.shu.edu.cn/pdf/20190509-1.doc', 'html代码': '<a id="dnn_ctr64006_ArticleList__ctl0_ArtDataList__ctl9_titleLink1" class="linkfont1" title="上海大学2018-2019年度百优团员、十佳团支书名单汇总表" href="http://www.science.shu.edu.cn/pdf/20190509-1.doc"\n target="_new">上海大学2018-2019年度百优团员、十佳团支书名单汇总表</a>'}
	a = Login_NEWS(BROWSER, WAIT, '10002833', 'tanfp321')
	a.first_login()
	a.prepare()
	#test为每一条记录
	a.draft(test)


