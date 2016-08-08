# -*- coding: utf-8 -*-
# !/usr/bin/env python
import urllib2, urllib, sqlite3, sys, datetime

url = 'http://weibo.cn/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'weibo.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0 FirePHP/0.7.4',
    'x-insight': 'activate'
}

# 得到weibo的cookie
url = url + 'pub/'
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
print response.info().getheader('Set-Cookie')
