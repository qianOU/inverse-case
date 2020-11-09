# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:10:26 2018

@author: Administrator
"""
import requests,json
from pyquery import PyQuery as pq
from pymongo import MongoClient
#from redis import StrictRedis as sr
import pymysql
def  parse_url(url,page):
    params={
            'containerid':'2304136025466664_-_WEIBO_SECOND_PROFILE_WEIBO',
            'page_type':'03',
            'page':page
            }
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
            'Host':'m.weibo.cn',
            'Cookie':'SUB=_2A25xBlUADeRhGeBO6VcV9ijKzTiIHXVSCXtIrDV6PUJbkdBeLWX5kW1NSjDLflNEKa8Gmj95F134i1M430hNlL4D; SUHB=0IIV6hnD0mSO8r; SCF=AtV1Neg1LW_mpkBFlyqxFb6UsvTn01g8eSXI5G06fDNwWhQXYzxFLK7Jx_d08hQZBVVZO43wI1oyVlViNxXh1ZE.; SSOLoginState=1543644496; _T_WM=7a1f6d736fb81bc6de2611a77b2a2883; MLOGIN=1; WEIBOCN_FROM=1110106030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2304136025466664_-_WEIBO_SECOND_PROFILE_WEIBO%26fid%3D2304136025466664_-_WEIBO_SECOND_PROFILE_WEIBO%26uicode%3D10000011'

            }
    try:
        response=requests.get(url,headers=headers,params=params)
        if response.status_code==200:
            return response.text
    except ConnectionError as e:
        print('the connection is wrong! and the reason is %s'%(e.args))
        
        
def opreate_text(text):
    text=json.loads(text)
   
    try:
        items=text.get('data').get('cards')
        for j in items:
            i=j.get('mblog')
            a={}
            a['created_at']=i.get('created_at')
            a['reads_count']=i.get('reads_count')
            a['comments-count']=i.get('comments_count')
            a['attitudes_count']=i.get('attitudes_count')
            a['text']=pq(i.get('text')).text() 
            yield a  
    except:
        print('the opreate_text has an error!')

#(1)mongodb用来存储，最优，可以储存键名相同的量
def save_mongo(key):
    #client=MongoClient(host='localhost',port=27017)
    #db=client.weibo
   # collection=db.weibo
    global collection
    print(type(collection))
    if key:
       try:
           print(key)
           collection.insert_one(key)
           print('saved successfully!')
       except:
           print('wrong!')
 

'''
#(2)redis只能用来存储键名不同的量，否则重复覆盖
def save_redis(key):
    redis=sr(host='localhost',port=6379,db=0,password=13262523878)
    print(redis)
    for i in key.keys():
        redis.set(i,key.get(i))
  
   #(3)用mysql存储失败
def save_mysql(key):
    db=pymysql.connect(host='localhost',port=3306,user='root',password=13262523878)
    cursor=db.cursor()
    sql='CREATE TABLE IF NOT EXISTS weibo(created_at VARCHAR(255),read_count INT NOT NULL,comments-count INT NOT NULL,attitudes_count INT NOT NULL,text VARCHAR(255))'
    cursor.execute(sql)
    print(sql)
    sql='INSERT INTO weibo({0}) values({1})'.format(','.join(key.keys()),','.join(['%s']*len(key))) 
    try:
        cursor.execute(sql,tuple(key.values()))
        db.commit()
    except:
        db.rollback()
'''    
          

url='https://m.weibo.cn/api/container/getIndex'
client=MongoClient(host='localhost',port=27017)
db=client.weibo
collection=db.weibo
print('='*100)
for page in range(1,9):
    text=parse_url(url,page)
    for num,key in enumerate(opreate_text(text)):
        print('',end='')
        save_mongo(key)
        #save_redis(key)
        #save_mysql(key)

        
