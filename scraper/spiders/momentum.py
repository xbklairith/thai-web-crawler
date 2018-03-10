# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news_scrap.items import ArticleScrapItem


class MomentumSpider(CrawlSpider):
    name = 'momentum'
    allowed_domains = ['themomentum.co']
    start_urls = ['http://themomentum.co/site/']

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ArticleScrapItem()
        item[u'title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
        item["link"]    = response.url
        item["article"] = '\n'.join(response.xpath(u'//div[contains(@class,"entry-content")]//p//text()')
                                    .extract()).strip()
        if item['title']:
            yield item
