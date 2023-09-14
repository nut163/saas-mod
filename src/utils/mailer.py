```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, mail_server, mail_port, mail_username, mail_password):
        self.mail_server = mail_server
        self.mail_port = mail_port
        self.mail_username = mail_username
        self.mail_password = mail_password

    def send_email(self, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.mail_username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.mail_server, self.mail_port)
        server.starttls()
        server.login(self.mail_username, self.mail_password)
        text = msg.as_string()
        server.sendmail(self.mail_username, recipient, text)
        server.quit()
```