# -*- coding: utf-8 -*-
import scrapy
from news_scrap.items import NewsScrapItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class DailySpider(scrapy.Spider):
    name = 'daily'
    allowed_domains = ['www.dailynews.co.th']
    start_urls = ['https://www.dailynews.co.th/']
    def start_requests(self):
        for i in range(330000, 575000):
            yield Request('https://www.dailynews.co.th/article/%d' % i,
                          callback=self.parse)

    def parse(self, response):
        item = NewsScrapItem()
        item[u'news_title'] = response.xpath(u'//h1[@class="title"]/text()').extract_first()
        item["news_link"] = response.url
        item["news_article"] = response.xpath(u'//section[@class="article-detail"]//div[contains(@class, "content-all")]').extract_first()
        return item
