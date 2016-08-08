# -*- coding: utf-8 -*-
# !/usr/bin/env python
import urllib2, urllib, sqlite3, sys, datetime, re, chardet

# 获取st值，这个值好像在每日更新
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US, en;q = 0.5',
    'Connection': 'keep-alive',
    'Cookie': '_T_WM=c1ea775bb14caeacdd56cb50f28e7d72; \
    SUB=_2A256n2M9DeTxGeNH41QX9ybKzD6IHXVWYA11rDV6PUJbkdAKLVHwkW0Wxrxt_dzr4acit4QFeXl_VOKwZw..; \
    gsid_CTandWM=4uwG50921iqnqIwWljZlcp7pkaQ',
    'Host': 'weibo.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'x-insight': 'activate'
}
'''
d = {'p': 'r', 'pos': '65', 'rand': '1234', 's2w': 'admin'}
url = 'http://weibo.cn'
req = urllib2.Request(url, urllib.urlencode(d), headers)
response = urllib2.urlopen(req)
html = response.read().decode('')
print 'format:', chardet.detect(html)
print response.getcode()
print >> open('test.html', 'w'), html
st_exp = r'<form method="post" accept-charset="UTF-8" action="/mblog/sendmblog\?st=(.+?)">'
st_reg = re.compile(st_exp)
st = st_reg.findall(html)[0]
'''
data = {
    'st': '40cf35',
    'content': '',
    'rl': '0'
}
url = 'http://weibo.cn/mblog/sendmblog?st=%s' % data['st']

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
print '[操作提示:]微博内容:\n' + data['content']
print '[操作提示:]正在发送微博，请稍后...'
response = urllib2.urlopen(req)
print '[操作提示:]发送成功'
