# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy import cmdline
# import time
# import pymysql
# import hashlib
# import json
# from scrapy import Request
#
# class GetipSpider(scrapy.Spider):
#     name = 'getIp'
#     #allowed_domains = ['fds']
#     #start_urls = ['http://fds/']
#     host = '127.0.0.1'
#     user = 'root'
#     passwd = '18351962092'
#     dbname = 'proxies'
#     tablename = 'proxy'
#     proxySet = []
#
#     def start_requests(self):
#         db = pymysql.connect(self.host, self.user, self.passwd, self.dbname)
#         cursor = db.cursor()
#         sql = f"select * from {self.tablename}"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         cursor.close()
#         for row in results:
#             ip = row[0]
#             port = row[1]
#             fromUrl = f"http://{ip}:{port}"
#             toUrl = 'http://httpbin.org/ip'
#             yield Request(toUrl, callback=self.parse, meta={'proxy': fromUrl})
#
#     def parse(self, response):
#         result = json.loads(response.text)['origin'].split(',')
#         if len(result) == 1:
#             self.proxySet.append(result[0])
#
#     if len(proxySet) < 50:
#         db = pymysql.connect(host, user, passwd, dbname)
#         cursor = db.cursor()
#         sql = f"truncate table {tablename}"
#         cursor.execute(sql)
#         cmdline.execute('scrapy crawl proxy'.split())
#     else:
#         time.sleep(700)
#
#     # def updateDb(self, ip, port):
#     #     s = ip + port
#     #     hash = hashlib.md5()
#     #     hash.update(s.encode('utf-8'))
#     #     hashCode = hash.hexdigest()
#     #     sql = f"""insert into {self.tablename}(ip, port, crawlTime, hashCode, spider) values("{ip}","{port}","{time.strftime('%Y-%m-%d',time.localtime())}","{hashCode}","proxy")"""
#     #     self.cursor.execute(sql)
#
#
#
#
