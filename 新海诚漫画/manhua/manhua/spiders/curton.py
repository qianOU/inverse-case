# -*- coding: utf-8 -*-
import scrapy
from manhua.items import ManhuaItem
from pyquery import PyQuery as pq
class CurtonSpider(scrapy.Spider):
    name = 'curton'
    allowed_domains = ['manhua.dmzj.com']
    start_urls = ['https://manhua.dmzj.com/tags/xinhaic.shtml']
    
    
    def parse(self, response):
        URL='https://manhua.dmzj.com'
        for i in range(1,5):
            w=response.css('div.pic:nth-child(%d) a::attr(href)'%i).extract_first()
            self.logger.warn(w)
            #w=response.xpath('//div[@class="pic"][%d]/a/img/@href'%i).extract_first()
            yield scrapy.Request(url=URL+w,callback=self.mai)
            self.logger.debug('ask to'+URL+w)
        """
         if scrapy.Request.url!='https://manhua.dmzj.com/tags/xinhaic.shtml':
            for i in response.css('div.cartoon_online_border ul li').items():
                text=ManhuaItem()
                text['name']=i.css('a::attr(title)').extract_first().split('。')[0]
                text['chapter']=i.css("a::text").extract_first()
                text['link']=[URL+i.css("a::attr(href)").extract_first()+'#@page='+str(t) for t in range(1,13)]
                for uri in text['link']:
                    yield scrapy.Request(url=uri,callback=self.dowload)
        """  
    def mai(self,response):
        URL='https://manhua.dmzj.com'
        for i in response.css('div.cartoon_online_border ul li').extract():
            text=ManhuaItem()
            i=pq(i)
            text['name']=i('a').attr('title')
            text['chapter']=i("a").text()
            text['link']=[URL+i("a").attr('href')+'#@page='+str(t) for t in range(1,13)]
            yield text
            
            
            for uri in text['link']:
                #self.logger.info('='*30+uri)
                yield scrapy.Request(url=uri,callback=self.download)
                    
    def download(self,response):
       self.logger.info('='*30+response.text)
       try: 
        text=ManhuaItem()
        text['name']=response.css('h1.hotrmtexth1 a::attr(title)').extract_first()
        text['chapter']=response.css('span.redhot1::text').extract_first()
        self.logger.info('*'*30+text['name']+'*'*10+text['chapter'])
        text['link']='https:'+(response.xpath('//*[@id="center_box"]/img/@src').extract_first())
        #text['link']='https:'+response.css('div[id="center_box"] img::attr(src)').extract_first()
        self.logger.warn('*'*30+text['link'])
        yield text
        #self.logger.info('*'*30+text['link'])
        self.logger.debug(str(text))
       except:
           pass
        #yield scrapy.Request(url=response.css('div#center_box img::@src').extract_first(),callback=self.picture)
        