# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:44:30 2018

@author: Administrator
"""
import requests
import csv
import random
from pyquery import PyQuery as PQ
from requests.exceptions import ConnectionError
from multiprocessing import Pool
#from multiprocessing.dummy import Pool as ThreadPool
class proxies(object):
    def __init__(self, url):
        self.url=url
        self.headers={
                'User-Agent':self.get_agent()
                     }      
        self.text=self.get_text() if type(self).__name__=='proxies' else None
    def get_agent(self):
        agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
                  'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
        return random.choice(agents)
    
    def get_text(self):
        print('尝试访问%s'%self.url)
        response=requests.get(self.url,headers=self.headers)
        if response.status_code==200:
            print('访问网页成功！')
            return response.text
        else:
            try:
                 raise ConnectionError("you can't connent to %s"%(self.url))
            except ConnectionError as e:
                print('访问失败，try again！',e)                

        
    def find_element(self):
        text=PQ(self.text)
        for item in text('tbody tr').items():
            dict1={}
            dict1.setdefault('IP',str(item('td:first-child').text()))
            dict1.setdefault('端口',str(item('td:nth-child(2)').text()))
            dict1.setdefault('地区',item('td:nth-child(3)').text())
            dict1.setdefault('类型',str(item('td:nth-child(4)').text()))
            dict1['日期']=item('td:last-child').text()
            print(dict1)
            yield dict1
            #self.list.append(dict1)    
            
    def test(self):
        url='http://httpbin.org/get'
        for proxy in self.find_element():
            proxies={'http':'http://'+proxy['IP']+':'+proxy['端口']}
            print('测试{}'.format(proxy['IP']))
            try:
                t=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'},proxies=proxies,timeout=2)
                if t.status_code==200:
                    print(t.text)
                    print("%s 测试通过!"%(proxy['IP']+":"+proxy['端口']))
                    yield proxy
                    #self.list.append(proxy)
                else:
                     print("%s抱歉测试未通过!"(proxy['IP']+":"+proxy['端口']))
            except:
                print("%s抱歉测试未通过!")
                print('nextone')
                continue
            
    def write_csv(self):
        with open('./proxies.csv','a',newline='') as f:
#            fieldnames=['IP','端口','地区','类型','日期']
#            writer=csv.DictWriter(f,fieldnames=fieldnames)
#            writer.writeheader()
#            writer=csv.DictWriter(f,fieldnames=fieldnames,delimiter=' ')
            writer=csv.writer(f,delimiter=' ')
            for i in self.test():
                if i is not None:
                     writer.writerow([i['IP'],i['端口']])
            
    

if __name__=='__main__':
    p=Pool(4)
    proxies_list=[proxies("http://www.89ip.cn/index_"+str(i)+".html") for i in range(1,4)]
    for j in proxies_list:
        p.apply_async(j.write_csv,args=())
    p.close()
    p.join()
   
"""
if __name__=='__main__':
    proxies_list=[proxies("http://www.89ip.cn/index_"+str(i)+".html") for i in range(1,3)]
    for i in proxies_list:        
        i.write_csv()
"""     