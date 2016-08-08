#!/usr/bin/env python
# coding=utf-8
import os,sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ip import *

mailInfo={
    "from":"wzwmxd@qq.com",
    "to":"884015671@qq.com",
    "hostname":"smtp.qq.com",
    "username":"wzwmxd",
    "to":"wzwmxd@qq.com",
    "hostname":"smtp.qq.com",
    "username":"wzwmxd",
    "mailsubject":"ROBOT",
    "mailencoding":"utf-8"
}
if __name__=='__main__':
    mailInfo['password']=raw_input('[操作提示:]请输入邮箱密码/授权码:')
    ip_info=get_ip_ip138()
    mailInfo['mailtext']=ip_info[0]+' '+ip_info[1]
    smtp=SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(0)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])
    
    msg=MIMEMultipart()
    msg.attach(MIMEText(mailInfo["mailtext"],"plain",mailInfo["mailencoding"]))
    msg['Subject']=Header(mailInfo['mailsubject'],mailInfo['mailencoding'])
    msg['from']=mailInfo['from']
    msg['to']=mailInfo['to']

    print '[操作提示:]正在发送邮件请耐心等待...'
    try:
        smtp.sendmail(mailInfo['from'],mailInfo['to'],msg.as_string())
        print '[操作提示:]邮件发送成功.'
    except:
        print '[操作提示:]邮件发送失败.'

    smtp.quit()
