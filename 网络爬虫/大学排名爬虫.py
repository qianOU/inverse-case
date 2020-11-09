import requests
import bs4
from bs4 import BeautifulSoup
def getHtml(url):
    try:
         r=requests.get(url)
         r.raise_for_status()
         r.encoding=r.apparent_encoding
         return r.text
    except:
        return ''

def opreateHtml(ulist,text):
    soup=BeautifulSoup(text,'html.parser')
    for tr in soup.find('tbody').children:
        if type(tr)==bs4.element.Tag:#等价于isinstance(tr,bs4.element.Tag)
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,int(tds[0].string)])
def printHtml(ulist,num):
    th1='{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(th1.format("排名",'学校','地址',chr(12288)))
    #th2=sorted(ulist,key=lambda ulist:ulist[3],reverse=True) 倒转排序
    for i in range(num):
     #   print(th1.format(th2[i][0],th2[i][1],th2[i][2],chr(12288))) 倒转输出最后几名
         print(th1.format(ulist[i][0],ulist[i][1],ulist[i][2],chr(12288)))
def main():
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    ulist=[]
    z=getHtml(url)
    if z=='':
        print('wrong!')
        return
    opreateHtml(ulist,z)
    printHtml(ulist,100)
main()
