#!python
# -*- coding:UTF-8 -*-

import smtplib
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header         import Header
from email.utils          import formataddr
from email.mime.application    import MIMEApplication

my_sender='*******@126.com' #填写你的邮箱
my_password='******'     #填写你的邮箱SMTP的授权码 非邮箱登陆密码
my_receiver='*****@kindle.cn'   #填写你的kindle邮箱

msg=MIMEMultipart()
msg['From']=formataddr(['yourname',my_sender])
msg['To']=formataddr(['kindle',my_receiver])
msg['Subject']=Header('发送个人文档','utf-8')

#msg.attach(MIMEText('个人文档','plain','utf-8'))
file=input('请输入文件名包含格式\n')
#文件的路径可根据需要更改
attch_file=MIMEApplication(open('c:\\Users\\administrator\\desktop\\'+file,'rb').read())
attch_file['Content-Type']='application/octet-stream'
attch_file['Content-Disposition']='attachment;filename="test.mobi"'#修改需要的格式名，必须与转送的文件格式名一致
msg.attach(attch_file)

try:
    server=smtplib.SMTP_SSL('smtp.126.com',465)#填写你的邮箱的host主机与post端口
    server.ehlo()
    server.login(my_sender,my_password)
    server.sendmail(my_sender,my_receiver,msg.as_string())
    server.quit()
    print('发送成功')
except smtplib.SMTPException:
    print('发送失败...')
