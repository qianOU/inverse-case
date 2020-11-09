# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:21:14 2019

@author: Administrator
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import time
from pyquery import PyQuery as pq
class XieCeng(object):
    """
    option -----选择旅游的类型
    """
    string = "window.open(%s)"
    #主题类型，可继续添加
    options_xpath = ['//*[@id="vac-103045-left-dest-2-主题旅游-1"]',
                     '//*[@id="vac-103045-left-dest-2-周边旅游-1"]',
                     '//*[@id="vac-103045-left-dest-2-境内旅游-1"]']
    def __init__(self,url,option):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,10)
        self.url = url #首页
        self.option = option
        
    #按不同种类进行解析
    def login_page(self):
        self.browser.get(self.url)                                                    
        Theme=self.wait.until(EC.element_to_be_clickable((By.XPATH,
                            XieCeng.options_xpath[self.option-1])))
        Theme.click()
        #获取某一个WebElement对象的属性 ------get_atttribute()
        url = 'https:' + Theme.get_attribute('href')
        print(url)
        #执行打开第二个窗口
        #self.browser.execute_script(string%url)
        #切换到第二个窗口，默认窗口第一个下标是0
        self.browser.switch_to.window(self.browser.window_handles[1])
        Theme=self.wait.until(EC.element_to_be_clickable((By.XPATH,
        '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a')))
        Theme.click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.index_page(2)
        
        
    def index_page(self,page):
        str = '//*[@id="searchResultContainer"]/div[17]/a[last()]'
        condition = self.browser.find_element_by_xpath(
            '//*[@id="searchResultContainer"]/div[17]/a[10]').text
        while True:
            bouttom=self.wait.until(EC.element_to_be_clickable((By.XPATH,
            str)))
            bouttom.click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="searchResultContainer"]/div[17]/a[10]')))
            self.parse(self.browser.page_source)
            page+=1
            time.sleep(8)
            if page == int(condition):
                return 
            print("*"*100)    
            
        
    def parse(self,sourse):
        sourse = pq(sourse)
        for item in sourse('div.product_aggregation.basefix').items():
            w = {}
            w['article'] = item('div.aggregation_content h2.aggregation_title a').text().strip()
            w['begin'] = item('div.product_recommend.basefix span.place').text()
            w['content'] = item('dl.recommend').text().strip()
            w['time'] = item('div.other_list').text()
            w['inputer'] = item('div.product_new_other').text().strip()
            w['money'] = item('div.box_r.contrast').text()
            print(w)
def main():
    browser = webdriver.Chrome()
    
if __name__ == '__main__':
    url = 'https://vacations.ctrip.com/'
    ins = XieCeng(url,1)
    ins.login_page()
    
