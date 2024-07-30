from twilio.rest import Client
import smtplib

ACCOUNT_SID = "get your own"
AUTH_TOKEN = "get your own"

user_mail = "dummy@gmail.com"
password = "123456"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_text(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_="+17086690263",
            to="+your number"
        )
        print(message.sid)

    def send_mail(self, emails, message):
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=user_mail, password=password)
            connection.sendmail(from_addr=user_mail, to_addrs=emails, msg=message)
