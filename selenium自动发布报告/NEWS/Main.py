import requests
import re
import time


from NEWS.MathAcd import math_news
from NEWS.SciReports import sci_report_main
from NEWS.SciResearch import sci_research_main
from NEWS.SciGraduate import sci_graduate_main
from NEWS.SciUnder import sci_undergraduate_main
from NEWS.SciNews import sci_news_main
from NEWS.LOGIN import Login_NEWS
from settings import PUNCTUATION

def title(text):
	for i in PUNCTUATION:
		text = text.replace(i, '')
	return text

def get_one(haved, param):
	storage = []
	list_1, detail = param
	list_2 = [title(i) for i in list_1]
	list_3 = dict(zip(list_2, list_1))
	temp = set(list_2) - haved
	for i in temp:
		for item in detail:
			if item['标题'] == list_3[i]:
				storage.append(item)
				break
	return storage



def get_wanted_news():
	"""
		得到需要更新的数学相关的新闻
	"""
	#数学系已经登过的新闻
	temp = [title(i) for i in math_news()]
	haved = set(temp)
	#理学院的通知报告
	reports =get_one(haved, sci_report_main())
	researches = get_one(haved, sci_research_main())
	under =get_one(haved, sci_undergraduate_main())
	graduate = get_one(haved, sci_graduate_main())
	news = get_one(haved, sci_news_main())
	wanted_list = reports + researches + under +\
	graduate + news
	# print(wanted_list)
	return wanted_list


def news_main(Browser):
	"""
		无需登录,进行添加
		Broswer 为Login_News对象
	"""
	temp = get_wanted_news()

	# #按编号排序
	# temp = sorted(temp, key= lambda x:int(re.search(r'第(\d+)期', x).group(1)))

	Browser.prepare()
	#test为每一条记录
	for test in temp:
		Browser.draft(test)
	print('-'*100+'\n')
	print('已经更新完所有的新闻速递！')
	print('-'*100+'\n')
	Browser.browser.close()


if __name__ == "__main__":
	#test = {'标题': '上海大学2018-2019年度百优团员、十佳团支书名单汇总表', '创建日期': '2019-05-09', 'URL': 'http://www.science.shu.edu.cn/pdf/20190509-1.doc', 'html代码': '<a id="dnn_ctr64006_ArticleList__ctl0_ArtDataList__ctl9_titleLink1" class="linkfont1" title="上海大学2018-2019年度百优团员、十佳团支书名单汇总表" href="http://www.science.shu.edu.cn/pdf/20190509-1.doc"\n target="_new">上海大学2018-2019年度百优团员、十佳团支书名单汇总表</a>'}
	from NEWS.settings import *
	temp = get_wanted_news()
	a = Login_NEWS(BROWSER, WAIT, '10002833', 'tanfp321')
	a.first_login()
	a.prepare()
	#test为每一条记录
	for test in temp:
		a.draft(test)