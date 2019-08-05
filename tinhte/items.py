# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class AuthorItem(scrapy.Item):
    name = Field()
    phone = Field()
class TinhteItem(scrapy.Item):
    title = Field()
    img = Field()
    excerpt = Field()
    content = Field()
    author = Field()

