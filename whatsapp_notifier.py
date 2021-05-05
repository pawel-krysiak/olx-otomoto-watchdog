import os
from twilio.rest import Client

class WhatsappNotifier:

    def notify(self, msg):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=msg,
            from_='whatsapp:+14155238886',
            to='whatsapp:{number}'.format(number=os.environ["PH_NUMBER"])
        )
        return message