# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:49:29 2018

@author: Administrator
"""
import requests
from pyquery import PyQuery as pq
def get_text(url):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Cookie':'_xsrf=JPDjEQiQx99TKco16MhycBC3yH5Xpnl7; _zap=7e520d55-36de-4447-977e-6f7edd4e3e65; d_c0="AFDllOhXUg6PTpsLpUfGpwrWv-h4qPD3SJU=|1538824140"; q_c1=ea70fd6e49b6479db40e940a277833d4|1543040773000|1543040773000; l_cap_id="ZWEyMTMxOTc2ZTE0NDI1ODgxZTdkOTk1YzJjM2Q5Zjk=|1543050180|23ca1f1009818635a94270f99cfe77370b13b9c6"; r_cap_id="YzkwODVkNjk3MjFmNDE5NWE4OTVlMmZjOTQzMzFlMWE=|1543050180|77fcce2e73b8b2ba401c560f9130e2283514a3c9"; cap_id="NjcxZmZhOTkzYTYwNGNhZjkyYWJiODM5MmYzMGRmNzI=|1543050180|d1af696dd1783f5a286392a83f41165f3676d769"; capsion_ticket="2|1:0|10:1543326158|14:capsion_ticket|44:ZDNjYmY2NDMxOThhNGQ2NWJiMGYzYzI2ZDBmZjUxOTM=|5408afa46725da5bcc957241a125d03ee80ac724a47a3798a7e2114eda2b4617"; z_c0="2|1:0|10:1543326161|4:z_c0|92:Mi4xT1lCQkJRQUFBQUFBVU9XVTZGZFNEaVlBQUFCZ0FsVk4wWmZxWEFBaldmdWNqQzZCUVF1bDJCZXdzYUpicy01ZVFR|a1ab5fd140e52ef9993ee2061849d4c7b8d13d26a3ed8f8ce20d7ee1cdc3dda3"; tst=h; tgw_l7_route=e0a07617c1a38385364125951b19eef8; __utma=51854390.558160433.1543327622.1543327622.1543329811.2; __utmb=51854390.0.10.1543329811; __utmc=51854390; __utmz=51854390.1543327622.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20170621=1^3=entry_date=20170621=1'
            }    
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        print(response.status_code,'-----this means somesthing wrong! ')
    pass
def find_point(text):
    html=pq(text)
    a={}
    for i,j in enumerate(html('.explore-feed').items()):
        try:
              a['number']=str(i+1)
              a['question']='Question:'+j.find('.question_link').text() 
              a['name']='name:'+j.find('a.author-link').text()          
              a['summary']='Summary:'+''.join(pq(j.find('.content').html()).text().split())
              yield a
              a={}
        except:
              print('hello')
              continue
    
def write_txt(text):
    for i in find_point(text):
        with open('zhihu.txt','a',encoding='utf-8') as f:
            f.write('\n'.join([i[j].strip() for j in i]))
            f.write('\n'+'='*100+'\n')
            
            
        
def main():
    url='https://www.zhihu.com/explore'
    text=get_text(url)
  #  a=find_point(text)
    write_txt(text)
main()