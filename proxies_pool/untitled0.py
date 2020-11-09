# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:34:09 2019

@author: Administrator
"""
import requests
import re
class check_mark(object):
    login_url = 'https://sso.shu.edu.cn/idp/Authn/UserPassword'
    def __init__(self,username,password):
        self.username = username 
        self.password = password
        self.session = requests.Session()
        self.headers = {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                 }
    def login(self):
#        global c
        data ={
            "j_username": self.username,
            "j_password": self.password
              }
        data1={
                'SAMLRequest':'',
                 'RelayState': 'https://oauth.shu.edu.cn//oauth/authorize?client_id=yRQLJfUsx326fSeKNUCtooKw&response_type=code&state=&redirect_uri=http%3A%2F%2Fcj.shu.edu.cn%2Fpassport%2Freturn',
}       
        
        str1='https://sso.shu.edu.cn/idp/profile/SAML2/POST/SSO'
        w=self.session.get('https://oauth.shu.edu.cn/oauth/authorize?response_type=code&client_id=yRQLJfUsx326fSeKNUCtooKw&redirect_uri=http://cj.shu.edu.cn/passport/return&state=',allow_redirects = False)
        c=w.text
        value = re.search(r'value=\"(.*?)\".*?value=\"(.*?)\"',w.text,re.S)
        #print(value.group(1))
        #print(value.group(2))
        data1['SAMLRequest'] = str(value.group(1))
        data1['RelayState'] = str(value.group(2))
        print('*'*40)
        print(data1)
        print('*'*40)
        response = self.session.post(str1,headers = self.headers,data=data1,allow_redirects=False)
        if response.status_code == 302:
            cookies = requests.utils.dict_from_cookiejar(response.cookies)
            print(response.url)
            print('-'*40)
            print(cookies)
            print('-'*30)
#        print(self.session.cookies)
#        self.headers['Host']='sso.shu.edu.cn'
#        self.headers['Origin']='https://sso.shu.edu.cn'
#        self.headers['Referer']='https://sso.shu.edu.cn/idp/Authn/UserPassword'
#        self.headers['Upgrade-Insecure-Requests']='1'
#        self.headers['Content-Type']='application/x-www-form-urlencoded'
        #此处不太懂为什么一定要访问下面这个网页
        response = self.session.get('https://sso.shu.edu.cn/idp/AuthnEngine',headers=self.headers)
        print(response.status_code,response.url)
        response = self.session.post('https://sso.shu.edu.cn:443/idp/Authn/UserPassword',data=data,headers=self.headers,allow_redirects=False)
        #print(response.url)
        if response.status_code == 302: 
            print('='*35)
            print(response.url)
            print('='*35)
            cookies = requests.utils.dict_from_cookiejar(response.cookies)
            print(cookies)
            print('='*35)
        response = self.session.get('https://sso.shu.edu.cn/idp/profile/SAML2/POST/SSO',headers=self.headers)
        response.encoding = response.apparent_encoding
        c=response.text
        text=re.search(r'name=\"RelayState\".*?=\"(.*?)\".*?name=\"SAMLResponse\".*?=\"(.*?)\"',c,re.S)
        str1 = text.group(1)
        str2 = text.group(2)
        data1={
                'RelayState':'',
                 'SAMLResponse':"",
              }
        data1['RelayState'] = str1.replace('&#x3a;',':').replace('&#x2f;','/').replace('&#x25;','%').replace('&#x3f;','?').replace('&#x3d;','=').replace('&amp;','&')
        data1['SAMLResponse'] = str2
        print('#'*40)
        #print(str1)
        print('\n')
        #print(data1['RelayState'])#,'\n',str2)
        print('#'*40)
        response = self.session.post('http://oauth.shu.edu.cn/oauth/Shibboleth.sso/SAML2/POST',headers=self.headers,data = data1,allow_redirects=False)
        print(response.cookies)
        print('%'*40)
        response = self.session.get(data1['RelayState'],headers=self.headers,allow_redirects=False)
        cookies=response.cookies
        url = response.headers['Location']
        print(response.headers['Location'])
        print('-'*50)
        response = self.session.get(url,headers=self.headers,allow_redirects=False)
        #response = self.session.get('http://cj.shu.edu.cn/passport/return?code=807d3e023eb65306e25fb44b5ecb732d',headers=self.headers,allow_redirects=False)
        cookies=response.cookies
        #response = requests.get('http://cj.shu.edu.cn/passport/return?code=807d3e023eb65306e25fb44b5ecb732d',headers=self.headers,allow_redirects=False,cookies=cookies)
        print(response.cookies)
        response = self.session.get(url,headers=self.headers,allow_redirects=True)
        print(response.text)
        #res=self.session.get('http://cj.shu.edu.cn/Home/StudentIndex',headers=self.headers)
        #print(res.text)
        成绩查询_url = 'http://cj.shu.edu.cn/StudentPortal/CtrlScoreQuery'
        data = {
                'academicTermID': 20175
                }
        response=self.session.get(成绩查询_url,headers=self.headers,data = data)
        print('+'*40)
        print(response.text)
c=""            
def main():
    #username,pwd =input('username,pwd=').split(',')
    username,pwd ="17170034","HHj1998"
    go = check_mark(username,pwd)
    go.login()

if __name__ == '__main__':
    main()
        
    