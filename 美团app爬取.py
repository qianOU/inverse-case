# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:26:44 2019

@author: Administrator
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import os,time
from pymongo import MongoClient
TIME_OUT=40 
PLATFORM='Android'
DEVICE_NAME='ERMDU17817004817'
APP_PACKAGE='com.sankuai.meituan.takeoutnew'
APP_ACTIVITY='com.sankuai.waimai.business.page.homepage.MainActivity'
DRIVE_SERVER='http://localhost:4723/wd/hub'
MONGO_URL='localhost'
MONGO_DB='moments'
MONGO_COLLECTION='moments'
class meituang():
    def __init__(self):
        self.driver=webdriver()
        self.db=MongoClient[MONGO_DB]
        self.collection=self.db[MONGO_COLLECTION]
        self.wait=WebDriverWait(self.driver,TIME_OUT)
        self.action=TouchAction(self.driver)
    def login(self):
        next1=self.wait.until(ec.element_to_be_clickable((By.ID,"com.android.packageinstaller:id/permission_allow_button")))
        next1.click()
        nex1=self.wait.until(ec.element_to_be_clickable((By.ID,"com.android.packageinstaller:id/permission_allow_button")))
        nex1.click()
        nex1=self.wait.until(ec.element_to_be_clickable((By.ID,"com.android.packageinstaller:id/permission_allow_button")))
        nex1.click()
        quxiao=self.wait.until(ec.element_to_be_clickable((By.ID,"com.sankuai.meituan.takeoutnew:id/close")))
        quxiao.click()
        """
        self.driver.implicitly(5)
        self.action.tap(x=367, y=1227).perform()
        w=self.wait.until(ec.presence_of_element_located((By.ID,'com.sankuai.meituan.takeoutnew:id/list_orderList_orderList')))
        self.action.tap(x=345, y=812).perform()
        piple=self.wait.until(ec.presence_of_element_located((By.ID,'com.sankuai.meituan.takeoutnew:id/user_password_login')))
        piple.click()
        phone=self.wait.until(ec.presence_of_element_located((By.ID,'com.sankuai.meituan.takeoutnew:id/passport_mobile_phone')))
        phone.set_text('13262523878')
        password=self.wait.until(ec.presence_of_element_located((By.ID,'com.sankuai.meituan.takeoutnew:id/edit_password')))
        password.set_text('hhj123456789')
        login1=self.wait.until(ec.presence_of_element_located((By.ID,'com.sankuai.meituan.takeoutnew:id/login_button')))
        login1.click()
        """
    def enter(self):
        time.sleep(10)
        
        
        
        