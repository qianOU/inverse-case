# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
class DangdangPipeline(object):
    def __init__(self,uri,db,collection):
        self.uri=uri
        self.mongo_db=db
        self.Collection=collection
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.get('URI'),crawler.settings.get('DB'),crawler.settings.get('COLLECTION'))
    
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.uri)
        self.db=self.client[self.mongo_db]
        self.collection=self.db[self.Collection]
        
    def close_spider(self,spider):
        self.client.close()
        
    def process_item(self, item, spider):
        #with open(r'C:\Users\Administrator\Desktop\python爬虫小列子\dangdang\www.json','a',encoding='utf-8') as f:
        #   f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        self.collection.update({'title':item['title']},{'$set':item},True)
        #self.collection.insert_one(dict(item))
        return item
