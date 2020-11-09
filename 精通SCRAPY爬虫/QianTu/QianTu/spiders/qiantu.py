# -*- coding: utf-8 -*-
import scrapy
from ..items import QiantuItem
from  scrapy.http import Request,FormRequest
import logging
from QianTu.settings import USERNAME, PASSWORD
from scrapy.http.cookies import CookieJar

class QiantuSpider(scrapy.Spider):
    cookiejar = CookieJar()
    name = "qiantu"
    allowed_domains = ["search.51job.com"]
    base_url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%2B,2,{:d}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    # start_urls = []
    flag = False
    username = USERNAME
    pwd = PASSWORD
    # def __init__(self, username, pwd):
    # 	self.username = username
    # 	self.pwd = pwd


    # @classmethod
    # def from_crawler(cls, clawer):
    # 	username = clawer.settings.get('USERNAME')
    # 	pwd = clawer.settings.get('PASSWORD')
    # 	logging.warning(username+'|||'+pwd)
    # 	return cls(username, pwd)

    def login(self):
    	formdata = {'lang':'c','action':'save','from_domain':'i','loginname':self.username,
    	'password':self.pwd,'verifycode':'','isread':'on'}
    	login_url = 'https://login.51job.com/login.php'
    	self.logger.warning(str(formdata))
    	yield FormRequest(login_url,formdata=formdata,callback=self.verify,meta={'cookiejar':1})

    def verify(self, response):
    	if '洪' in  response.text:
    		self.logger.warning('登录成功！')
    		self.flag = True
    	else:
    		self.logger.error('登录失败！')
    	yield Request(self.base_url.format(1),callback=self.get_nums,meta={'cookiejar':1})


    def start_requests(self):
        yield from self.login()
        # yield Request(self.base_url.format(1),callback=self.get_nums)

    def get_nums(self, response):
    	# self.page_nums = int(response.xpath('*').re_first('共(\d+)页'))
    	self.cookiejar.extract_cookies(response, response.request)
    	self.logger.error(list(self.cookiejar))
    	self.page_nums = 1
    	for i in range(1, self.page_nums+1):
    		yield Request(self.base_url.format(i),meta={'cookiejar':response.meta['cookiejar']})

    def parse(self, response):
        for one in  response.xpath('//div[@class="el"]'):
            if one.re('t2'):
            	item = QiantuItem()
            	item['company'] = one.css('span.t2 a::attr(title)').extract_first()
            	item['job'] = one.xpath('./p/span/a[@target="_blank"]/@title').extract_first()
            	item['salary'] = one.css('span.t4::text').extract_first()
            	item['work_place'] = one.css('span.t3::text').extract_first()
            	item['output_date'] = one.css('span.t5::text').extract_first()
            	item['link'] = one.xpath('./p/span/a[@target="_blank"]/@href').extract_first()
            	yield item
