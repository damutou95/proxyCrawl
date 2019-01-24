# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from proxyCrawl import settings
from proxyCrawl.items import ProxycrawlItem
import json

class ProxySpider(scrapy.Spider):
    name = 'proxy'
    #allowed_domains = ['sss']
    start_urls = []
    headers = settings.HEADERS
    proxySet = []
    for i in range(20):
        start_urls.append(f'http://www.89ip.cn/index_{str(i+1)}.html')

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        listPre = response.xpath('//tr')
        list = listPre[1:]
        #print(list)
        #file = open('/home/xiyujing/文档/proxy.json','a')
        for i in list:
            item = ProxycrawlItem()
            item['ip'] = i.xpath('./td[1]/text()').extract_first().strip('\t').strip()
            item['port'] = i.xpath('./td[2]/text()').extract_first().strip('\t').strip()
            print(item)
            proxy = f"http://{item['ip']}:{item['port']}"
            url = 'http://httpbin.org/ip'
            try:
                yield Request(url, callback=self.parse_item, meta={'proxy': proxy, 'item': item}, dont_filter=True)
            except Exception:
                continue


    def parse_item(self, response):
        if 'error' not in response.text:
            result = json.loads(response.text)['origin'].split(',')
            if len(result) == 1:
                self.proxySet.append(result[0])
            # if result == 1:
            #     if result !=
            #         response.meta['file'].write(response.meta['item'])
            yield response.meta['item']
