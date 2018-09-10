# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from katadata.items import KataDataItem

class UrlsSpider(CrawlSpider):
    name = 'urls'
    allowed_domains = ['katadata.co.id']
    start_urls = ['http://katadata.co.id/indeks/search/-/-/-/-/255/-']
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagination__item.next > .pagination__link',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
        
        item_links = response.css('h4 > a::attr(href)').extract()
        
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)
        
    def parse_detail_page(self, response):
        title = response.css('kemenperin::text').extract()[0]
        article = ' '.join(response.css('.textArticle > p::text').extract())
        
        item = KataDataItem()
        item['title'] = title
        item['article'] = article
        item['url'] = response.url
        yield item
