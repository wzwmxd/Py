#!/usr/bin/env python
# coding=utf-8
import os,sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailInfo={
    "from":"884015671@qq.com",
    "to":"884015671@qq.com",
    "hostname":"smtp.qq.com",
    "username":"884015671",
    "mailsubject":"title",
    "mailencoding":"utf-8"
}
if __name__=='__main__':
    mailInfo['password']=raw_input('请输入密码:')
    mailInfo['mailtext']=raw_input("请输入你想说的话:\n")
    smtp=SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])
    
    msg=MIMEText(mailInfo["mailtext"],"plain",mailInfo["mailencoding"])
    msg['Subject']=Header(mailInfo['mailsubject'],mailInfo['mailencoding'])
    msg['from']=mailInfo['from']
    msg['to']=mailInfo['to']
    smtp.sendmail(mailInfo['from'],mailInfo['to'],msg.as_string())

    smtp.quit()
