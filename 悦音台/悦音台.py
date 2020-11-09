# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:59:36 2018

@author: Administrator
"""
import requests,os,random,json
from requests.exceptions import ProxyError
from pyquery import PyQuery
from urllib.parse import unquote
def get_agent():
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    return random.choice(agents)
def get_proxy():
    proxies=[("101.81.217.207",8060),
            ("180.140.191.233",37980),
            
            ]
    t=random.choice(proxies)

    return 'http://'+t[0]+':'+str(t[1])            

def get_request(url):
   headers={
            'User-Agent':get_agent(),
            }
   proxies={
            'http':get_proxy(),
            }
   try:
    t=requests.get(url,headers=headers,proxies=proxies)
    t.encoding='utf-8'
    if t.status_code==200:
        return t.text
    else:
        get_request(url)
   except ProxyError:
        get_request(url)
        
    
    
def opr_text(text):
    text=PyQuery(text)
    for i in text('.vitem').items():
        item={}
        item['score']=unquote(i('.score_box h3').text())
        item['mark']=unquote(i('.top_num').text())
        item['video address']=unquote(i('a.video-bo-img').attr('href'))
        item['name']=unquote(i('a.video-bo-img img').attr('alt'))
        item['author']=unquote(i('a.special').text())
        item['created time']=unquote(i('p.c9').text())
        print(item)
        yield item
        
def mk_file():
    if not os.path.exists('./悦音台'):
        os.mkdir('./悦音台')
        
def main():
    url='http://vchart.yinyuetai.com/vchart/trends?area=ML&page='
    for page in range(1,4):
        uri=url+str(page)
        print(uri)
        text=get_request(uri)
        mk_file()
        os.chdir('./悦音台')
        with open('悦音台.json','a',encoding='utf-8') as f:
            for item in opr_text(text):
                f.write(json.dumps(item,ensure_ascii=False))
                f.write('\n')      
            print('{:4.2f}% has done!\r'.format(page/3*100))

main()
        
