# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os
logger=logging.getLogger('ImagePipeline')
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
#ImagesPipeline 调用函数顺序如下：1.get_media_requests,2.file_pah 3.item_completed 
class ImagePipeline(ImagesPipeline):
    IMAGE_SOURCE='./iamges'
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            logger.debug('下载图片失败')
            raise DropItem('Image Downloaded Failed')
        logger.debug('下载图片成功')
        #重命名文件
        os.rename(self.IMAGE_SOURCE + "/" + image_paths, self.IMAGE_SOURCE + "/" + item["name"] + ".jpg")     
        return item
    
    def get_media_requests(self, item, info):
        yield Request(item['href'])
        
"""        
class ImagePipeline(ImagesPipeline):
    def file_path(self,request,response=None,info=None):
        file_name=request.url('/')[-1]
        return file_name
    def item_completed(self,results,item,info):
        images_path=[x for ok,x in results if ok]
        if not images_path:
            logger.debug('下载失败')
            raise DropItem
        logger.debug('下载成功')
        return item
    def get_media_requests(self,item,info):
        yield Request(item['href'])
"""