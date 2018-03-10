# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news_scrap.items import ArticleScrapItem


class ThaiwikiSpider(CrawlSpider):
    name = 'thaiwiki'
    allowed_domains = ['kanchanapisek.or.th']
    start_urls = ['http://kanchanapisek.or.th/kp6/sub/book/']

    rules = (
        Rule(LinkExtractor(allow=r'book/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ArticleScrapItem()
        item[u'title']  = ''.join(response.xpath(u'//p//a/text()').extract()).strip()
        item["link"]    = response.url
        item["article"] = ''.join(response.xpath(u'//td/text()')
                                    .extract()).strip()
        
        if item['title'] and 'infodetail' in response.url :
            yield item
