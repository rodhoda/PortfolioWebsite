import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
username = "rod.hoda12live.co.uk@gmail.com"
password = "wyrmzfdsbzxpryxf"

reciever = "rod.hoda12live.co.uk@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)