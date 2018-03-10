# -*- coding: utf-8 -*-
import scrapy
from news_scrap.items import NewsScrapItem
from scrapy.linkextractors import LinkExtractor
import urlparse
from scrapy.spiders import CrawlSpider, Rule

# pylint: disable=bad-whitespace
# pylint: disable=no-member



class ManagerSpider(CrawlSpider):
    name = 'manager'
    allowed_domains = ['manager.co.th','www.manager.co.th']
    # start_urls = ['http://www.manager.co.th/home/']
    start_urls = ['http://www.manager.co.th/Crime/ViewNews.aspx?NewsID=9600000000009',
                  'http://www.manager.co.th/Crime/ViewNews.aspx?NewsID=9590000000009',
                  'http://www.manager.co.th/Crime/ViewNews.aspx?NewsID=9580000000009',
                  'http://www.manager.co.th/Crime/ViewNews.aspx?NewsID=9570000000009',
                  'http://www.manager.co.th/Crime/ViewNews.aspx?NewsID=9560000000009',
                  'http://www.manager.co.th/Crime/ViewNews.aspx?NewsID=9550000000010']

    rules = [
        Rule(LinkExtractor(allow=()),follow=True,callback="parse_links")
    ]

    def parse_links(self, response):
        all_page_links = response.xpath('//a/@href').extract()
        for relative_link in all_page_links:
            print("relative link procesed:" + relative_link)

            absolute_link = urlparse.urljoin('http://'
                                             +self.allowed_domains[0], relative_link.strip())
            request = scrapy.Request(absolute_link,
                                     callback=self.parse_data)
            yield request

    def filter_links(self, links):
        for link in links:
            if 'ViewNews.aspx' not in link.url:
                print 'filter_links' + link.url
            return links

    def parse_data(self, response):
        item = NewsScrapItem()
        item[u'news_title']  = response.xpath(u'//h1/text()').extract_first()
        item["news_link"]    = response.url
        item["news_article"] = ''.join(response.xpath('//*[@id = "innity-in-post"]//table//td[@valign = "baseline"]/text()').extract()).strip()
        if 'ViewNews.aspx' in response.url:
            return item

