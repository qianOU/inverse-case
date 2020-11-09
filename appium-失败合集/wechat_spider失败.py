# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:40:07 2019

@author: Administrator
"""
import time
from pymongo import MongoClient
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
PLATFORM='Android'
DEVICE_NAME='ERMDU17817004817'
APP_PACKAGE='com.tencent.mm'
APP_ACTIVITY='.ui.LauncherUI'
DRIVE_SERVER='http://localhost:4723/wd/hub'
TIME_OUT=300
MONGO_URL='localhost'
MONGO_DB='moments'
MONGO_COLLECTION='moments'

class Moments():
    """
    初始化
    """
    #启动配置
    def __init__(self):
        self.desired_caps={
                'platformName':'Android',
                'deviceName':DEVICE_NAME,
                'appPackage':APP_PACKAGE,
                'appActivity':APP_ACTIVITY
                }
        self.driver=webdriver.Remote(DRIVE_SERVER,self.desired_caps)
        self.wait=WebDriverWait(self.driver,TIME_OUT)
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[MONGO_COLLECTION]
        self.action=TouchAction(self.driver)
    
    def login(self):
        next2=self.wait.until(ec.element_to_be_clickable(By.ID,'android:id/button1'))
        next2.click()
        login=self.wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/e0y')))
        login.click()
        phone=self.wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/ka')))
        phone.set_text('13262523878')
        login_2=self.wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/awv')))
        login_2.click()
        print(1)
        password=self.wait.until(ec.presence_of_element_located((By.ID,"com.tencent.mm:id/ka")))
        password.set_text('hhj13262523878')
        print(2)
        next=self.wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/awv')))
        print(3)
        next.click()
        
    def enter(self):
        print(4)
        
        #return self.driver.page_source
        time.sleep(13)
        self.wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/j8')))
        print(self.driver.find_elements(By.XPATH,'//*[@resource-id="com.tencent.mm:id/qr"]'))
        try:
            print('yes')
            print(self.driver.find_elements(By.XPATH,'//*[@resource-id="com.tencent.mm:id/qr"][3]'))
            find=self.wait.until(ec.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/qr"][3]')))
            find.click()
        except:
            print('no')
            
        print(5)
        moments=self.wait.until(ec.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/kd"][1]')))
        print(6)
        moments.click()
        print('all down')
        
if __name__=='__main__':
    a=Moments()
    a.login()
    w=a.enter()
    print(w)
    a.driver.save_screenshot('1.png')