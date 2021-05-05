import requests

from parsers.otomoto_parser import OtoMotoParser

class OffersParser:
    OTOMOTO = 'https://www.otomoto.pl/motocykle-i-quady/yamaha/fz/od-2008/?search%5Bfilter_float_engine_capacity%3Ato%5D=750&search%5Bfilter_enum_features%5D%5B0%5D=abs&search%5Border%5D=created_at%3Adesc&search%5Bcountry%5D='
    OLX = 'https://www.olx.pl/motoryzacja/motocykle-skutery/q-fz6-s2/?search%5Bfilter_enum_mark%5D%5B0%5D=yamaha&search%5Bfilter_float_year%3Afrom%5D=2008'    
    
    def __init__(self):
        self.otomoto_content = requests.get(self.OTOMOTO).content

    def get_current_offers(self):
        return { "otomoto" : OtoMotoParser().parse(self.otomoto_content) }