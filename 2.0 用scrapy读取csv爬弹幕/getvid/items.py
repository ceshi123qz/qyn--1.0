# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetvidItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    upcount = scrapy.Field()
    opername = scrapy.Field()
    uservip_degree = scrapy.Field()


