# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from news_scrap.items import NewsScrapItem
from scrapy.linkextractors import LinkExtractor
import urlparse


class MeekhaoSpider(scrapy.Spider):
    name = 'meekhao'
    allowed_domains = ['www.meekhao.com']
    start_urls = ['http://www.meekhao.com/']

    # rules = (
    #     Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    # )
    

    # def parse_item(self, response):
    #    item = NewsScrapItem()
    #    item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
    #    item["news_link"]    = response.url
    # #    item["news_article"] = ''.join(response.xpath('//div[@class="mw-parser-output"]//p').extract()).strip()
    #    if item["news_title"]:
    #        return item

    def parse(self, response):
    # img = ['.jpg','.png','.gif']
        for link in response.xpath('//a/@href').extract():
            if not link.lower().endswith(('.png', '.jpg', '.jpeg','.gif')):
                link = urlparse.urljoin(response.url, link)
                yield scrapy.Request(link, callback=self.parse)

        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
        item["news_link"]    = response.url
        # item["news_article"] = ''.join(response.xpath(u'//div[@class="td-post-content"]')
        #                             .extract()).strip()
        if item['news_title']:
            yield item
