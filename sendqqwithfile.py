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
    "mailsubject":"MESSAGE FROM PARENTS",
    "mailencoding":"utf-8"
}
if __name__=='__main__':
    mailInfo['password']=raw_input('[操作提示:]请输入邮箱密码:')
    mailInfo['mailtext']=raw_input("[操作提示:]请输入你想说的话:\n")
    smtp=SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(0)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])
    
    msg=MIMEMultipart()
    msg.attach(MIMEText(mailInfo["mailtext"],"plain",mailInfo["mailencoding"]))
    msg['Subject']=Header(mailInfo['mailsubject'],mailInfo['mailencoding'])
    msg['from']=mailInfo['from']
    msg['to']=mailInfo['to']

    files=raw_input("[操作提示:]请拖拽文件，多个文件之间用空格分开\n")
    file_list=files.split(' ')

    for file in file_list:
        if file=='':
            continue
        att=MIMEText(open(file[1:-1]).read(),'base64','utf-8')
        att['Content-Type']='application/octet-stream'
        att['Content-Disposition']='attachment;filename=%s'%file
        msg.attach(att)

    print '[操作提示:]正在发送邮件请耐心等待...'
    try:
        smtp.sendmail(mailInfo['from'],mailInfo['to'],msg.as_string())
        print '[操作提示:]邮件发送成功.'
    except:
        print '[操作提示:]邮件发送失败.'

    smtp.quit()
