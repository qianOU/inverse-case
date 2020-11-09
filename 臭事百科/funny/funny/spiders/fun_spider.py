# -*- coding: utf-8 -*-
import scrapy


class FunSpiderSpider(scrapy.Spider):
    name = 'fun_spider'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        pass
