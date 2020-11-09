# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:51:17 2018

@author: Administrator
"""
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://auth.geetest.com/register')
#browser.get('https://world.taobao.com/')
screenshot=browser.get_screenshot_as_png()
with open('www.jpg','wb+') as f:
    f.write(screenshot)
import time
time.sleep(3)
browser.close()
'''
input_first=browser.find_element_by_css_selector('#mq')
input_2=browser.find_element_by_xpath('//*[@id="mq"]')
input_4=browser.find_element_by_id('mq')
t=browser.find_element_by_name('q')
i=[]
i.append(input_first)
i.append(input_2)
i.append(input_4)
i.append(t)
print(i)
import time
time.sleep(5)
browser.close()
'''