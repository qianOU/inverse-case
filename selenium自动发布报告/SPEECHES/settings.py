from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

BROWSER = webdriver.Chrome()
WAIT = WebDriverWait(BROWSER, 10)


USERNAME = '10002833'
PASSWORD = 'tanfp321'


KEY_WORDS = ['数学', '代数', '矩阵', 'math', '几何']

#处理表格等数据
STR_FORMAT_1 = """<a id="dnn_ctr64006_ArticleList__ctl0_ArtDataList__ctl9_titleLink1" class="linkfont1" title="{title}" href="{link}"
 target="_new">{title}</a>"""

PUNCTUATION = ' ，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'