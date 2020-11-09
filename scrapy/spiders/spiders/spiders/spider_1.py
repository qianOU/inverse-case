# -*- coding: utf-8 -*-
import scrapy
from spiders.items import spider1Item

class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    def write(self,a):
        with open('a.txt','a+') as f:
            for i in a:
               f.write('{}:{}{}'.format(i,a[i],' '*6))
            f.write('\n')
            
    def parse(self, response):
        quotes=response.css('.quote')
        self.logger.debug(quotes)
        for quote in quotes:
            item=spider1Item()
            item['text']=quote.css('.text::text').extract_first()
            item['author']=quote.css('.author::text').extract_first()
            item['tags']=quote.css('.tags .tag::text').extract()
            yield item
            self.write(item)
        next=response.css('.pager .next a::attr(href)').extract_first()
        url=self.start_urls[0]+next
        yield scrapy.Request(url=url,callback=self.parse)
        
            
