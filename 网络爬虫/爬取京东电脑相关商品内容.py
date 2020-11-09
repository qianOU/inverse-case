import requests
import re
from bs4 import BeautifulSoup
def getHtml(url):
    age={'user-agent':'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=age)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('wrong')
        return ''

def opreateText(list1,text):
    soup=BeautifulSoup(text,'lxml')
    #print(type(soup))
    for i in soup.find_all('li'):
       # print(type(i)) i 为 Tag类型
            
            try:
                '''   
              t=re.findall(r'<em>.</em><i>(\d.*?)</i>.*?<em>(.*?)<font',str(i),re.S)[0]
              #要转换i的类型才可以用findall函数  re.S为可使正则表达式中的.代替换行符，加‘r‘表示正则表达式 
               list1.append([float(t[0]),t[1]])
                '''
                t=i.select('a')[0]
                t=t['title'].strip() if t is not None else ''
                print(t)
                #print(t)
                q=i.select('div.p-price i')[0]
                q=q.string.strip() if q is not None else ''
                
                if t is not None and re.match(r'\d{4,5}.\d{2}',q):
                     
                      list1.append([t,q])
            except:
              
                continue
 
            
     


def writeFile(list1):
    with open('jindong.txt','w',encoding='utf-8') as f:
         for number,i in enumerate(list1):
             q='{1:*<8d}{0[1]:<8s}{0[0]:>50s}'.format(i,number,chr(12288))
             f.write(q)
             f.write('\n')
       
    
    
def main():
    a=[]
    q=list(range(1,8,2))
    for i in q:   
        url='https://search.jd.com/Search?keyword=电脑&enc=utf-8&wq=电脑'+'&page='+str(i)
        text=getHtml(url)
        opreateText(a,text)
    writeFile(a)
    
main()
