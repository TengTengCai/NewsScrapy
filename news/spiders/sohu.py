# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from news.items import NewsItem


class SohuSpider(CrawlSpider):
    name = 'sohu'
    allowed_domains = ['www.sohu.com']
    start_urls = ['http://www.sohu.com/',
                  'http://news.sohu.com/',
                  'http://mil.sohu.com/',
                  'http://society.sohu.com',
                  'http://business.sohu.com',
                  'http://business.sohu.com/994',
                  'http://business.sohu.com/998',
                  'http://sports.sohu.com/',
                  'http://sports.sohu.com/2018/',
                  'http://sports.sohu.com/nba.shtml',
                  'http://yule.sohu.com/',
                  'http://auto.sohu.com/',
                  'http://00.auto.sohu.com/',
                  'http://fashion.sohu.com/',
                  'http://travel.sohu.com/',
                  'http://baobao.sohu.com/',
                  'http://it.sohu.com/',
                  'http://learning.sohu.com/',
                  'http://health.sohu.com/',
                  'http://chihe.sohu.com/',
                  'http://cul.sohu.com/',
                  'http://history.sohu.com/',
                  'http://astro.sohu.com/',
                  'http://acg.sohu.com/',
                  'http://game.sohu.com',
                  'http://gov.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'a/\d+_\d+\?*.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = NewsItem()
        print(response)
        i['title'] = response.xpath('//div[@class="text-title"]/h1/text()').extract_first()
        i['type'] = response.xpath('//div[@class="location area"]/a/text()').extract_first()
        i['publish_time'] = response.xpath('//span[@id="news-time"]/text()').extract_first()
        i['host'] = 'www.sohu.com'
        i['content'] = response.xpath('//article[@id="mp-editor"]').extract()[0]
        return i
