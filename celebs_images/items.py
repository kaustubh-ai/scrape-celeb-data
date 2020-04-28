# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CelebsItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Net_Worth = scrapy.Field()
    Date_of_Birth = scrapy.Field()
    Gender = scrapy.Field()
    Height = scrapy.Field()
    Profession = scrapy.Field()
    Nationality = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
