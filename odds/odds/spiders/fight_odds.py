# -*- coding: utf-8 -*-
import scrapy
from ..items import EventItem, FighterItem


class FightOddsSpider(scrapy.Spider):
    name = 'fight_odds'
    start_urls = ['https://www.bestfightodds.com/events/ufc-231-holloway-vs-ortega-1584/']

    def parse(self, response):
        event = EventItem()

        # get event id from event link
        event_link = response.css('div.table-header a::attr(href)').extract_first()
        event_id = event_link.split('-')[-1]
        event['event_id'] = int(event_id)

        # get event name
        event['event_name'] = response.css('div.table-header a::text').extract_first()

        # get event date
        event['event_date'] = response.css('span.table-header-date::text').extract_first()

        yield event

        fighter = FighterItem()

        # get all fighters data from page
        for body in response.css('table.odds-table-responsive-header tbody tr'):

            # get fighters id from link in tbody
            try:
                fighter_link = body.css('th a::attr(href)').extract_first()
                fighter_id = fighter_link.split('-')[-1]

                # get fighter name
                fighter_name = body.css('span.tw::text').extract_first()
                if fighter_id != '#':
                    fighter['fighter_id'] = int(fighter_id)
                    fighter['fighter_name'] = fighter_name

                    yield fighter

            except AttributeError:
                pass
