import os 
import ssl
import smtplib
from email.message import EmailMessage

email_sender='salimrashidov09@gmail.com'
email_password= 'kybysvpxltaummyc'
email_receiver=["bekzodrashidov0110@gmail.com","salihrashidov73@gmail.com","behruz.saidjonov@gmail.com"]


subject="Check out my video"
body="""
    I am Bekzod

"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()
print("Sending email")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(email_sender,email_password)
    server.sendmail(
        email_sender,email_receiver,em.as_string()

    )
    print("Email was sent")