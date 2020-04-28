# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from celebs.items import CelebsItem


class CelebsInsectSpider(scrapy.Spider):
    name = 'celebs_insect'
    allowed_domains = ['celebritynetworth.com']
    start_urls = ['http://celebritynetworth.com/list/top-50-bollywood-celebrities//']

    def parse(self, response):
        # names = response.xpath('//h2[@class="title"]/text()').extract()
        bio_urls = response.xpath('//a[@class="anchor clearfix"]/@href').extract()
        for i in bio_urls:
            yield Request(i, callback=self.parse_celebs)

    def parse_celebs(self, response):
        l = ItemLoader(item=CelebsItem(), response=response)
        name = response.xpath('//h2[@class="title celeb_stats_table_header"]/text()').extract()[0]

        l.add_value('Name', name)
        table = response.xpath('//table[@class="celeb_stats_table"]/tr')
        for i, data in enumerate(table):
            entry = data.xpath('td//text()').extract()
            k, v = entry[0][:-1].replace(' ', '_'), entry[1]
            l.add_value(str(k), v)

        image_urls = response.xpath('//img[contains(@alt, "Net Worth") and contains(@height, "300")]/@data-src').extract()
        l.add_value('image_urls', image_urls)

        return l.load_item()