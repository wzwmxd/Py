import re, urllib


def get_html(url):
    try:
        page = urllib.urlopen(url)
        html = page.read()
        return html
    except IOError:
        return ""
def get_book_page(html):
    re

main_url = r'http://www.qisuu.com'
root_url = main_url + '/soft'
