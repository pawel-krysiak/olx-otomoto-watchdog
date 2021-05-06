import os, requests, urllib, uuid
from twilio.rest import Client

class WhatsappNotifier:
    def __init__(self):
        self.url = "https://api.callmebot.com/whatsapp.php?phone={ph_number}&apikey={api_key}".format(ph_number=os.environ["PH_NUMBER"], api_key=os.environ["CALLMEBOT_API_KEY"])

    def notify(self, message):
        random_string_to_avoid_cache = str(uuid.uuid4())[:8]
        text = urllib.parse.quote_plus(random_string_to_avoid_cache + "\n\n" + message)
        url = self.url + "&text={text}".format(text=text)
        resp = requests.get(url)
        return resp.content