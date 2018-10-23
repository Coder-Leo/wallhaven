# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WallhavenItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()
    data_id = Field()
    img_w = Field()
    img_h = Field()
