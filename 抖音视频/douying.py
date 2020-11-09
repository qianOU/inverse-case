# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:44:48 2019

@author: Administrator
"""
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
server='http://localhost:4723/wd/hub'
desired_caps={
        'platformName':'Android',
        'deviceName':'ERMDU17817004817',
        'appPackage':"com.ss.android.ugc.aweme",
        'appActivity':"com.ss.android.ugc.aweme.main.MainActivity"
        }
TIME_OUT=40
class douying():
    def __init__(self):
        self.driver=webdriver.Remote(server,desired_caps)
        self.wait=WebDriverWait(self.driver,TIME_OUT)
        self.action=TouchAction(self.driver)
    def login(self):
        #next=self.wait.until(ec.presence_of_all_elements_located((By.ID,'com.ss.android.ugc.aweme:id/qn')))
        #next.click()
        next1=self.wait.until(ec.presence_of_element_located((By.ID,'com.android.packageinstaller:id/permission_allow_button')))
        next1.click()
        next2=self.wait.until(ec.presence_of_element_located((By.ID,'com.android.packageinstaller:id/permission_allow_button')))
        next2.click()
        while True:
            self.action.press(x=311, y=900).move_to(x=300,y=200).release().perform()
            time.sleep(4)

if __name__=='__main__':
    a=douying()
    a.login()
           
        
