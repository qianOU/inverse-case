# -*- coding: utf-8 -*-
import scrapy,json,pyquery
from urllib.parse import urlencode
from scrapy import Request
from images360.items import ImagesItem
from urllib.parse import unquote

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']
    
    def start_requests(self):
        data={'ch':'photography','listtype':'new','temp':1}
        base_url='https://image.so.com/zj?'
        for page in range(5,self.settings.get('MAX_PAGE')+1):
            data={'ch':'photography','listtype':'new','temp':1}
            data['sn']=page*30
            params=urlencode(data)
            url=base_url+params
            yield  Request(url,self.parse)
            del data
        
        #    self.logger.debug(t.headers)


    def parse(self, response):
        result=json.loads(response.text)
        for image in result.get('list'):
            item=ImagesItem()
            item['id']=image.get('id','None')
            item['url']=unquote(image.get('qhimg_thumb_url','None'))
            item['title']=unquote(image.get('group_title','None'))
            item['tags']=image.get('tag','None')
            yield item
            self.logger.debug(dict(item))
            
            
