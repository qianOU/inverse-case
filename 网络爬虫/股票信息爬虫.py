# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:30:26 2018

@author: Administrator
"""
import re
import requests
from bs4 import BeautifulSoup
def getHtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('wrong!')
        return ''
    
def opreate(list1,list2,text):
     z=1
     soup=BeautifulSoup(text,'lxml')
     for i in soup.find_all('li'):       
       for j in i.children:
        if j:
         try:
           z+=1
           #t=(j.attrs['href']).split('/')[-1]
           t=re.findall('s[hz]\d{6}',j.attrs['href'])[0]
           #注：re.findall返回的是列表类型，所以要加[0],确保t是字符串
           if t[0:2]=='sz':
               list1.append(j.get_text())
           elif t[0:2]=='sh':
               list2.append(j.string)
           else:
               continue
         except:  
             continue
        else:
          continue
     print('the length is',z)  
    
def printText(list1,list2):
    c,q=(1,1)
    print('深圳')
    for i in list1:
        print(i)
        c=c+1
    print('上海')
    for i in list2:
        print(i)
        q=q+1
    print(c+q)

        
def main():
    url='http://quote.eastmoney.com/stocklist.html'
    a=[]
    b=[]
    t=getHtml(url)
    opreate(a,b,t)
    printText(a,b)
main()
    
