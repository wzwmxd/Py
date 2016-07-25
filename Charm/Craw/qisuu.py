#!/usr/bin/env python
# coding=utf-8
import re, urllib, sys, urllib2, threading, thread, os, sys
import time
import socket


def get_html(url):
    try:
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', \
            'Accept': 'text/html;q=0.9,*/*;q=0.8', \
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', \
            'Accept-Encoding': 'gzip', \
            'Connection': 'close', \
            'Referer': None}
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req)
        return resp.read()  # decode('utf-8').encode()  # .decode('gbk').encode(type)
    except IOError:
        return ""


def get_book_page(html):
    book_item_author1 = ur'<li>[\r\n\t ]+<div class="s">.+?<a.+?>(.+?)</a><br +/?>'
    book_item_author2 = ur'<li>[\r\n\t ]+<div class="s">([^<]+?)<br +/?>'
    book_item_size = ur'.+?([\d\.]+)MB<br */?>'
    book_item_other = ur'.+?<em class="lstar([1-5])"></em><br>.+?</div>[\r\n\t ]+<a href="(/[\d]+.html)">' + \
                      ur'<img src="(.+?\.jpg)">' + \
                      ur'(.+?)</a>[\r\n\t ]+<div class="u">.+?</div>'
    book_re1 = re.compile(book_item_author1 + book_item_size + book_item_other)
    book_re2 = re.compile(book_item_author2 + book_item_size + book_item_other)
    book_list = re.findall(book_re1, html)
    book_list2 = re.findall(book_re2, html)
    return book_list + book_list2


def get_book_file(html):
    show_info = ur'<div class="showInfo">[\r\n\t ]+<p>(.+?)</p>[\r\n\t ]+</div>'
    show_info_re = re.compile(show_info)
    show_info_text = re.findall(show_info_re, html)

    text_file = ur'<a +class="downButton" +href=\'(.+?)\''
    text_file_re = re.compile(text_file)
    text_file_link = re.findall(text_file_re, html)
    # print text_file_link
    return show_info_text, text_file_link


def download_report(count, blockSize, totalSize):
    percent = int(count * blockSize * 100 / totalSize)
    sys.stdout.write("\r%d%%" % percent + '  completing')
    sys.stdout.flush()


def get_book_name(url):
    addr = url.split('/')
    return addr[-1]


save_dir = '/home/kyo/C/Books/'
main_url = 'http://www.qisuu.com'
root_url = main_url + '/soft'
book_list = []
socket.setdefaulttimeout(30.0)  # timeout

type = sys.getfilesystemencoding()  # 关键
# print content.decode("UTF-8").encode(type)  # 关键

print 'Scanning websites...'
for i in range(1, 2):
    for j in range(1, 3):
        if j == 1:
            url = root_url + '/sort0%d/index.html' % i
        else:
            url = root_url + '/sort0%d/index_%d.html' % (i, j)
        print url
        try:
            text = get_html(url)
            text = get_html(url)
            print text  # .decode('utf8').encode(type)
            book_page_list = get_book_page(text)
            book_file_list = []
            for book_page in book_page_list:
                book_file = get_book_file(get_html(book_page))
                print book_file
                book_file.append(book_file)
            book_list = list(set(book_list).union(set(book_file_list)))
        except IOError, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            break

