# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from ..items import BookItem
from scrapy import Request
import logging

class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    # allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for data in  response.css('li.col-xs-6'):
        	item = BookItem()
        	item['name'] = data.css('a[href]::attr(title)').extract_first()
        	item['dollar'] = data.css('p.price_color::text').extract_first()
        	yield item
        le = LinkExtractor(restrict_css="li.next>a")
        links = le.extract_links(response)
        for link in links:
        	logging.warning(link.url)
        	yield Request(link.url, callback = self.parse)
