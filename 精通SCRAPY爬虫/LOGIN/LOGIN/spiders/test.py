import requests
import browsercookie
cookies = browsercookie.firefox()

headers = {
    'Host': 'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'http://bd.118wa.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = (
    ('tn', '78000241_2_hao_pg'),
)

response = requests.get('https://www.baidu.com/', headers=headers, params=params, cookies=cookies)
if '不像星' in response.text:
    print('successful!!!')
else:
    print('fail!')
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.baidu.com/?tn=78000241_2_hao_pg', headers=headers, cookies=cookies)