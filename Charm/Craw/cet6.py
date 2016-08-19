# -*- coding: utf-8 -*-

import urllib2, urllib, cookielib, re, Image

ustc1 = '340011'
ustc1 = '340012'
TimeType = '1622'
# TimeType='1621'四级
# 假设每个考场不超过80人
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_41458584ac7611d4bad1fc47207293a2=1471593751; Hm_lpvt_41458584ac7611d4bad1fc47207293a2=1471593760' + \
              '; ASP.NET_SessionId=2deqr0x0l3ycmg4unmittqju; CNZZDATA1327025=cnzz_eid%3D2135347720-1471589151-http%253A' + \
              '%252F%252Fwww.233.com%252F%26ntime%3D1471589151; _cnzz_CV1255235319=%E8%AE%BF%E5%AE%A2%E7%B1%BB%E5%9E' + \
              '%8B%7C%E6%B8%B8%E5%AE%A2%7C0%26%E8%AE%BF%E5%AE%A2%E6%9D%A5%E6%BA%90%7C%E8%BF%B7%E4%BD%A0%E7%89%88%7C0' + \
              '; CNZZDATA1255235319=1617764625-1471593544-http%253A%252F%252Fwww.233.com%252F%7C1471593544; CNZZDATA1257783334' + \
              '=194391230-1471592945-http%253A%252F%252Fwww.233.com%252F%7C1471592945; CNZZDATA4109769=cnzz_eid%3D2027526205-1471590228-http' + \
              '%253A%252F%252Fwww.233.com%252F%26ntime%3D1471590228',
    'Host': 'wx.233.com',
    'Referer': 'http://wx.233.com/u/hook/9.html?format=iframe&width=658',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'X-Requested-With': 'XMLHttpRequest'
}
post_data = {
    'api_hookId': '9',
    'format': 'iframe',
    'id': '',
    'name': ''
}
post_data['name'] = '许仕杰'
start = '340012162200334'
for i in range(1, 101):
    for j in range(1, 81):
        post_data['id'] = ustc1 + TimeType + '%03d%02d' % (i, j)
        if int(post_data['id']) <= int(start):
            continue
        url = 'http://wx.233.com/u/hook/fork/o?format=iframe&id=' + post_data['id'] + '&name=' + post_data[
            'name'] + '&api_hookId=' + post_data['api_hookId']
        response = urllib2.urlopen(url)
        text = response.read()
        print '\r[%s]: 正在查询...' % post_data['id'],
        if text.find('失败') == -1:
            print text
            break
