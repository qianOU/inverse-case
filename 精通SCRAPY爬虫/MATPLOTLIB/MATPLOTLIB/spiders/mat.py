# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from ..items import MatplotlibItem

class MatSpider(scrapy.Spider):
    name = "mat"
    allowed_domains = ["matplotlib.org"]
    start_urls = ['https://matplotlib.org/gallery/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.sphx-glr-thumbcontainer p.caption'
        	        ,deny='/index.html$')
        for link in le.extract_links(response):
        	yield scrapy.Request(link.url, callback=self.page_parser)

    def page_parser(self, response):
    	href = response.css('div>a.reference.download.internal::attr(href)').extract_first()
    	url = response.urljoin(href)
    	item = MatplotlibItem()
    	item['file_urls'] = [url]
    	yield item

