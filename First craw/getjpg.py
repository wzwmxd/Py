import urllib
import re
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.+?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    '''
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        x+=1'''
    for i,url in enumerate(imglist):
        urllib.urlretrieve(url,"./pic/%s.jpg"%(i,))
html=getHtml('http://tieba.baidu.com/p/3415450222')
#print(html)
print(getImg(html))