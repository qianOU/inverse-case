"""
terminate@author: Administrator
"""
from 简易代理池 import proxies
import requests
import csv
from pyquery import PyQuery as PQ
from requests.exceptions import ConnectionError
from multiprocessing import Pool
class K_proxies(proxies):
    def __init__(self,url):
        super().__init__(url)
        #self.url=url
        self.list=self.list_proxies()
        self.txt=self.get_text1()
            
    def get_text1(self):
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
                   print('访问失败！ try again')
                   self.get_text1()
            
           
        
    def find_element(self):
        text=PQ(self.txt)
        for item in text('tbody tr').items():
            dict1={}
            dict1.setdefault('IP',str(item('td:first-child').text()))
            dict1.setdefault('端口',str(item('td:nth-child(2)').text()))
            dict1.setdefault('地区',item('td:nth-child(5)').text())
            dict1.setdefault('匿名度',str(item('td:nth-child(3)').text()))
            dict1.setdefault('类型',item('td:nth-child(4)').text())
            dict1['日期']=item('td:last-child').text()
            print(dict1)
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
                 
              
if __name__=='__main__':
    p=Pool(4)
    proxies_list=[K_proxies("https://www.kuaidaili.com/free/inha/"+str(i)+"/") for i in range(1,5)]
    for j in proxies_list:
        p.apply_async(j.write_csv,args=())
    p.close()
    p.join()
    
"""
if __name__=='__main__':
    proxies_list=[K_proxies("https://www.kuaidaili.com/free/inha/"+str(i)+"/") for i in range(1,2)]
    for i in proxies_list:  
             i.write_csv()
"""