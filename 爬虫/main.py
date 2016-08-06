import urllib
import re


def get_html(url):
    try:
        page = urllib.urlopen(url)
        html = page.read()
        return html
    except IOError:
        return ""


def get_img(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    '''
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        x+=1'''
    for i, url in enumerate(imglist):
        urllib.urlretrieve(url, "./pic/%s.jpg" % (i,))


baidu_html = get_html('http://tieba.baidu.com/p/3415450222')
# print(html)
print(get_img(baidu_html))
