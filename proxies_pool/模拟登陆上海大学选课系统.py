# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:02:12 2019

@author: Administrator
"""
import requests,json
from pyquery import pyquery as pq
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'37',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'sso.shu.edu.cn',
'Origin':'https://sso.shu.edu.cn',
'Referer':'https://sso.shu.edu.cn/idp/Authn/UserPassword',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
data={
'j_username':17170034,
'j_password':'HHj1998'
}
session=requests.Session()
w=session.post('https://sso.shu.edu.cn/idp/Authn/UserPassword',data=data,headers=headers,timeout=6)
print(w.text)
#w=session.get('http://xk.autoisp.shu.edu.cn:8080/CourseSelectionStudent/FuzzyQuery',timeout=10)
data={
"TeachName":"王",
"PageSize":8,
"PageIndex":1,
"NotFull":"false",
"Campus":0,
"FunctionString":"InitPage"
}
#w=session.post('http://xk.autoisp.shu.edu.cn:8080/CourseSelectionStudent/CtrlViewQueryCourseCheck',data=data)
#print(w.text)
z=input('A=')