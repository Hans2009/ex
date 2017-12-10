#!/usr/bin/python
# -*- coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.126.com"
mail_user = "lishuaitj@126.com"
mail_pass = "Wonder2017"


sender = 'lishuaitj@126.com'
#receivers = ['80771104@qq.com','lishuaitj@126.com']
#receivers = ['80771104@qq.com']
receivers = ['lishuaitj@126.com']
#receivers = ['lishuai6@lenovo.com']

message = MIMEText('Hello world, this is from SMTP ubuntu','plain','utf-8')
message['From'] = Header("ubuntu",'utf-8')
message['To']   = Header("Hans",'utf-8')

subject = 'This is 6th mail'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
#    smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print ("Mail sent successfully")
except smtplib.SMTPException:
    print("Error:Failed to send mail")

