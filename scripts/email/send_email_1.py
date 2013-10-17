# Sending an email with python

from email.message import Message
import smtplib

# Email-address of sender:
sender = "" 

# Email-address of recipient:
recipient = ""

# url of smtp-server 
server = ""

# username on smtp-server
user = ""

# password on smtp-server:
password = ""

# Mail subject and message
subject = "Mail vom Raspberry PI"
message = "Unglaublich, der Raspberry kann emails schicken!"

# Prepare message and send
msg = Message()
msg.set_payload(message)
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = recipient
smtp = smtplib.SMTP(server)
smtp.login(user,password)
smtp.sendmail(sender,recipient,msg.as_string())
smtp.quit()


