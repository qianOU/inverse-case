# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from pyquery import PyQuery as pq
from dangdang.items import DangdangItem
from scrapy import signals

class DandanSpider(scrapy.Spider):
    name = 'dandan'
    start_url = ['http://book.dangdang.com/']
    
    def parse(self, response):
        print(response)
        for i in response.css('a#name::attr(href)'):
        	self.logger.warn(i.extract())


