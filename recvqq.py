#!/usr/bin/env python
# coding=utf-8
import string
import poplib
import sys
from email import parser
#import StringIO,rfc822

servername='pop.qq.com'
username='884015671@qq.com'
password=raw_input("password:")

pop_conn=poplib.POP3_SSL(servername)
pop_conn.user(username)
pop_conn.pass_(password)

messages=[pop_conn.retr(i) for i in range(1,len(pop_conn.list()[1])+1)]

messages=["\n".join(mssg[1]) for mssg in messages]

messages=[parser.Parser().parsestr(mssg) for mssg in messages]
i=0
for message in messages:
    i=i+1
    if i>20:
        break
    print message['From']
    #if message['Subject']!='MESSAGE FROM PARENTS':
    #    continue
    mailName="mail %d"%(i)
    print '\r'
    sys.stdout.flush()
    print '接受了 %d 封邮件'%i,
    f=open(mailName+'.log','w')
    print >>f,"Date: ",message['Date']
    print >>f,"From: ",message['From']
    print >>f,"To: ",message['To']
    print >>f,'Subject: ',message['Subject']
    print >>f,'Datai: '
    j=0
    for part in message.walk():
        j=j+1
        fileName=part.get_filename()
        contentType=part.get_content_type()
        if fileName:
            data=part.get_payload(decode=True)
            fileName="%s.%d.%s"%(mailName,j,fileName)
            fEx=open(fileName,'wb')
            fEx=write(data)
            fEx.close()
        elif contentType=='text/plain' or contentType=='text/html':
            data=part.get_payload(decode=True)
            print >>f,data
    f.close()
pop_conn.quit()
    
