# -*- coding: utf-8 -*-

import pymysql
import time
import json
import os
import requests
import logging
import hashlib
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
cursor.close()
db.close()
proxies = []
def deleteIp(ip, port):
    host = '127.0.0.1'
    user = 'root'
    passwd = '18351962092'
    dbname = 'proxies'
    tablename = 'proxy'
    db = pymysql.connect(host, user, passwd, dbname)
    cursor = db.cursor()
    logging.info('######################代理失效')
    sql = f"""delete from {tablename} where ip = '{ip}' and port = '{port}'"""
    cursor.execute(sql)
    cursor.close()
    db.commit()
    db.close()

if results != []:
    for row in results:
        ip = row[0]
        port = row[1]
        fromUrl = f"http://{ip}:{port}"
        proxy = {'http': fromUrl, 'https': fromUrl}
        toUrl = 'http://httpbin.org/ip'
        try:
            html = requests.get(url=toUrl, proxies=proxy, timeout=(0.1, 0.2))
        except Exception:
            logging.info('######################代理失效')
            deleteIp(ip, port)
            continue
        if html.status_code == 200 and ('無效用戶' not in html.text):
            result = json.loads(html.text)['origin'].split(',')
            if len(result) == 1:
                logging.info('######################代理可用')
                proxies.append({'ip': ip, 'port': port})
            else:
                logging.info('#######################代理失效')
                deleteIp(ip, port)
    if len(proxies) < 180:
        os.system('cd /home/xiyujing/proxyCrawl; scrapy crawl proxy')
    else:
        logging.info('########################睡眠中！')
        time.sleep(180)
else:
    logging.info('###############################代理池为空，重新爬取代理')
    os.system('cd /home/xiyujing/proxyCrawl; scrapy crawl proxy')











