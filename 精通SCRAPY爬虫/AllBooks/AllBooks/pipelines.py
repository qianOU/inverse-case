# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class AllbooksPipeline(object):
    mapping = {
		'One': 1,
		'Two': 2,
		'Three': 3,
		'Four': 4,
		'Five': 5,
	}

    def process_item(self, item, spider):
    	rating = item.get('review_rating')
    	if rating:
    		item['review_rating'] = self.mapping[rating]
    	return item

class DropPipeline:
	def __init__(self):
		self.set = set()

	def process_item(self, item, spider):
		if item['name'] in self.set:
			raise DropItem('书本已经存在')
		self.set.add(item['name'])
		return item