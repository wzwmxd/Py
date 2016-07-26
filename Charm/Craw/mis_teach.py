# -*- coding: utf-8 -*-

import urllib2, urllib, cookielib, re


def get_course(course_html):
    course1 = r'<td.+?>[\r\n\t ]*' + \
              r'<a.+?>[\r\n\t ]*' + \
              r'<font.+?>(.+?)</font>[\r\n\t ]*' + \
              r'</a>[\r\n\t ]*.+?</td>[\r\n\t ]*'
    course2 = r'<td.+?>[\r\n\t ]*.+?</td>[\r\n\t ]*'
    course_exp1 = r'<td.+?>[\r\n\t ]*' + \
                  r'(\d+?)[\r\n\t ]*</td>[\r\n\t ]*' + \
                  r'<td.+?>[\r\n\t ]*([\d\w]+?)[\r\n\t ]*</td>[\r\n\t ]*' + \
                  r'<td.+?>[\r\n\t ]*<a.+?>[\r\n\t ]*' + \
                  r'<font.+?>(.+?)</font>[\r\n\t ]*' + \
                  r'</a>[\r\n\t ]*</td>[\r\n\t ]*'
    course_exp2 = r'<td.+?>(.+?)</td>[\r\n\t ]*' + \
                  r'<td.+?>(.+?)</td>[\r\n\t ]*' + \
                  r'<td.+?>(.+?)</td>[\r\n\t ]*' + \
                  r'<td.+?>(.+?)</td>[\r\n\t ]*' + \
                  r'<td.+?>[\r\n\t ]*([\d/]+?)[\r\n\t ]*</td>[\r\n\t ]*' + \
                  r'<td.+?>[\r\n\t ]*(.+?)[\r\n\t ]*</td>[\r\n\t ]*'
    course_reg1 = re.compile(course_exp1 + course1 + course_exp2)
    course_reg2 = re.compile(course_exp1 + course2 + course_exp2)
    return course_reg1.findall(course_html) + course_reg2.findall(course_html)


url = 'http://mis.teach.ustc.edu.cn'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US, en;q = 0.5',
    'Connection': 'keep-alive',
    'Cookie': '_gscu_1103646635=69155042d0dour98; _gscs_1103646635=69155042wyvvcb98|pv:1; _ga=GA1.3.234722701.1469155052; _gat=1',
    'Host': 'mis.teach.ustc.edu.cn',
    'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:47.0) Gecko/20100101 Firefox/47.0'
}
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
jsessionid = response.info().getheader('Set-Cookie')
print 'Get cookie OK: ', jsessionid

headers['Cookie'] = jsessionid
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/'
data = {'userbz': 's'}
data = urllib.urlencode(data)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
compressedData = response.read()
print 'Open http://mis.teach.ustc.edu.cn/init.do OK.'

# date = '1469152125415'
date = '1469242601259'
url = 'http://mis.teach.ustc.edu.cn/randomImage.do?date=%%27%s%%27' % date
headers['Accept'] = '*/*'
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/userinit.do'
data = {'date': date}
data = urllib.urlencode(data)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
compressedData = response.read()
f = open('/home/kyo/random_img_file.jpg', 'w')
print >> f, compressedData
f.close()
print 'Get random_img OK.'

url = 'http://mis.teach.ustc.edu.cn/login.do'
data = {
    'check': '8547',
    'passWord': '',
    'userCode': '',
    'userbz': 's'
}
data['check'] = ''  # raw_input('Please input check_code:')
data['passWord'] = raw_input('Password: ')
data['userCode'] = raw_input('Username: ')
data = urllib.urlencode(data)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
# compressedData = response.read()

print 'Login successfully, get info...'
'''
url = 'http://mis.teach.ustc.edu.cn/bt_top.do'
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/login.do'
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
compressedData = response.read()
'''
url = 'http://mis.teach.ustc.edu.cn/left.do'
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/login.do'
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
# compressedData = response.read()
# print compressedData

url = 'http://mis.teach.ustc.edu.cn/init_xk_ts.do'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/left.do'
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)

url = 'http://mis.teach.ustc.edu.cn/init_st_xk_dx.do'
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/init_st_xk.do'
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
# print response.read()

url = 'http://mis.teach.ustc.edu.cn/init_st_xk_dx.do'
headers['Referer'] = 'http://mis.teach.ustc.edu.cn/init_st_xk_dx.do'
data = {
    'kcmc': '',
    'kkdw': '',
    'qr_queryType': 'null',
    'queryType': '2',
    'rkjs': '',
    'seldwdm': 'null',
    'selkkdw': '',
    'seyxn': '2016',
    'seyxq': '1',
    'sjpdmlist': '',
    'xnxq': '20161'
}
req = urllib2.Request(url, urllib.urlencode(data), headers)
response = urllib2.urlopen(req)
course_html = response.read().decode('GBK').encode('utf-8')
# print course_html
course_list = get_course(course_html)
# print course_list
for elem in course_list:
    for i in range(len(elem)):
        print elem[i],
    print '\n'
