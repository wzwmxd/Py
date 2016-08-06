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
    for i, url in enumerate(imglist):
        urllib.urlretrieve(url, "./pic/%s.jpg" % (i,))


mirrors_main_url = 'http://mirrors.ustc.edu.cn/'
format=r'''<tr>
                <td class="filename"><a href="apache/">apache</a></td>
                <td class="filetime">2016-07-11 23:10:54</td>
                <td class="help">
                    <a href="https://lug.ustc.edu.cn/wiki/mirrors/help/apache"></a>
                </td>
            </tr>'''