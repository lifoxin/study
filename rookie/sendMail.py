#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['805986238@qq.com','szwjpk@vip.qq.com']

message = MIMEText('来了就是深圳人...','plain','utf-8')
message['From'] = Header("深圳",'utf-8')
message['To'] = Header("上海",'utf-8')

subject = '望京最好的扑克'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("success")
except smtplib.SMTPException:
    print("false")

