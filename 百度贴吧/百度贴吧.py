# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:26:18 2018

@author: Administrator
"""
import requests,os
from pyquery import PyQuery as PQ
#from multiprocessing import Pool
import time
def req_url(page,url):
    url=url+'&pn='+str(page)
#    headers={
#            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
#            }
    response=requests.get(url,timeout=10)
    response.encoding='utf-8'
    if response.status_code==200:
        return response.text
    else:
        print('req_url has a promblem and code is %d'%response.status_code)
        return None

def opr_text(text):
    text=PQ(text)
    try:
        for item in text('li.j_thread_list.clearfix').items():
             a={}
             a['标题']=item('div.threadlist_title a').text()           
             a['链接']=('http://tieba.baidu.com'+item('div.threadlist_title a').attr('href')) if item('div.threadlist_title a').attr('href') else ''
             a['创建时间']=item('div.threadlist_author .is_show_create_time').text()
             a['作者']=item('span.frs-author-name-wrap').text()
             a['发帖图片地址:']=item('li a.thumbnail img').attr('src') if item('li a.thumbnail img').attr('src') else '没图片'
             a['最后的回复时间']=item('span.pull_right').text()
             a['回复数量']=item('.threadlist_rep_num').text()
             yield a
    except:
        print('has some thing wrong!')

def percent(page):
    s='{}% is done!'.format(page/2)
    print(s)

def main():
     url='http://tieba.baidu.com/f?kw=上海大学&ie=utf-8'
     format1='{:}：{:}\t'
     if os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\百度贴吧\百度贴吧.txt'):
        f=open('百度贴吧.txt','w')
        f.close()
     else:
        os.mkdir(r'C:\Users\Administrator\Desktop\python爬虫小列子\百度贴吧\百度贴吧.txt')
        
     with open('百度贴吧.txt','a+',encoding='utf-8') as f:
      for page in range(0,250,50):
        if req_url(page,url):
            text=req_url(page,url)
            time.sleep(0.7)
            for i in opr_text(text):
                for j in i:
                    if i[j]:
                          f.write(format1.format(j,i[j],' '*4))
                f.write('\n')
            percent(page)
        else:
            print('wrong!')
            return None
           
main()
                
                
            
        
        
