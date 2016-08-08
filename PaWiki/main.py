import urllib2
import urllib
import re

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getNextUrl(url):
    reg=r'<a href="/article/([0-9]+.htm)'
    nextre=re.compile(reg)
    nextUrl=re.findall(nextre,getHtml(url))
    return nextUrl
def Spide(article_name,n):
    if n<=0:
        return;
    else:
        urllist=getNextUrl(getHtml(init_page+article_name))
        for i, child_url in enumerate(urllist):
            urllib.urlretrieve(child_url,"E:\Wikipedia\%s"%(child_url))
        for i,child_url in enumerate(urllist):
            Spide(child_url,n-1)
init_page="http://www.jb51.net/article/"
Spide("59368.htm",2)