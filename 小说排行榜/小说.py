# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:44:49 2018

@author: Administrator
"""
import requests
import os
from pyquery import PyQuery as PQ
import time
from multiprocessing.dummy import Pool

def get_url(url):
    response=requests.get(url)
    response.encoding=response.apparent_encoding
    if response.status_code==200:
        return response.text
    else:
        print(get_url.__name__,'has an problem %d'%response.status_code)

def op_all_text(text):
    text=PQ(text)
    try:
        for item in text('div.index_toplist').items():
            t=item('.toptab span').text().split()[0]
            format1='{}的{}'   
            p=list(zip([ i for i in item('.tabRight').text() if i!=' '],[i.attr('id')[-1] 
                      for i in item('.tabRight span').items()]))
            for ul in item('.topbooks ul').items():
                for name,num in p:               
                    a={'排行榜':t}    
                    if num==ul.parent().attr('id')[-1]:
                        a['排行榜']=format1.format(name,t)
                        p1=1
                        for li in ul('li').items():
                            a['更新日期']=li('.hits').text()
                            a['排名']=li('.num').text()
                            a['作品']=li('a').text()
                            a['作品链接']='https://www.qu.la'+li('a').attr('href')
                            yield a,p1
                            a={}
                            p1=0
                    else:
                        continue
    except:
        print('op_all_text has an error!')
        
                        
def mk_file():
    if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\小说排行榜'):
        os.mkdir(r'C:\Users\Administrator\Desktop\python爬虫小列子\小说排行榜')
    if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\小说排行榜\小说.txt'):
        f=open(r'C:\Users\Administrator\Desktop\python爬虫小列子\小说排行榜\小说.txt','w')
        f.close()

    
def write_to_file(text): 
    mk_file()
    with open(r'C:\Users\Administrator\Desktop\python爬虫小列子\小说排行榜\小说.txt','w+') as f:
        format1='{:20s}排行榜{:^20}'
        format2='排名: {排名:}\t 作品: {作品:10s}\t 作品链接: {作品链接:20s}\t 最后更新日期: {更新日期:10s}'
        for i,t in op_all_text(text):
            if t:
                f.write(format1.format(' ',i['排行榜']))
                f.write('*'*100+'\n'+'*'*100+'\n\n')
            f.write(format2.format(**i))
            f.write('\n')


def mk2_file(dict1):
    """
    list_name:排行榜
    name:书名
    创建相关文件夹
    """
    if not os.path.exists(r'F:\电影\%s'%dict1['list_name']):
        os.mkdir(r'F:\电影\%s'%dict1['list_name'])
    if not os.path.exists(r'F:\电影\{list_name}\{name}'.format(**dict1)):
        os.mkdir(r'F:\电影\{list_name}\{name}'.format(**dict1))
        
def write_one_chapter(url,dict1):
    """
    url：书每一章节的url
    list_name：排行榜
    name：书名
    把具体的某一个章节写入相应的文件中
    """
    response=requests.get(url)
    response.encoding=response.apparent_encoding
    text1=PQ(response.text)
    chapter=text1('div.bookname h1').text()
    body=text1('#content').text()          
    mk2_file(dict1)
    print(chapter)
    with open(r'F:\电影\{0}\{1}\{2}.txt'.format(dict1['list_name'],dict1['name'],chapter),'w+',encoding='utf-8') as f:
        f.write(body)
    
def get_all_chapters(text):
    """
    返回每一本书的链接与名字，与属于的排行榜
    """
    text=PQ(text)
    try:
        for item in text('div.index_toplist').items():
            list_name=item('.toptab span').text().split()[0]
            for q in item('.topbooks').items():
                if q.attr('id')[-1]=='1':
                    a={'list_name':list_name}
                    for li in q('li').items():
                        a['href']='https://www.qu.la'+li('a').attr('href')
                        a['name']=li('a').text()
                        yield a
                        a={}#要清空a，否则因为a的引用一直未变，所以对于同一个排行榜中的a的应用未变，故每一个排行榜中只能得最后一个文件
                        a={'list_name':list_name}                      

    except:
        print('get_all_chapter has an error!')
                    
def get_book(list1):
    """
    list1:由书名，书链接，所在排行榜组成的字典
    目的是得到每一本书的所有章节并写入相关文件中
    """
    text=get_url(list1['href'])                       
    text=PQ(text)
    text=text('div#list')
    t=0 #只是为了测试
    for dd in text('dd').items():
        try:
            #只是为了测试
            if 'book' in dd('a').attr('href'):
                t+=1
                print(list1)
                if t==8:
                    break
                write_one_chapter('https://www.qu.la'+dd('a').attr('href'),list1)
                if t==4:#只是为了测试
                    return #只是为了测试
        except:
            print('get_book has a problem!')
        
            continue
'''
def main():
    url='https://www.qu.la/paihangbang/'        
    text=get_url(url)
    write_to_file(text)
    print('one step is successful!')
    for i,list1 in enumerate(get_all_chapters(text)):
        get_book(list1)
        print('step %d has done'%(i+2)) 
    
main()
'''
"""text=get_url('https://www.qu.la/paihangbang/')   
for i in get_all_chapters(text):
    get_book(i)
             
"""

                      
if __name__=='__main__':
    """
    启用多线程,这里打开了八个线程，一般线程数
    要通过做实验比较得出最优的线程数量
    """
    start=time.perf_counter()
    p=Pool(8)
    url='https://www.qu.la/paihangbang/'        
    text=get_url(url)
    write_to_file(text)
    print('one step is successful!')
    z=p.map(get_book,get_all_chapters(text))
    print('ALL subprocesses done!')
    end=time.perf_counter()
    print("expend %6.3fs"%(end-start))
    
"""
if __name__=='__main__':
    p=Pool(8)
    url='https://www.qu.la/paihangbang/'        
    text=get_url(url)
    write_to_file(text)
    print('one step is successful!')
    print('*'*100)
    for i in get_all_chapters(text):
        get_book(i)
    
"""
