import numpy, urllib, urllib2
url='http://www.baidu.com/'
response=urllib2.urlopen(url).read()
print response