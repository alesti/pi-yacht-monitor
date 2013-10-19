from email.message import Message
import smtplib
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

emailconfig = r.hgetall("config.email.smtp")
sender    = emailconfig["sender"]
server    = emailconfig["server"]
user      = emailconfig["username"]
password  = emailconfig["password"] 

smtp_open = False

if r.llen("messages") > 0:
    smtp = smtplib.SMTP(server)
    smtp.login(user,password)
    smtp_open = True



while r.llen("messages") > 0:
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
        smtp.sendmail(sender,recipient,msg.as_string())

if smtp_open:
    smtp.quit()
