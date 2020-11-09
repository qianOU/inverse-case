# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:47:49 2019

@author: Administrator
"""
import csv
import time
import json
import requests
from pyquery import PyQuery as PQ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#from ./cities代码 import parse_station
from urllib.parse import urlencode
requests.urllib3.disable_warnings()
class find_tickets():
    def __init__(self,start,termination,date,idd,train_kind):
        self.url='https://kyfw.12306.cn/otn/leftTicket/init?'
        self.start=start
        self.termination=termination
        self.date=date
        self.browser=webdriver.Chrome(chrome_options=chrome_options)
        if idd=='Y' and train_kind=='Y':
            self.flag='Y,Y,Y'
        elif idd=='Y':
            self.flag='Y,N,Y'
        elif train_kind=='Y':
            self.flag='N,Y,Y'
        else:
            self.flag='N,N,Y'
    
    def callback_url(self):
        f=open('cities.json','r',encoding='utf-8')
        w=json.loads(f.read())
        f.close()
        start=w.get(self.start,None)
        termination=w.get(self.termination,None)
        #https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=上海,SHH&ts=玉山,YNG&date=2019-01-03&flag=Y,N,Y
        params={
                'linktypeid':'dc',
                'fs':self.start+','+start,
                'ts':self.termination+','+termination,
                'date':self.date,
                'flag':self.flag
                }
        t=urlencode(params).replace('%2C',',')
        (self.browser).get(self.url+t)
        print(self.browser.current_url)
        self.browser.implicitly_wait(6)
        return self.browser.page_source
        #response=requests.get(self.url+t,headers=headers)
        #response=requests.get(self.url,params=params,verify=False,headers=
                              #{'User-Agent':self.get_agent()})
        
        
#        if response.status_code==200:
#            response.encoding=response.apparent_encoding
#            return response.text
#        else:
#            print('状态码：',response.status_code)
#            raise ConnectionError('输入参数有错!')
    
    def opr_text(self):
        text=PQ(self.callback_url())
        self.browser.close()
        #print(text)
        #print(text('#queryLeftTable').text())
        for item in text('table tbody#queryLeftTable tr').items():
           if 'ticket' in item.attr('id'):
            #print(item)
            a={}
            a['始发站']=item('strong.start-s').text()
            a['终点站']=item('strong.start-s').siblings('strong').text()
            a['出发时间']=item('strong.start-t').text()
            a['到达时间']=item('strong.color999').text()
            #print(a)
            q=item('div.ls').attr('id')[0:-3]
            a['历时']=item('div.ls strong').text()
            a['几日到达']=item('div.ls span').text()
            a['商务座']=item('td#SWZ_'+q).text()
            a['一等座']=item('td#ZY_'+q).text()
            a['二等座']=item('td#ZE_'+q).text()
            a['高级软卧']=item('td#GR_'+q).text()
            a['软卧一等']=item('td#RW_'+q).text()
            a['动卧']=item('td#SRRB_'+q).text()
            a['硬卧二等卧']=item('td#YW_'+q).text()
            a['软座']=item('td#RZ_'+q).text()
            a['硬座']=item('td#YZ_'+q).text()
            a['无座']=item('td#WZ_'+q).text()
            yield a
           else:
               continue
    
    def  write_to_file(self):
        with open('trains_plan.csv','w',encoding='cp936',newline='') as f:
            filed_names=['始发站','终点站','出发时间','到达时间',
                         '历时','几日到达','商务座','一等座','二等座',
                         '高级软卧','软卧一等','动卧','硬卧二等卧','软座',
                         '硬座','无座']
            writer=csv.DictWriter(f,filed_names,delimiter=' ')
            writer.writeheader()
            for i in self.opr_text():
                writer.writerow(i)
                print(i)
                print('='*120)
            print('写入完成')
        
if __name__=="__main__":
    s=time.perf_counter()
    # start=input('始发站:')
    # termination=input('终点站：')
    # date=input('坐车时间:eg(2019-01-03) :')
    # id=input('身份:学生 Y/普通 N :')
    # train_kind=input('只坐动车、高铁:Y/N :')
    start = '玉山南'
    termination = '上海虹桥'
    date = '2019-05-18'
    id = 'N'
    train_kind = 'N'
    print(' '*15,'查询中...')
    w=find_tickets(start,termination,date,id,train_kind)
    w.write_to_file()       
    print('查询完成!\t用时:{:4.2f}s'.format((time.perf_counter()-s)))
