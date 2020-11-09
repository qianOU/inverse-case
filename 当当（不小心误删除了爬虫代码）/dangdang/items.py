# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    pre_price=scrapy.Field()
    now_price=scrapy.Field()
    book_store=scrapy.Field()
    public=scrapy.Field()
    time=scrapy.Field()
    author=scrapy.Field()
    comment=scrapy.Field()
    comment_link=scrapy.Field()
    book_link=scrapy.Field()
    discount=scrapy.Field()
    information=scrapy.Field()
    pass
    
