"""
    Script to track olx and otomoto announcements and notify me if there is something new
"""
from offers_parser import OffersParser
from storage import Storage
from whatsapp_notifier import WhatsappNotifier

class OlxOtomotoWatchdog:

    def __init__(self):
        self.storage = Storage()
        self.last_offers = self.storage.get_offers()

    def run(self):
        current_offers = OffersParser().get_current_offers()
        self.storage.update_offers(current_offers)
        message = self.format_otomoto_message(current_offers['otomoto'][0])
        return message
        
    def format_otomoto_message(self, otomoto):
        return '\n\n'.join([otomoto['link'], otomoto['offer']])
        
print(OlxOtomotoWatchdog().run())