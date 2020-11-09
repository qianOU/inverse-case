# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:25:19 2019

@author: Administrator
"""
import requests
import re
import json
from requests.exceptions import ConnectionError
#关闭警告
requests.packages.urllib3.disable_warnings()


class parse_stations():
    def __init__(self,url):
        self.url=url
        
    def get_cities(self):
        #开启免验证证书
        response=requests.get(self.url,verify=False)
        response.raise_for_status
        if response.status_code==200:
            response.encoding=response.apparent_encoding
            return response.text
        else:
            raise ConnectionError('wrong!')
    
    def opr_text(self):
        text=self.get_cities()
        text=text
        pattren=re.compile(r'@(.*?)\|\d',re.S)
        items=re.findall(pattren,text)
        a={}
        for i in items:
            w=[j.replace('\n','') for j in i.split('|')]
            a.setdefault(w[1],w[2])
        print(a)
        return a
            
    def write_to_file(self):
        with open(r'cities.json','w',encoding='utf-8') as f:
            cities_code=self.opr_text()
            f.write(json.dumps(cities_code,ensure_ascii=False))

if __name__=='__main__':
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8392'
    a=parse_stations(url)
    a.write_to_file()
