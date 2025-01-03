# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class NewsScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_title = Field()
    news_link = Field()
    news_article = Field()

class ArticleScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    article = Field()
