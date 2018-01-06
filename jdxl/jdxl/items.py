# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdxlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #姓名
    url = scrapy.Field() #链接
    info = scrapy.Field() #简介
    zx_type = scrapy.Field() #咨询类型
    location = scrapy.Field() #地点
    price = scrapy.Field() #价格
