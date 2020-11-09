# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import csv
import random
from pyquery import PyQuery as PQ
from requests.exceptions import ConnectionError
from multiprocessing import Pool
class K_proxies():
    def __init__(self,url):
        self.url=url
        self.headers={
                'User-Agent':self.get_agent()
                     }
        self.list=self.list_proxies()
        self.text=self.get_text()
        
    
    def get_agent(self):
        agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
                  'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                  'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
        return random.choice(agents)  
    
    
    def get_text(self):
        print('尝试访问%s'%self.url)
        for i in self.list:
            try:
                 proxies={'http':'http://'+i[0]+':'+i[1]}
                 response=requests.get(self.url,headers=self.headers,proxies=proxies,timeout=2)
                 if response.status_code==200:
                     print(i)
                     print('访问网页成功！')
                     return response.text
#            else:
#                raise ConnectionError("you can't connent to %s"%(self.url))
#                self.get_text();
            except ConnectionError:
                   print('try again')
                   self.get_text();

            
        
    def find_element(self):
        text=PQ(self.text)
        for item in text('tbody tr').items():
            dict1={}
            dict1.setdefault('IP',str(item('td:first-child').text()))
            dict1.setdefault('端口',str(item('td:nth-child(2)').text()))
            dict1.setdefault('地区',item('td:nth-child(5)').text())
            dict1.setdefault('匿名度',str(item('td:nth-child(3)').text()))
            dict1.setdefault('类型',item('td:nth-child(4)').text())
            dict1['日期']=item('td:last-child').text()
            yield dict1
            #self.list.append(dict1)
        
    def list_proxies(self):
        """
        a中的每一个元素为
        """
        a=[]
        with open('proxies.csv','r') as f:
            text=f.readlines()
        for i in text:
            q=i.replace('\n','')
            if q:
                a.append(q.split(' '))
        return a
 
    
    def random_proxy(self):
        q=random.choice(self.list)
        print('proxies=',{'http':'http://'+q[0]+':'+q[-1]})
        return {'https':'https://'+q[0]+':'+q[-1]}


    def write_csv(self):       
        with open('./proxies.csv','a',newline='',encoding='utf-8') as f:
#            fieldnames=['IP','端口','地区','类型','匿名度','日期']
#            writer=csv.DictWriter(f,fieldnames=fieldnames)
#            writer.writeheader()
#            writer=csv.DictWriter(f,fieldnames=fieldnames,delimiter=' ')
            writer=csv.writer(f,delimiter=' ')
            for i in self.test():
                if i is not None:
                     writer.writerow(i)


    def test(self):
        url='http://httpbin.org/get'
        for pro in self.find_element():
          proxies={'http':'http://'+pro['IP']+':'+pro['端口']}
          print(proxies)
          try:
            t=requests.get(url,headers=self.headers,proxies=proxies,timeout=2)
            if t.status_code==200:
                print(t.text)
                print("%s 测试通过!"%(pro['IP']+':'+pro['端口']))
                yield [pro['IP'],pro['端口']]
                  #self.list.append(proxy)
            else:
                 print("%s抱歉测试未通过!"(pro['IP']+':'+pro['端口']),t.status_code)
          except:
              print("%s抱歉测试未通过!")
              print('next_one')
              continue
                 
"""                
if __name__=='__main__':
    p=Pool(4)
    proxies_list=[K_proxies("https://www.kuaidaili.com/free/inha/"+str(i)+"/") for i in range(1,50)]
    for j in proxies_list:
        p.apply_async(j.write_csv,args=())
    p.close()
    p.join()
"""
if __name__=='__main__':
    proxies_list=[K_proxies("https://www.kuaidaili.com/free/inha/"+str(i)+"/") for i in range(1,2)]
    for i in proxies_list:  
             i.write_csv()
    
        
                   
                  
        
        