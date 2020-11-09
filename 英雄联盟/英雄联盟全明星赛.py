import requests
import os,json
def get_text(url):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'x-requested-with':'XMLHttpRequest'
            }
    r=requests.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    if r.status_code==200:
        return json.loads(r.text)
    else:
        print('get_text has somethings wrong!')

def cre_file():
        if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟'):
            os.mkdir(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟')
        if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟\英雄联盟全明星.txt'):
            f=open(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟\英雄联盟全明星.txt','w')
            f.close()
            
            
def opr_text(text):
    format1='序号：{:<3d}\t 游戏类型：{}\t 游戏时间：{}\t 游戏队伍：{}\t 获胜队伍：{}'
    t=len(text['msg'])
    if text:
        cre_file()
        with open(r'C:\Users\Administrator\Desktop\python爬虫小列子\英雄联盟\英雄联盟.txt','w+',encoding='utf-8') as f:
            for order,item in enumerate(text['msg']):
              try:
                a=[]
                a.append(order+1)
                a.append(item['GameTypeName'])
                a.append(item['MatchDate'])
                a.append(item['bMatchName'])
                p=2 if int(item['MatchWin'])>=2 else 1               
                a.append(item['bMatchName'].split('vs')[0].strip() if p==1 else item['bMatchName'].split('vs')[-1].strip())
                f.write(format1.format(*a))
                f.write('\n')
                if order%10==0:
                    print('{}% has done!'.format((order+1)/t*100))
                if order==t-1:
                    print('100% has done!')
              except:
                 print('opr_text has wrong!')
              
            
                 
def main():
    url='https://lpl.qq.com/web201612/data/LOL_MATCH2_MATCH_HOMEPAGE_BMATCH_LIST.js'
    text=get_text(url)
    opr_text(text)

main()
    
            