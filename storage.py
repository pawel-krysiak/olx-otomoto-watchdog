import requests, json
import os

class Storage: 
    URL = 'https://jsonblob.com/api/jsonBlob/{blob}'.format(blob=os.environ['BLOB']) 
    HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
    
    def get_offers(self):
        return self.session.get(self.URL).json()

    def update_offers(self, data):
        return self.session.put(self.URL, data=json.dumps(data)).json()