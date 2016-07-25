#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

import urllib2


def get_html(url):
    try:
        req_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_6c6aeb1d6c029e488ea9ffd12154bb26=1469099863,1469153322,1469417275,1469432600; 37cs_pidx=2; 37cs_user=37cs38108468432; 37cs_show=32; Hm_lpvt_6c6aeb1d6c029e488ea9ffd12154bb26=1469433742',
            'Host': 'www.qisuu.com',
            'If-None-Match': 'W/"b5f7f985addd11:0"',
            'Referer': 'http://www.qisuu.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req)
        return resp.read()
    except IOError:
        return ""


print >> open('/home/kyo/test.txt', 'w'), get_html('http://www.qisuu.com/soft/sort01/index.html')
