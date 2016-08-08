# -*- coding: utf-8 -*-
import urllib2, re


def get_html(url):
    try:
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip',
            'Connection': 'close',
            'Referer': None}
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req)
        return resp.read()
    except IOError:
        return ""


def get_ip_ip138():
    url = 'http://1212.ip138.com/ic.asp'
    html = get_html(url).decode('gb2312')
    # print html
    re_exp = ur'<center>您的IP是：\[(.+?)\] 来自：(.+?)</center>'
    reg = re.compile(re_exp)
    return reg.findall(html)[0]


'''
if __name__ == '__main__':
    print get_ip_ip138()[0][0],get_ip_ip138()[0][1]
'''
