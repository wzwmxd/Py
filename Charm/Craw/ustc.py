import urllib, urllib2, re, requests


def get_respone(url):
    try:
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', \
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip',
            'Connection': 'close',
            'Referer': None}
        req = urllib2.Request(url, None, req_header)
        return urllib2.urlopen(req)
    except:
        return None


def is_modified(url):
    resp = requests.get(url)
    if resp.status_code == 303:
        return True
    else:
        return False


url = 'http://www.ustc.edu.cn/ggtz/'
print get_respone(url).read()
print is_modified(url)
