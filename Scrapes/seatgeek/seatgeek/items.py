# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SeatgeekItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # artist = scrapy.Field()
    #text = scrapy.Field()
    #showUrls = scrapy.Field()
    venue = scrapy.Field()
    artist_name = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
