# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import time
import logging
from pymysql import cursors
from twisted.enterprise import adbapi
from proxyCrawl import settings
class ProxycrawlPipeline(object):
    table = settings.MYSQL_TABLE
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparas = dict(
            host = settings['MYSQL_HOST'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            db = settings['MYSQL_DB'],
            charset = 'utf8',
            cursorclass = cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparas)
        return cls(dbpool)
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.doInsert, item)
        query.addErrback(self.handleErr)
        return item
    def doInsert(self, cursor, item):
        s = item['ip'] + item['port']
        hash = hashlib.md5()
        hash.update(s.encode('utf-8'))
        hashCode = hash.hexdigest()
        sql = f"""insert into {self.table}(ip, port, crawlTime, hashCode, spider) values("{item['ip']}","{item['port']}","{time.strftime('%Y-%m-%d',time.localtime())}","{hashCode}","proxy")"""
        cursor.execute(sql)
        logging.info('##############成功插入！##############')
    def handleErr(self, failure):

        print(failure)
