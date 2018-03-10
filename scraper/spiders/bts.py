# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news_scrap.items import NewsScrapItem


class BtsSpider(CrawlSpider):
    name = 'bts'
    allowed_domains = ['btsstation.com']
    start_urls = ['http://btsstation.com/']

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//h1/text()').extract_first()
        item["news_link"]    = response.url
        # item["news_article"] = ''.join(response.xpath(u'//div[@class="td-post-content"]')
        #                             .extract()).strip()
        if item['news_title']:
            yield item
