# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):
    event_id = scrapy.Field()
    event_name = scrapy.Field()
    event_date = scrapy.Field()
    fighters_id = scrapy.Field()


class FighterItem(scrapy.Item):
    fighter_id = scrapy.Field()
    fighter_name = scrapy.Field()
