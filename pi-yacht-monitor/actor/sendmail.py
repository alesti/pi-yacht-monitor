from email.message import Message
import smtplib
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

emailconfig = r.hgetall("config.sendmail")
sender    = emailconfig["sender"]
recipient = emailconfig["recipient"]
server    = emailconfig["server"]
user      = emailconfig["user"]
password  = emailconfig["password"] 


message = r.lpop("messages")

if message is not None:
    parts = message.split("|")
    recipient = parts[0]
    subject = parts[1]
    message = parts[2]

    msg = Message() 
    msg.set_payload(message) 
    msg["Subject"] = subject 
    msg["From"] = sender 
    msg["To"] = recipient
    smtp = smtplib.SMTP(server) 
    smtp.login(user,password) 
    smtp.sendmail(sender,recipient,msg.as_string())
    smtp.quit()
