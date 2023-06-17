import os
import ssl, smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
os.environ['email'] = 'my_email'
os.environ['email_password'] = 'my_password'

from email.message import EmailMessage
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dadakhodjaeva Visola'
email['to'] = 'visolad1@gmail.com'
email['subject'] = 'Почему вам стоит завести кошку!'

email.set_content(html.substitute(
        {}
    ),
    'html'
)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    try:
        smtp.starttls()
        smtp.login(os.environ.get('email'), os.environ.get('email_password'))
        smtp.send_message(email)
        print('all ok')
    except Exception as err:
        print(err)
