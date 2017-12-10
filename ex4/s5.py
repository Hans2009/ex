#!/usr/bin/python
# -*- coding:UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.126.com"
mail_user = "lishuaitj@126.com"
mail_pass = "Wonder2017"

sender = 'lishuaitj@126.com'

receivers = ['80771104@qq.com','lishuaitj@126.com']
#receivers = ['80771104@qq.com']
#receivers = ['lishuaitj@126.com']
#receivers = ['lishuai6@lenovo.com']

message = MIMEText('this is from SMTP ubuntu','plain','utf-8')
#message['From'] = Header("lishuai<lishuaitj@126.com>",'utf-8')
message['From'] = "lishuai<lishuaitj@126.com>"

#message['To']   = Header("Shuai Li<80771104@qq.com>",'utf-8')
message['To']   = "Shuai Li<80771104@qq.com>"
#message['To']   = ["Shuai Li<80771104@qq.com>","lishuaitj<lishuaitj@126.com>"]
#message['To']   = "Hans Shuai6 Li<lishuai6@lenovo.com>"

subject = 'This is 15th mail'
message['Subject'] = Header(subject,'utf-8')
#message['Subject'] = subject

try:
    #smtpObj = smtplib.SMTP()
    #smtpObj.connect(mail_host,25)
    smtpObj = smtplib.SMTP_SSL(mail_host,465)
    smtpObj.set_debuglevel(1)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print ("Mail sent successfully")
except smtplib.SMTPException:
    print("Error:Failed to send mail")

