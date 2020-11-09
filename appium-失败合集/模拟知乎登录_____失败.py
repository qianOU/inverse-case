# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:45:46 2019

@author: Administrator
"""
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
#初始化driver
driver = webdriver.Chrome()
#打开知乎登录页面
driver.get('https://www.zhihu.com/signup')
#默认是注册界面，这里需要先找到切换登录的按钮
signup_switch_bt = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span')
#如果内容显示登录，则证明在注册页面，需要点击一下切换到登录页面
if signup_switch_bt.text == '登录':
    signup_switch_bt.click()
#找到填写用户名的输入框
uname_textfield = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
#找到填写密码的输入框
pwd_textfield = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')
#找到登录按钮
signup_bt = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button')
time.sleep(4)
#填写用户名，需要替换为你的用户名
uname_textfield.send_keys('13262523878')
#填写密码，需要替换为你的密码
pwd_textfield.send_keys('123456789hhj',Keys.ENTER)
#点击登录
time.sleep(7)

pwd_textfield.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
WW.until(EC.visibility_of_element_located(signup_bt))
pwd_textfield.send_keys(Keys.ENTER)
print(driver.page_source)