# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:58:48 2019

@author: Administrator
"""
import threading
import pickle
import requests
import queue
from lxml import etree
import re
import os
import time

def get_url():
    f = open(r'E:\python\test.txt','rb')
    w = pickle.loads(f.read())
    print(w)
    f.close()
    return w
 
class Producter(threading.Thread):
    def __init__(self,image_queue,page_queue,*args,**kwgs):
        self.image_queue = image_queue
        self.page_queue = page_queue
        super().__init__(*args,**kwgs)
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        }
        
    def run(self):
        while True:
            if self.page_queue.empty():
                return 
            url_list = self.page_queue.get()[1:]
            for url in url_list:
                response=requests.get(url,headers=self.headers)
                if response.status_code == 200:
                    response.encoding = 'utf-8'
                    html = etree.HTML(response.text)
                    image=html.xpath('/html/body/div[4]/center/img/@src')
                    print(html.xpath('/html/body/div[2]/div[1]/h1/text()'))
                    self.image_queue.put((url,image))
                    print('='*30)
                    
        
class Consumer(threading.Thread):
     def __init__(self,image_queue,page_queue,*args,**kwgs):
        self.image_queue = image_queue
        self.page_queue = page_queue
        self.headers =  {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
        }
        super().__init__(*args,**kwgs)
    
     def run(self):
        while True:
            if self.image_queue.empty() and self.page_queue.empty():
                return 
            URL,list_1 = self.image_queue.get()
            self.headers['Referer'] = URL
            for url in list_1:
                response=requests.get(url,headers = self.headers)
                if response.status_code == 200:
                    print('*'*40)
                    os.chdir('E:\python')
                    with open (''.join(url.split('/')[-2:]),'wb') as f:
                        f.write(response.content)
                    print(''.join(url.split('/')[-2:]),'完成了！')
    

    
w=''
def main():
    global w
    image_queue = queue.Queue(-1)
    page_queue = queue.Queue(1000)
    w=get_url()
    print(w)
    for i in range(100,1000,4):
        page_queue.put(list(w.values())[i])
    for i in range(2):
        t = Producter(image_queue,page_queue)
        t.start()
    time.sleep(3)
    print(image_queue.get())
    print(image_queue.empty(),
          page_queue.empty())
    for i in range(4):
      t = Consumer(image_queue,page_queue)
      t.start()
     
        
        
    
if __name__ == "__main__":
    main()