# -*- coding: utf-8 -*-
import scrapy
from ..items import EventItem, FighterItem


class FightOddsSpider(scrapy.Spider):
    name = 'fight_odds'
    allowed_domains = ['https://www.bestfightodds.com']
    start_urls = ['https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584/']

    def parse(self, response):
        event = EventItem()

        # get event id from event link
        event_link = response.css('div.table-header a::attr(href)').extract_first()
        event_id = event_link.split('-')[-1]
        event['event_id'] = int(event_id)

        # get event name
        event['event_name'] = response.css('div.table-header a::text').extract_first()
