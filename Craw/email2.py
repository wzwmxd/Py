# -*- coding: utf-8 -*-
import smtplib
import email.MIMEMultipart  # import MIMEMultipart
import email.MIMEText  # import MIMEText
import email.MIMEBase  # import MIMEBase
import os.path
import sys
import mimetypes
import email.MIMEImage  # import MIMEImage
from email.header import Header

# 命令 mail.py <1:发送方（回复地址）10000@qq.com> <2:发送地址，多个以;隔开> <3:发送文件>
From = "%s<wzwmxd@qq.com>" % Header("许仕杰", "utf-8")
ReplyTo = sys.argv[1]
To = sys.argv[2]
file_name = sys.argv[3]  # 附件名

server = smtplib.SMTP("smtp.exmail.qq.com", 25)
server.login("wzwmxd@qq.com", "4181456184xu")  # 仅smtp服务器需要验证时

# 构造MIMEMultipart对象做为根容器
main_msg = email.MIMEMultipart.MIMEMultipart()

# 构造MIMEText对象做为邮件显示内容并附加到根容器
text_msg = email.MIMEText.MIMEText("顶击拨号帮你转发的邮件", _charset="utf-8")
main_msg.attach(text_msg)

# 构造MIMEBase对象做为文件附件内容并附加到根容器
ctype, encoding = mimetypes.guess_type(file_name)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)
file_msg = email.MIMEImage.MIMEImage(open(file_name, 'rb').read(), subtype)

# 设置附件头
basename = os.path.basename(file_name)
file_msg.add_header('Content-Disposition', 'attachment', filename=basename)  # 修改邮件头
main_msg.attach(file_msg)

# 设置根容器属性
main_msg['From'] = From
main_msg['Reply-to'] = ReplyTo
# main_msg['To'] = To
main_msg['Subject'] = u"亲，你朋友给你发送的邮件－许仕杰"
main_msg['Date'] = email.Utils.formatdate()

# main_msg['Bcc'] = To
# 得到格式化后的完整文本
fullText = main_msg.as_string()

# 用smtp发送邮件
try:
    server.sendmail(From, To.split(';'), fullText)
finally:
    server.quit()
