import re

from SPEECHES.math_acd import math_speech_main
from SPEECHES.sci_acd import sci_speech_main
from SPEECHES.LOGIN import Login
from settings import PUNCTUATION



# def main():
# 	#获得数学系已发布的报告列表
# 	a1 = MathSeries()
# 	a1.to_list()
# 	math_list = a1.url_list
# 	df = pd.Series(a1.url_list)
# 	df.to_excel(excel_writer=r'./documents/数学系已经登记的讲座列表.xlsx',index = False)
# 	print(a1.url_list)
# 	#获得理学院发布的报告列表
# 	a = Text()
# 	text = a.get_text()
# 	w = Speaches(text)
# 	w.to_list()
# 	sci_list = w.list_name
# 	#运用多线程加快速度
# 	with futures.ThreadPoolExecutor(8) as executor:
# 		res = executor.map(w.parse, w.url_list)
# 	while not w.queue.empty():
# 		w.sets_dict.append(w.queue.get())
# 	df = pd.DataFrame(w.sets_dict)
# 	df.to_excel(excel_writer=r'./documents/理学院获取的讲座信息.xlsx',index = False)
# 	df = pd.Series(w.list_name)
# 	df.to_excel(excel_writer=r'./documents/理学院的讲座列表.xlsx',index = False)
# 	#暂时还没有发布的报告
# 	temp_set = set(sci_list) - set(math_list)
# 	for item in temp_set:
# 		for dict1 in w.sets_dict:
# 			if dict1['标题'] == item:
# 				print(dict1)
# 				Browser.draft(dict1)
# 				break
# 	Browser.close()
# main()


#新的去重算法，去掉了标点符号的影响
def title(text):
	for i in PUNCTUATION:
		text = text.replace(i, '')
	return text

def speech_main(Browser):
	"""Broser 为Login对象"""
	Browser.first_login()
	Browser.prepare()
	haved_1 = math_speech_main()
	list_1, detail = sci_speech_main()
	print('进行去重...')
	list_2 = [title(i) for i in list_1]
	list_3 = dict(zip(list_2, list_1))
	haved_2 = [title(i) for i in haved_1]
	temp_set = set(list_2) - set(haved_2)
	print('去重完成， 进行排序...')
	#按编号排序
	temp_set = sorted(temp_set, key= lambda x:int(re.search(r'第(\d+)期', x).group(1)))
	print('排序完成， 开始更新...')
	for item in temp_set:
		for dict1 in detail:
			if dict1['标题'] == list_3[item]:
				# print(dict1)
				Browser.draft(dict1)
				break
	print('-'*100+'\n')
	print('已经更新完所有的学术报告！')
	print('-'*100+'\n')
	# q = input('请确认是否继续更新新闻:[Y/N]')
	# if q.lower() != 'y':
	# 	Browser.close()
	# else:
	Browser.browser.back()


if __name__ == "__main__":
	from SPEECHES.settings import USERNAME, PASSWORD,BROWSER,WAIT


	Browser = Login(USERNAME, PASSWORD,BROWSER,WAIT)
	Browser.first_login()
	Browser.prepare()
	speech_main(Browser)