# -*- coding: utf-8 -*-

# Scrapy settings for proxyCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'proxyCrawl'

SPIDER_MODULES = ['proxyCrawl.spiders']
NEWSPIDER_MODULE = 'proxyCrawl.spiders'
# HEADERS = {
# 'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':  'gzip, deflate, br',
# 'Accept-Language':  'zh-CN,zh;q=0.9',
# 'Connection':  'keep-alive',
# 'Cookie':  '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZjY2ZmZTRlODkxNjg3NDU0YTJhOTMzZjBmMjMzYzc3BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXMzL2poUHZBTXpJcFZqQVNNVWZBZXFvTHpSeW1iWWx0VnJhRVdxbVh5YjA9BjsARg%3D%3D--ec5f9227d1b85890e0a91447bdd6e461f890c5b2; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1547705108; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1547705111',
# 'Host':  'www.xicidaili.com',
# 'Referer':  'https://www.xicidaili.com/nn/',
# 'Upgrade-Insecure-Requests':  '1',
# 'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
# }
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '18351962092'
MYSQL_DB = 'proxies'
MYSQL_TABLE = 'proxy'
HEADERS = {
'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':  'gzip, deflate',
'Accept-Language':  'zh-CN,zh;q=0.9',
'Cache-Control':  'max-age=0',
'Connection':  'keep-alive',
'Cookie':  'yd_cookie=b5823054-d08b-48a45a3fc09d119fc9d4a1a9c6c8b3627f97; UM_distinctid=1685a6a4a2e3d8-0c228e91a659a6-18211c0a-1fa400-1685a6a4a2f12e; Hm_lvt_8ccd0ef22095c2eebfe4cd6187dea829=1547705142; CNZZDATA1254651946=1249228181-1547699977-https%253A%252F%252Fwww.baidu.com%252F%7C1547711425; Hm_lpvt_8ccd0ef22095c2eebfe4cd6187dea829=1547714012',
'Host':  'www.89ip.cn',
'Referer':  'http://www.89ip.cn/',
'Upgrade-Insecure-Requests':  '1',
'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'proxyCrawl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 3
#CONCURRENT_REQUESTS_PER_IP = 3

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'proxyCrawl.middlewares.ProxycrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'proxyCrawl.middlewares.ProxycrawlDownloaderMiddleware': 543,
    # 'proxyCrawl.middlewares.HttpProxyMiddleware': 300,

}
DOWNLOAD_TIMEOUT = 30
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'proxyCrawl.pipelines.ProxycrawlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
