import smtplib
server=smtplib.SMTP('smtp.world4you.com',25)
server.ehlo()
server.login('mail@gmail.com','password123')