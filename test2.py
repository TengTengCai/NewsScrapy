from datetime import datetime

import pymysql


class DBController(object):
    def __init__(self):
        self.db = pymysql.connect(host='120.79.52.3',
                                  user='root',
                                  password='123456',
                                  port=3306,
                                  db='hodgepodge')
        self.db.set_charset('utf8')
        self.cursor = self.db.cursor()

    def find_type(self, type_name):
        sql = f'SELECT * from News_type where name="{type_name}"'
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        else:
            one = self.cursor.fetchone()
            if one:
                return one
            else:
                return self.add_type(type_name)

    def add_type(self, type_name):
        sql = "INSERT INTO News_type(name) VALUES ('%s')" % type_name
        try:
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
        my_datetime = datetime.strptime(item['publish_time'], '%Y-%m-%d %H:%M')
        sql = "INSERT INTO News_article(type_id, title, Publish_time, content, from_host, read_total) " \
              "VALUES ('%s', '%s', '%s', '%s', '%s', 0)" % \
              (type_id, item['title'], str(my_datetime), item['content'], item['host'])
        try:
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


def main():
    con = DBController()
    # tuple1 = con.find_type('娱乐')
    # print(tuple1)
    item = {
        'type': '体育',
        'title': 'test title',
        'publish_time': '2018-07-01 13:24',
        'host': 'www.sohu.com',
        'content': 'qwertyuiopasdfghjklzxcvbnm'
    }
    con.add_news_article(item)
    pass


if __name__ == '__main__':
    main()
