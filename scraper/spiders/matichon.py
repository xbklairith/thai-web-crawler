# -*- coding: utf-8 -*-
import urlparse
import scrapy
from news_scrap.items import NewsScrapItem
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule
import re

# pylint: disable=bad-whitespace
# pylint: disable=no-member

class MatichonSpider(CrawlSpider):
    name = 'matichon'
    allowed_domains = ['www.matichon.co.th']
    start_urls = ['https://www.matichon.co.th/home']


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

    def parse(self, response):
        # img = ['.jpg','.png','.gif']
        if re.search(r"\/\d+", response.url):
            item = NewsScrapItem()
            item[u'news_title']  = response.xpath(u'//head/meta[@property="og:title"]/@content').extract_first()
            item["news_link"]    = response.url
            item["news_article"] = ''.join(response.xpath(u'//div[@class="td-post-content"]')
                                           .extract()).strip()
            yield item
        for link in response.xpath('//a/@href').extract():
            if not link.lower().endswith(('.png', '.jpg', '.jpeg','.gif')):
                link = urlparse.urljoin(response.url, link)
                yield scrapy.Request(link, callback=self.parse)

