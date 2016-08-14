# -*- coding: utf-8 -*-
import re, urllib, urllib2, sqlite3


# 用于计算身份证最后一位校验码
def calc_check(s):
    if len(s) != 17:
        return ""
    total = 0
    check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    for i in range(17):
        total += int(s[i]) * w[i]
    return check_code[(total % 11)]


# 查询 ustc 录取
def search(ident):
    url = 'http://admission.ustc.edu.cn/search.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Cookie': '_gscu_1103646635=69155042d0dour98; _ga=GA1.3.234722701.1469155052; _gscbrs_1103646635=1',
        'Host': 'admission.ustc.edu.cn',
        'Referer': 'http://admission.ustc.edu.cn/search.php',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0 FirePHP/0.7.4',
        'x-insight': 'activate'
    }
    post_data = {
        'sl': '查 询',
        'sfzh': ident
    }
    req = urllib2.Request(url, urllib.urlencode(post_data), headers)
    response = urllib2.urlopen(req)
    search_text = response.read()
    search_exp = r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;考&nbsp;生&nbsp;号：&nbsp;&nbsp;(\d+)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;姓　　名：&nbsp;&nbsp;(.+?)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;中　　学：&nbsp;&nbsp;(.+?)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;学　　院：&nbsp;&nbsp;(.+?)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;专　　业：&nbsp;&nbsp;<font color="red">(.+?)</font></TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;EMS&nbsp;单号：&nbsp;&nbsp;(\d+?)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;邮寄地址：&nbsp;&nbsp;(.+?)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+' + \
                 r'<TR.+?>[\r\n\t ]+<TD.+?>.+?</TD>[\r\n\t ]+' + \
                 r'<TD.+?>&nbsp;&nbsp;收&nbsp;件&nbsp;人：&nbsp;&nbsp;(.+?)</TD>[\r\n\t ]+' + \
                 r'<TD.+?>.+?</TD>[\r\n\t ]+</TR>[\r\n\t ]+'
    id_reg = re.compile(search_exp)

    out = id_reg.findall(search_text)
    return out


# 查询体检单，似乎也可以查询2015级
def get_body_check(ksh, sfzh):
    '''
    url = 'http://cx.ahzsks.cn/pugao/pgtjb2016_in.php'
    text = urllib2.urlopen(url).read().decode('gb2312')
    check_code_exp = ur'<div class="left">验证码:</div>[\r\n\t ]+' + \
                     ur'<div.+?><input.+?>(\d+)</div>'
    check_code_reg = re.compile(check_code_exp)
    check_code = check_code_reg.findall(text)[0]
    url = 'http://cx.ahzsks.cn/pugao/pgtjb2016_out.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'cx.ahzsks.cn',
        'Referer': 'http://cx.ahzsks.cn/pugao/pgtjb2016_in.php',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0 FirePHP/0.7.4',
        'x-insight': 'activate',
        'Content-Length': '51',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    post_data = {
        'ksh': ksh,
        'sfzh': sfzh,
        'yzm': check_code
    }
    req = urllib2.Request(url, urllib.urlencode(post_data), headers)
    response = urllib2.urlopen(req)
    print response.read().decode('gb2312')
    '''
    url = 'http://admin.ahzsks.cn/defaultroot/images/pgtjb2016/'
    url = url + ksh[:8] + '/' + ksh + '_' + sfzh + '.gif'
    urllib.urlretrieve(url, './body_check_img/%s_%s.gif' % (ksh, sfzh))


def save_in_database():
    conn = sqlite3.connect('ustc_2016.db')
    cur = conn.cursor()
    try:
        cur.execute('CREATE TABLE ustc_2016(id varchar(18) PRIIMARY KEY,\
                    ksh varchar(14),name varchar (32),school varchar(64),\
                    depart varchar(32),class varchar(32),post_id varchar (13),\
                    addr varchar(100),recv varchar(32));')
    except:
        print 'DATABASE exists.'


# local_list = [
#    '340101', '340102', '340103', '340104', '340111', '340121', '340122', '340123'
# ]
local_list = ['330201', '330201', '330203',
              '330204', '330205', '330206',
              '330211', '330212', '330225', '330226',
              '330281', '330282', '330283']
year = '1998'
month_list = ['%02d' % i for i in range(1, 13)]
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_month_list = [['%02d' % j for j in range(1, day_list[i] + 1)] for i in range(12)]
xx_list = ['%02d' % i for i in range(1, 101)]
s_list = ['%d' % i for i in range(10)]
total = 0
out = open('out.txt', 'a')

for s in s_list:
    for local in local_list:
        for i, month in enumerate(month_list):
            for day in day_month_list[i]:
                for xx in xx_list:
                    ident = local + year + month + day + xx + s
                    ident = ident + calc_check(ident)
                    s = search(ident)
                    print '\r正在查询:' + ident + ', ',
                    if len(s) == 0:
                        print '没有考生记录',
                    else:
                        print >> out, ident
                        print '找到一条.'
'''
for item in search('340104199811120015')[0]:
    print item,

print get_body_check('16340101155179', '340104199811120015')
'''
