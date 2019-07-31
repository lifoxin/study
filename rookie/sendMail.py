#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText  

host = 'smtp.163.com'
port = 465
sender = '18344589481@163.com'
pwd = 'Tx123456'

def sentemail():
	receivers = ["805986238@qq.com","381407211@qq.com"] 
	with open("/tmp/yulu.text") as f:
		content = f.read()
#	msg = MIMEText(body, 'html') 
	msg = MIMEText(content,_subtype='plain',_charset='utf-8')
	msg['subject'] = '前程无忧运维工作' 
	msg['from'] = sender  
	for receiver in receivers:
		msg['to'] = receiver  
		s = smtplib.SMTP_SSL(host, port)  
		# 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
		s.login(sender, pwd)  
		s.sendmail(sender, receiver, msg.as_string().encode())
	print ('Done.sent email success')
			
if __name__ == '__main__':
	sentemail()
