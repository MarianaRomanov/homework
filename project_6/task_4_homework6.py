import smtplib
from smtplib import SMTP
from email.message import EmailMessage

from_ad = 'mariana.mariam25@gmail.com'
to_ad = ['mariana.mariam25@gmail.com', 'el.piankova@gmail.com']
message = 'I did it!'
sbj = 'Subject for test message hw #6'

f = open('pass.txt')
pas = f.read()

# 1 basic
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(from_ad, pas)
smtpObj.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=message)
smtpObj.quit()

# 2 with 'with'
with SMTP('smtp.gmail.com') as smtp:
    smtp.starttls()
    smtp.login(from_ad, pas)
    smtp.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=message)
    smtp.quit()

# 3 with 'email'
msg = EmailMessage()
msg['Subject'] = sbj
msg['From'] = from_ad
msg['To'] = to_ad
msg.set_content(message)
with SMTP('smtp.gmail.com') as smtp:
    smtp.starttls()
    smtp.login(from_ad, pas)
    smtp.send_message(msg)
    smtp.quit()

f.close()
