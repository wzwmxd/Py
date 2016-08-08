# -*- coding: utf-8 -*-
import urllib2, urllib, cookielib, re, Image

url = 'http://rss.ustc.edu.cn/rssfeed.php'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Cookie': '_gscu_1103646635=69155042d0dour98; _ga=GA1.3.234722701.1469155052; _gscs_1103646635=705430570qkmsu98|pv:2; _gscbrs_1103646635=1',
    'Host': 'rss.ustc.edu.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0 FirePHP/0.7.4',
    'x-insight': 'activate',
    'Referer': ''
}
data = {'sn': 'USTCChineseMainSiteNews'}
req = urllib2.Request(url, urllib.urlencode(data), headers)
print urllib2.urlopen(req).read()

data['sn'] = 'USTCChineseMainSiteAnnouncement'
req = urllib2.Request(url, urllib.urlencode(data), headers)
print urllib2.urlopen(req).read()
'''
url = 'http://www.teach.ustc.edu.cn/category/notice/feed'
headers['Host'] = 'www.teach.ustc.edu.cn'
headers['Referer'] = 'http://www.teach.ustc.edu.cn/'
req = urllib2.Request(url, None, headers)
print urllib2.urlopen(req).read()
'''
