#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email import utils
from email.header import Header
import os

smtp_server  = "smtp.naver.com"
port = 587
userid = "happytoday83"
passwd = "tlsqkdnf87!"

def send_mail(from_user, to_user, cc_users, subject, text, attach):
        COMMASPACE = ", "
        msg = MIMEMultipart("alternative")
        msg["From"] = from_user
        msg["To"] = to_user
        msg["Cc"] = COMMASPACE.join(cc_users)
        msg["Subject"] = Header(s=subject, charset="utf-8")
        msg["Date"] = utils.formatdate(localtime=1)
        msg.attach(MIMEText(text, "html", _charset="utf-8"))

        if (attach != None):
                part = MIMEBase("application", "octet-stream")
                part.set_payload(open(attach, "rb").read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % os.path.basename(attach))
                msg.attach(part)


if __name__ == '__main__':
    smtp = smtplib.SMTP(smtp_server, port)
    smtp.starttls()
    smtp.login(userid, passwd)
    smtp.sendmail('happytoday83@naver.com', 'toyaji83@gmail.com ', "happytoday83@empal.com", "Test", "This is message test")
    smtp.close()