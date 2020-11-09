# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote,unquote
from pretty_girl.items import PrettyGirlItem
import json

class GirlsSpider(scrapy.Spider):
    name = 'girls'
    allowed_domains = ['pic.sogou.com']
    start_urls = ['https://pic.sogou.com/']
    list1=['车模','萝莉','清纯','唯美','女神','时尚','短发','妹纸','小清新','自拍','可爱']
    start_urls=["""https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%s&tag=%s&start=%d&len=15"""%(quote('美女'),quote(i),j) for i in list1
                for j in range(0,50,15)]
    def parse(self, response):
        w=json.loads(response.text)
        for img in w['all_items']:
            item=PrettyGirlItem()
            item['href']=img.get('thumbUrl',None)
            item['name']=img.get('title',None)
            item['tag']=[unquote(i) for i in img.get('tags',None)]
            yield item

        
        
