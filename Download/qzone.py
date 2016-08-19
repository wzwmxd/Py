# -*-coding=utf-8-*-
import urllib, urllib2, re

url = 'http://user.qzone.qq.com/2641808532'

data = {
    'a': 'dl',
    'exec': '9405',
    'lic': '38488187',
    'lpid': '3152983'
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': 'lastshowtime2641808532=1471225618751; pgv_pvid=8147016232; pac_uid=1_884015671; pt2gguin=o2641808532' + \
              '; ptcz=7d294b419da0802dfe2b6174f72a07d6a885a0132fc0d9741134a00653a0b63b; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT' + \
              '=0; cpu_performance_v8=45; __Q_w_s__QZN_TodoMsgCnt=1; o_cookie=884015671; __Q_w_s__appDataSeed=1; hasShowWeiyun2641808532' + \
              '=1; lastshowtime2641808532=1469823070568; __Q_w_s_hat_seed=1; ptisp=cm; pgv_info=ssid=s5743736260; ptui_loginuin' + \
              '=wzwmxd@qq.com; RK=2Gc/zSVDzK; fnc=2; 2641808532_todaycount=0; 2641808532_totalcount=2; pgv_pvi=1201165312' + \
              '; pgv_si=s7813536768; _qz_referrer=user.qzone.qq.com; uin=o2641808532; skey=@f172nWM1W; p_uin=o2641808532' + \
              '; p_skey=8c5zoNjmBNu2glEvOL1Qt0VnF-LE4vxHp4Gi-AOs-m4_; pt4_token=vyOKCKvgmJiuxfCjXzZ15C5yG1USGDwKZuD' + \
              'Zzw8pB3o',
    'Host': 'user.qzone.qq.com',
    'If-Modified-Since': 'Tue, 16 Aug 2016 00:00:29 GMT',
    'Referer': 'http://qzs.qq.com/qzone/v5/loginsucc.html?para=izone',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
}
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
print response.read()
