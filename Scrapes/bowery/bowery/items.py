# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoweryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    venue = scrapy.Field()
    headline_artist_name = scrapy.Field()
    other_artists_name = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    button = scrapy.Field()
    #pass
