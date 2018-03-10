# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from news_scrap.items import ArticleScrapItem


class BlognoneSpider(scrapy.Spider):
    name = 'blognone'
    allowed_domains = ['blognone.com']
    start_urls = ['https://blognone.com/']

  
    def start_requests(self):
        for i in range(0,100000):
            yield Request('https://blognone.com/node/%d' % i,
                            callback=self.parse)

    def parse(self, response):
        item = ArticleScrapItem()
        item[u'title']  = ''.join(response.xpath(u'//div[@class="content"]//h2//a/text()').extract()).strip()
        item["link"]    = response.url
        item["article"] = ''.join(response.xpath(u'//div[@class="node-content"]')
                                    .extract()).strip()
        return item
