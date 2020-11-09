# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
#import requests
class ManhuaPipeline(object):
    def mk_file(self,item):
        if item['name'] and item['chapter']:
            item['name']=item['name'][0:2]
            if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\新海诚漫画\manhua\{}'.format(item['name'])):
                os.mkdir(r'C:\Users\Administrator\Desktop\python爬虫小列子\新海诚漫画\manhua\{}'.format(item['name']))
            #os.chdir('C:\Users\Administrator\Desktop\python爬虫小列子\新海诚漫画\manhua/{}'.format(item['name']))
            if not os.path.exists(r'C:\Users\Administrator\Desktop\python爬虫小列子\新海诚漫画\manhua\{}\{}'.format(item['name'],item['chapter'])):
                os.mkdir(r'C:\Users\Administrator\Desktop\python爬虫小列子\新海诚漫画\manhua{}'.format(item['name']))
                
    def process_item(self, item, spider):
        self.mk_file(item)
        #response=requests.get(item['link'])
        #if response.status_code==200:
         #   w=response.content
         #else:
            #w=None
        with open(r'C:\Users\Administrator\Desktop\python爬虫小列子\新海诚漫画\manhua\{}'.format(item['chapter']),'w') as f:
            f.write(item['link'])
        return item
