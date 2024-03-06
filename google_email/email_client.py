import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config


class EmailClient:
    def __init__(self):
        self.server = smtplib.SMTP(
            config("EMAIL_SMTP_SERVER"), int(config("EMAIL_SMTP_PORT"))
        )
        self.email = config("EMAIL_ADDRESS")
        self.server.starttls()
        self.server.login(self.email, config("EMAIL_PASSWORD"))
