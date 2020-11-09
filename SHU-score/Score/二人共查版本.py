# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:06:22 2019

@author: Administrator
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:10:25 2019

@author: Administrator
"""
import itchat
from 成绩查询 import check_mark
import time
from threading import Thread


class Send(object):
    def __init__(self,name,filename):
        self.user = name
        self.filename = filename
        itchat.auto_login(hotReload = True)
        
    def send_info(self):
        #itchat.auto_login(hotReload = True)
        user = itchat.search_friends(name = self.user)[0]
        itchat.send('成绩发布啦！,请查看下面的文件：',toUserName = user['UserName'])
        itchat.send_file(fileDir = self.filename,toUserName = user['UserName'])
        
    def keep_live(self):
        pass
        
        
#def main(name):
#    #选择微信用户
#    with open('Score.txt','w',encoding ='utf-8') as f:
#        f.close()
#    target = Send(name)
#    print(target)
#    username,pwd =input('输入用户名,密码（以逗号分隔）=').split(',')
#    option = input("""格式如下：年份+学期  学期=1：秋季学期   学期=2：冬季学期   学期=3：春季学期   学期=5：夏季学期\n例子：20182 表示 2018年冬季学期\n请输入查询的学期：""")
#    go = check_mark(username,pwd,option)
#    print('正在查询！请稍后...')
#    while True:
#        try:
#             text = go.login()
#             if int(option[-1]) not in [1,2,3,5]:
#                 print('请输入正确的学期代号！！！')
#             elif '本学期成绩未发布！' in text:
#                 print('成绩未发布！持续更新中...')
#                 time.sleep(8)
#                 continue
##                 print('查询本学期成绩中...')
##                 time.sleep(1)
#             else:
#                 go.parse(text)
#                 break
#        except Exception:
#            print('成绩未发布！持续更新中...')
#            time.sleep(8)
#            continue
#            
#    target.send_info()
#    return 1

#def Main(name):
#    while True:
#         if main(name):
#             print('successful!')
#             break
         
            
class XianCeng():
    def __init__(self,name,filename):
        self.user = name
        self.filename = filename
        
    def main(self,username,pwd,option = 20171):
        #选择微信用户
        #with open(self.filename,'w',encoding ='utf-8') as f:
        #    f.close()
        target = Send(self.user,self.filename)
        print(target)
        #username,pwd =input('输入用户名,密码（以逗号分隔）=').split(',')
        #option = input("""格式如下：年份+学期  学期=1：秋季学期   学期=2：冬季学期   学期=3：春季学期   学期=5：夏季学期\n例子：20182 表示 2018年冬季学期\n请输入查询的学期：""")
        #go = check_mark(username,pwd,option,self.filename)
        print('正在查询！请稍后...')
        while True:
            try:
                 go = check_mark(username,pwd,option,self.filename)
                 text = go.login()
                 if int(option[-1]) not in [1,2,3,5]:
                     print('请输入正确的学期代号！！！')
                 elif '本学期成绩未发布！' in text:
                     print('成绩未发布！')
                     #time.sleep(2)
                     continue
                #                 print('查询本学期成绩中...')
                #                 time.sleep(1)
                 elif '课程编号' in text:
                     go.parse(text)
                     break
            except Exception:
                    print('成绩未发布！持续更新中...')
                    #time.sleep(2)
                    continue
    
        target.send_info()
        return 1
    
    def run(self,username,pwd,option):
        while True:
         if self.main(username,pwd,option):
             print('successful!')
             break
        
        
        
if __name__ == '__main__':
     name = ['洪吼吼']
     t=XianCeng(name[0],'Score_2.txt')
     t.run('*****')
     #with open('Score.txt','w',encoding ='utf-8') as f:
     #     f.close()
     #t=XianCeng(name[1],'Score_1.txt')
     #t.run('17170036','Lc151319','20182')
     #time.sleep(60)
     #print('别人的学号！')

