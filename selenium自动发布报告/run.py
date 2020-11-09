from NEWS.Main import news_main
from NEWS.LOGIN import Login_NEWS
from SPEECHES.LOGIN import Login
from SPEECHES.SpeechMain import speech_main
from settings import USERNAME, PASSWORD,BROWSER,WAIT,PUNCTUATION


def fun():
	"""
		预处理确保三个settings配置相同
	"""
	with open(r'settings.py', 'r', encoding='utf8') as text1,\
	open(r'./NEWS/settings.py', 'w', encoding='utf8') as text2,\
	open(r'./SPEECHES/settings.py', 'w', encoding='utf8') as text3:
		text3.write(text1.read())
		text2.write(text1.read())
	print('-'*100)
	print('预处理完成')
	print('-'*100)


def main():
	fun()
	browser = Login(BROWSER, WAIT, USERNAME, PASSWORD)
	speech_main(browser)
	browser = Login_NEWS(BROWSER, WAIT)
	news_main(browser)

main()