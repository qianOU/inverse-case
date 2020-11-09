# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:58:19 2018

@author: Administrator
"""
import requests
import os
from pyquery import PyQuery as PQ
import time
from selenium import webdriver
def sele_url(url):
    browser=webdriver.Chrome()
    try:
        browser.get(url)
        browser.implicitly_wait(7)
        return browser.page_source
    except:
        print('sele_url has an error!')
    finally:
        browser.close()
        
def get_url(url):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
            }
    response=requests.get(url,headers=headers)
    response.raise_for_status()
    response.encoding=response.apparent_encoding
    if response.status_code==200:
        print(response.text)
        return response.text
    else:
        print('get_url has wrong!')

def mk_file():
    if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟'):
        os.mkdir(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟')
    if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟\英雄联盟.txt'):
        f=open(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟\英雄联盟.txt','w+')
        f.close()
    
def opr_text(text):
      text=PQ(text)
      a={}
      try:
        for item in text('ul.area-vs-list').items():
            #print(item)
            for li in item('li').items():
                a={}
               # print(li,'*'*100)
                if 'win' in li('a.up').attr('class'):
                    a['胜队']=li('a.up b.name').text()
                    a['败队']=li('a.down b.name').text()
                else:
                    a['胜队']=li('a.down b.name').text()
                    a['败队']=li('a.up b.name').text()
                a['比赛日期']=li('p.time').text()
                a['比赛视频网站']=li('p.team-btn a').attr('href')
                yield a               
      except:
            print('opr_text has errors!')

def wri_to_file(text):
    mk_file()
    format1='胜队：{胜队:<15s}\t 败队：{败队:<15s}\t 比赛日期：{比赛日期:<25s}\t 比赛视频网站：{比赛视频网站}'
    with open(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟\英雄联盟.txt','w+',encoding='utf-8') as f:
      try:
        for i in opr_text(text):
            f.write(format1.format(**i))
            f.write('\n')
        print('successful!')
      except:
        print('wrong')

def main():
    url='https://lpl.qq.com/es/allstar/2018/index.html?ADTAG=innercop.lol.web.top'
    #text=get_url(url)
    text=sele_url(url)
    wri_to_file(text)

main()