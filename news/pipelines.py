# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random
import time
from datetime import datetime

import pymysql


class NewsPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host='120.79.52.3',
                                  user='root',
                                  password='123456',
                                  port=3306,
                                  db='hodgepodge')
        self.db.set_charset('utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        my_item = dict(item)
        time.sleep(random.randint(1, 3))
        if self.add_news_article(my_item):
            # self.close_db()
            return item

    def find_type(self, type_name):
        # sql = f'SELECT * from News_type where name="{type_name}"'
        sql = "SELECT * from News_type where name='%s'" % type_name
        try:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
            return None
        else:
            one = self.cursor.fetchone()
            if one:
                return one
            else:
                return self.add_type(type_name)

    def add_type(self, type_name):
        sql = "INSERT INTO News_type(name) VALUES ('%s')" % type_name
        try:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        else:
            return self.find_type(type_name)

    def add_news_article(self, item):
        type_name = item['type']
        type_id = self.find_type(type_name)[0]
        if not type_id:
            return False
        my_datetime = datetime.strptime(item['publish_time'], '%Y-%m-%d %H:%M')
        sql = "INSERT INTO News_article(type_id, title, Publish_time, content, from_host, read_total) " \
              "VALUES ('%s', '%s', '%s', '%s', '%s', 0)" % \
              (type_id, item['title'], str(my_datetime), item['content'], item['host'])
        try:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
        else:
            return True

    def close_db(self):
        self.db.close()
