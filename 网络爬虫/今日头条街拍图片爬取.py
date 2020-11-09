# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:54:33 2018

@author: Administrator
"""
import requests
import json
import os
from hashlib import md5
from multiprocessing import Pool
import time
def ask_url(url,offset):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'x-requested-with':'XMLHttpRequest'
            }
    params={
            'keyword':'街拍',
            'offset':offset,
            'format':'json',
            'autoload':'true',
            'count':20,
            'cur_tab':1,
            'from':'search_tab',
            'pd':'synthesis'
            }
    response=requests.get(url,headers=headers,params=params)
    if response.status_code==200:
        # print('asking url is successful!')
        #return response.json()
        return json.loads(response.text)
    else:
        print('can\'t ask url!')
        return None

def askone_url(url):
    response=requests.get(url)
    try:
        if response.status_code==200:
            return response.content
    except requests.ConnectionError as e:
        print(e)
        
        
    
def opreate_text(text1):
    t=0
    try:
        a=text1.get('data')
        for i in a:
            z=i.get('title')
            for j in i.get('image_list'):
                q=askone_url('http:'+j.get('url').replace('list','large'))
                yield z,q
                t+=1
    except:
        print('the function of  opreate_text has an error!')
    print(t)
        
        
def write_jpg(tuples):
    if  not os.path.exists('E:\\街拍图库'):
         os.mkdir('E:\\街拍图库')
    if os.path.exists('E:\\街拍图库\\{}'.format(tuples[0])):
        with open('E:\\街拍图库\\{}\\{}.jpeg'.format(tuples[0],md5(tuples[1]).hexdigest()),'wb') as f:
            #朱此处用congtent作为MD5编码的源，因为congtent一定是不同的即md5码一定是不同的
            f.write(tuples[1])
    else:
        os.mkdir('E:\\街拍图库\\{}'.format(tuples[0]))
        with open('E:\\街拍图库\\{}\\{}.jpeg'.format(tuples[0],md5(tuples[1]).hexdigest()),'wb') as f:
            f.write(tuples[1])        
        
        
'''
#未用多进程时        
def main():
    url='https://www.toutiao.com/search_content/'
    for offset in range(0,160,20):
        content=ask_url(url,offset)
        for img_urls in opreate_text(content):
            write_jpg(img_urls)
'''

def main(offset):
    url='https://www.toutiao.com/search_content/'
    content=ask_url(url,offset)
    for img_urls in opreate_text(content):
        write_jpg(img_urls)

if __name__=='__main__': 
    start=time.clock()
    p=Pool()
    for i in range(0,160,20):
        p.apply_async(main,args=(i,))
    p.close()
    p.join()
    end=time.clock()
    print('take %6.3fs'%(end-start))
    print('*'*100,'all down!')
          

