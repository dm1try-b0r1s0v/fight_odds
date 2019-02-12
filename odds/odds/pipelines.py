# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from odds.items import EventItem, FighterItem


class OddsPipeline(object):

    def __init__(self):
        self.conn = psycopg2.connect(
            host='baasu.db.elephantsql.com',
            user='vimfzmjn',
            password='VJAW7UC3x3MtSsxnaOsCTMQv0zCtRdUT',
            dbname='vimfzmjn',
        )
        self.fighters_id = []

    def process_item(self, item, spider):
        cur = self.conn.cursor()
        if isinstance(item, FighterItem):
            cur.execute('''insert into fighters(id, fighter_name) values (%s, %s);''', [
                item['fighter_id'],
                item['fighter_name']
            ])
            self.fighters_id.append(item['fighter_id'])
            self.conn.commit()
        elif isinstance(item, EventItem):
            if item is not None:
                cur.execute('''insert into events (id, event_name, event_date, fighter_ids) values (%s, %s, %s, %s);''',
                            [
                                item['event_id'],
                                item['event_name'],
                                item['event_date'],
                                item['fighters_id']
                            ])
                self.conn.commit()

        return item
