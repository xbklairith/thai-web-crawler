# -*- coding: utf-8 -*-
import scrapy

from news_scrap.items import NewsScrapItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request


class ThairahSpider(scrapy.Spider):
    name = 'thairath'
    allowed_domains = ['www.thairath.co.th']
    start_urls = ['http://www.thairath.co.th/content/100000']

    def start_requests(self):
        for i in range(100000,950000):
            yield Request('http://www.thairath.co.th/content/%d' % i,
                          callback=self.parse)


    def parse(self, response):
        item = NewsScrapItem()
        item[u'news_title'] = response.xpath(u'//h1/text()').extract_first()
        item["news_link"] = response.url
        item["news_article"] = response.xpath("//article//p").extract_first()
        return item

