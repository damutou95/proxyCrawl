# -*- coding: utf-8 -*-

import pymysql
import time
import json
import os
import requests
import logging
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
proxies = []
if results != []:
    for row in results:
        ip = row[0]
        port = row[1]
        fromUrl = f"http://{ip}:{port}"
        proxy = {'http': fromUrl, 'https': fromUrl}
        toUrl = 'http://httpbin.org/ip'
        try:
            html = requests.get(url=toUrl, proxies=proxy, timeout=(3, 10))
        except Exception:
            logging.info('代理失效')
            continue
        result = json.loads(html.text)['origin'].split(',')
        if len(result) == 1:
            logging.info('代理可用')
            proxies.append(result[0])
    if len(proxies) < 180:
        sql = f"truncate table {tablename}"
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        os.system('cd;cd proxyCrawl; scrapy crawl proxy')
    else:
        time.sleep(600)
else:
    os.system('cd;cd proxyCrawl; scrapy crawl proxy')











