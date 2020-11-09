# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class QiantuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = Field()
    job = Field()
    work_place = Field()
    salary = Field()
    output_date = Field()
    link = Field()
