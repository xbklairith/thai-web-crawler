# -*- coding: utf-8 -*-
import scrapy
from news_scrap.items import NewsScrapItem
from scrapy.linkextractors import LinkExtractor
import urlparse
from scrapy.spiders import CrawlSpider, Rule

class LiekrSpider(CrawlSpider):
    name = 'liekr'
    allowed_domains = ['www.liekr.com']
    start_urls = ['http://www.liekr.com/']

    rules = [
        Rule(LinkExtractor(allow=()),follow=True,callback="parse_links")
    ]

    def parse_links(self, response):
        all_page_links = response.xpath('//a/@href').extract()
        for link in all_page_links:
            print("relative link procesed:" + link)
            link = urlparse.urljoin(response.url, link)
            request = scrapy.Request(link,
                                     callback=self.parse_data)
            yield request

    def parse_data(self, response):
        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
        item["news_link"]    = response.url
        item["news_article"] = ''.join(response.xpath(u'//div[@class="postmain"]//p').extract()).strip()
        yield item