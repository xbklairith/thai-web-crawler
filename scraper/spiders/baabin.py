# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news_scrap.items import NewsScrapItem


class BaabinSpider(CrawlSpider):
    name = 'baabin'
    allowed_domains = ['baabin.com']
    start_urls = ['https://baabin.com/']

    rules = (
        Rule(LinkExtractor(allow=(r'\d*')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

       #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
       #i['name'] = response.xpath('//div[@id="name"]').extract()
       #i['description'] = response.xpath('//div[@id="description"]').extract()

        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
        item["news_link"]    = response.url
        # item["news_article"] = ''.join(response.xpath(u'//div[@class="td-post-content"]')
        #                             .extract()).strip()
        if item['news_title']:
            yield item
