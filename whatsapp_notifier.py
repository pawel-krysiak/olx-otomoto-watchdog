import os, requests, urllib
from twilio.rest import Client

class WhatsappNotifier:
    def __init__(self):
        self.url = "https://api.callmebot.com/whatsapp.php?phone={ph_number}&apikey={api_key}".format(ph_number=os.environ["PH_NUMBER"], api_key=os.environ["CALLMEBOT_API_KEY"])

    def notify(self, message):
        url = self.url + "&text={text}".format(text=urllib.parse.quote_plus(message))
        resp = requests.get(url)
        return resp.content