# -*- coding: utf-8 -*-

import urlparse
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from news_scrap.items import NewsScrapItem


# pylint: disable=bad-whitespace
# pylint: disable=no-member

class KhaosodSpider(scrapy.Spider):
    name = 'khaosod'
    allowed_domains = ['www.khaosod.co.th']
    start_urls = [
                  'https://www.khaosod.co.th/home',
                #   'https://www.khaosod.co.th/hot-topics',
                #   'https://www.khaosod.co.th/special-stories/page/190',
                #   'https://www.khaosod.co.th/around-thailand/news_366925'
                ]

    # rules = [
    #     # Rule(LinkExtractor(allow=()), follow=True),
    #     Rule(LxmlLinkExtractor(allow=()), callback="parse_links", follow=True)
    # ]

    # def parse_links(self, response):
    #     all_page_links = response.xpath('//a/@href').extract()
    #     for link in all_page_links:
    #         # 
    #         if('https' not in link):
    #             link = urlparse.urljoin(response.url, link)
            
    #         print("link procesed:" + link)
    #         request = scrapy.Request(link,
    #                                  callback=self.parse_data)
    #         yield request

    # def parse_data(self, response):
    #     # if re.search("news_\d*",response.url):
    #     item = NewsScrapItem()
    #     # item[u'news_title']  = response.xpath(u'//h1/text()').extract_first()
    #     # item["news_link"]    = response.url
    #     # item["news_article"] = ''.join(response.xpath(u'//div[@class="td-post-content"]')
    #     #                             .extract()).strip()
    #     # yield item
    #     yield item

    def parse(self, response):
        img = ['.jpg','.png','.gif']
        if re.search("news_\d*",response.url):
            item = NewsScrapItem()
            item[u'news_title']  = response.xpath(u'//h1/text()').extract_first()
            item["news_link"]    = response.url
            item["news_article"] = ''.join(response.xpath(u'//div[@class="td-post-content"]')
                                        .extract()).strip()
            yield item
        # if re.search("news_\d*",response.url):
        for link in response.xpath('//a/@href').extract():
            if not link.lower().endswith(('.png', '.jpg', '.jpeg','.gif')):
                link = urlparse.urljoin(response.url, link)
                yield scrapy.Request(link, callback=self.parse)
