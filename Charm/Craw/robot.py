#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib, sqlite3, sys, datetime

url = 'http://weibo.cn/mblog/sendmblog?st=da1f85'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US, en;q = 0.5',
    'Connection': 'keep-alive',
    'Cookie': '_T_WM=798efab1572bbc03a0a429774361089f; SUB=_2A256kb8ADeTxGeNH41QX9ybKzD6IHXVWfcFIrDV6PUJbkdANLVOmkW0Li0_vNklV-LIU-qkRge5jz3mpAw..; gsid_CTandWM=4uPW630b1S4OMmrenEXLvp7pkaQ',
    'Host': 'weibo.cn',
    'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:47.0) Gecko/20100101 Firefox/47.0'
}

data = {
    'st': 'da1f85',
    'content': '',
    'rl': '0'
}
conn = sqlite3.connect('weather.db')
cur = conn.cursor()
day_night = sys.argv[1]
place = sys.argv[2]
city_date = '%s-%d-%d-%d' % (
    place, datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
result = cur.execute("SELECT * from weather_%s where city_date='%s'" % (day_night, city_date)).fetchall()[0]
if day_night == 'day':
    data['content'] = '[ROBOT:]%s %s %s 日间最高气温:%s[%s]' % (
        result[1].encode('utf-8'),
        result[2].encode('utf-8'),
        result[3].encode('utf-8'),
        result[4].encode('utf-8'),
        str(datetime.datetime.now())
    )
elif day_night == 'night':
    data['content'] = '[ROBOT:]%s %s %s 夜间最低气温:%s[%s]' % (
        result[1].encode('utf-8'),
        result[2].encode('utf-8'),
        result[3].encode('utf-8'),
        result[4].encode('utf-8'),
        str(datetime.datetime.now())
    )

req = urllib2.Request(url, urllib.urlencode(data), headers)
print '[操作提示:]正在发送微博，请稍后...'
response = urllib2.urlopen(req)
print '[操作提示:]发送成功'
