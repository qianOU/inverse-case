# -*- coding: utf-8 -*-
import scrapy
from ..items import SoImageaItem
import json

class ImagesSpider(scrapy.Spider):
    name = "images"
    BASE_URL = 'https://image.so.com/zjl?ch=art&sn=%s&listtype=new&temp=1'

    MAX_DOWNLOAD = 1000
    start_index = 0
    start_urls = [BASE_URL%0]

    def parse(self, response):
        item = SoImageaItem()
        infos = json.loads(response.text)
        item['image_urls'] = [info['qhimg_url'] for info in infos['list']]
        yield item
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD:
        	yield scrapy.Request(self.BASE_URL % self.start_index, callback=self.parse)

