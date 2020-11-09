# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:15:41 2019

@author: Administrator
"""
import os,re
from mitmproxy import ctx
pattern=re.compile(r'.*?ixigua\.(com|cn)',re.S)
def mk_file():
    if not os.path.exists('抖音视频'):
        os.mkdir('抖音视频')
def response(flow):
    ctx.log.info('*'*100)
    mk_file()
    if re.search(pattern,flow.request.url):
        ctx.log.error('='*100)
        name=flow.request.url.split('/')[-2]
        with open('./抖音视频/%s.mp4'%name,'wb') as f:
            f.write(flow.response.content)
        ctx.log.warn(name+'has done!')
        
        

