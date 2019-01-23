# -*- coding: utf-8 -*-

import pymysql
import time
import os
host = '127.0.0.1'
user = 'root'
passwd = '18351962092'
dbname = 'proxies'
tablename = 'proxy'
db = pymysql.connect(host, user, passwd, dbname)
cursor = db.cursor()
sql2 = f"select * from {tablename}"
cursor.execute(sql2)
results = cursor.fetchall()
if len(results) < 230:
    sql = f"truncate table {tablename}"
    cursor.execute(sql)
    # cursor.commit()
    # cursor.close()
    # db.close()
    os.system('cd;cd proxyCrawl; scrapy crawl proxy')
else:
    time.sleep(600)













