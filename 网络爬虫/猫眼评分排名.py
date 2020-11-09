# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:01:35 2018

@author: Administrator
"""
import re,os
import requests
url='https://maoyan.com/board/4'

def get_request(url,params):
    
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
            }
    try:
        response=requests.get(url,headers=headers,params=params)
        if response.status_code==200:
            return response.text
            
        else:
            print(response.status_code)
    except:
        print('get_request() has a problem!')
        
def get_contents(url):
    
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
            }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.content
            
        else:
            print(response.status_code)
    except:
        print('get_request() has a problem!')
     
def opreate_html(html,list1,list3):
    pattren=re.compile(r'<a.*?title="(.*?)".*?<p\sclass="star">(.*?)<.*?<p\sclass="releasetime">(.*?)<',re.S)
    test=re.compile(r'<img .*?[^title].*?alt="(.*?)".*?src="(.*?)"',re.S)
    w=re.findall(pattren,html)
    q=re.findall(r'<img data-src="(.*?)" alt="(.*?)"',html)
    list3.extend(q)
    #list1.extend(w)
    
def print_html(list2):
    for z,i in enumerate(list2):
        print('{1:<5d} {0[0]:<15s}{0[1]:^20s}{0[2]:>15s}'.format([j.strip() for j in i],z+1))
        
         
def all_data(url,list3):
     list1=[]
     params={
            'offset':0
            }
     for i in range(0,100,10):
         params['offset']=i
         text=get_request(url,params)
         opreate_html(text,list1,list3)
     return list1
 
def writer_png(list3):
    if not os.path.exists(r'C:\Users\Administrator\Desktop\网络爬虫\电影图片'):
        os.mkdir(r'C:\Users\Administrator\Desktop\网络爬虫\电影图片')
    os.chdir(r'C:\Users\Administrator\Desktop\网络爬虫\电影图片')
    for z in list3:
        
             text=get_contents(z[0])
             print(z)
             with open('%s.png'%z[1],'wb+') as f:
                 f.write(text)
"""                 
def writer_html(list3):
    t=open('maoyanspider.txt','w')
    t.close()  
    with open('maoyanspider.txt','a+') as f:
         for z,i in enumerate(list3):
             f.write('{1:<5d}\t{0[0]:<20s}\t{0[1]:<50s}\t{0[2]:<30s}'.format([j.strip() for j in i],z+1,chr(12288)))
             f.write('\n')
       
    print('the work of write has done!')
""" 
    
def main():
    list3=[]
    url='https://maoyan.com/board/4'
    list1=all_data(url,list3)
    #print_html(list1)
    #writer_html(list1)
    writer_png(list3)
main()
