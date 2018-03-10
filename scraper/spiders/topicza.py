# -*- coding: utf-8 -*-
import scrapy
from news_scrap.items import NewsScrapItem
from scrapy.linkextractors import LinkExtractor
import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

class TopiczaSpider(scrapy.Spider):
    name = 'topicza'
    allowed_domains = ['www.topicza.com','topicza.com']
    start_urls = ['http://www.topicza.com/']


    def start_requests(self):
        for i in range(0,50000):
            yield Request('http://www.topicza.com/news%d.html' % i,
                        callback=self.parse)
    # rules = [
    #     Rule(LinkExtractor(allow=()),follow=True,callback="parse_links")
    # ]

    # def parse_links(self, response):
    #     all_page_links = response.xpath('//a/@href').extract()
    #     for link in all_page_links:
    #         print("relative link procesed:" + link)
    #         link = urlparse.urljoin(response.url, link)
    #         request = scrapy.Request(link,
    #                                  callback=self.parse_data)
    #         yield request
    
    # def parse_data(self, response):
    #     item = NewsScrapItem()

    #     item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
    #     item["news_link"]    = response.url
    #     # no need article
    #     # item["news_article"] = ''.join(response.xpath(u'//div[@class="postmain"]//p').extract()).strip()
    #     yield item

    def parse(self, response):
        item = NewsScrapItem()
        

        # for link in response.xpath('//a/@href').extract():
        #     if not link.lower().endswith(('.png', '.jpg', '.jpeg','.gif')):
        #         link = urlparse.urljoin(response.url, link)
        #         yield scrapy.Request(link, callback=self.parse)

        
        item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
        item["news_link"]    = response.url
        # no need article
        # item["news_article"] = ''.join(response.xpath(u'//div[@class="postmain"]//p').extract()).strip()
        if item[u'news_title']:
            yield  item

