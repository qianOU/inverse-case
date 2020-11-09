# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from ..items import AllbooksItem

class AllBooksSpider(scrapy.Spider):
    name = "all_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_css='article')
        if le:
        	for link in le.extract_links(response):
        		yield scrapy.Request(link.url, callback=self.parse_page)
        le = LinkExtractor(restrict_css='li.next')
        links = le.extract_links(response)
        if links:
        	next_url= links[0].url
        	yield scrapy.Request(next_url, callback=self.parse)


    def parse_page(self, response):
    	item = AllbooksItem()
    	item['name'] = response.css('div.col-sm-6>h1::text').extract_first()
    	item['price'] =  response.css('div.col-sm-6>p::text').extract_first()
    	item['upc'] = response.css('table.table tr:first-child td::text').extract_first()
    	item['review_rating'] = response.css('p.star-rating::attr(class)').re_first(r'star-rating\s([a-zA-Z]+)')
    	item['review_num'] =    	item['stock'] = response.css('table.table tr:last-child td::text').extract_first()
    	item['stock'] = response.css('table.table tr:nth-last-child(2) td::text').re_first(r'In stock \((\d+) available')
    	yield item