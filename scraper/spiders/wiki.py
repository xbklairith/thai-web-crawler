# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news_scrap.items import NewsScrapItem


class WikiSpider(CrawlSpider):
    name = 'wiki'
    allowed_domains = ['th.wikipedia.org']
    start_urls = ['https://th.wikipedia.org/']

    rules = (
        Rule(LinkExtractor(allow=r'wiki/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//h1/text()').extract_first()
        item["news_link"]    = response.url
        item["news_article"] = ''.join(response.xpath('//div[@class="mw-parser-output"]//p').extract()).strip()
        if item["news_article"]:
            return item
        
        