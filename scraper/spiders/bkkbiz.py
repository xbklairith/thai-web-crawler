# -*- coding: utf-8 -*-
import scrapy
from news_scrap.items import NewsScrapItem
from scrapy.linkextractors import LinkExtractor
import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request


class BkkbizSpider(scrapy.Spider):
    name = 'bkkbiz'
    allowed_domains = ['www.bangkokbiznews.com/']
    start_urls = ['http://www.bangkokbiznews.com//']

    def start_requests(self):
        for i in range(550000,760000):
            yield Request('http://www.bangkokbiznews.com/news/detail/%d' % i,
                          callback=self.parse)
    
    def parse(self, response):
        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
        item["news_link"]    = response.url
        # no need article
        item["news_article"] = ''.join(response.xpath(u'//div[@class="text_post_block"]//p').extract()).strip()
        if item[u'news_title']:
            yield  item

