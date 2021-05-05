from bs4 import BeautifulSoup

class OtoMotoParser:
    def parse(self, olx_html_content):
        offers = BeautifulSoup(olx_html_content, 'html.parser').select('.offer-item__content')
        return [self.parse_offer(offer) for offer in offers]    

    def parse_offer(self, offer):
        return {'link': self.parse_link(offer), 'offer': '\n'.join([self.parse_title(offer), self.parse_subtitle(offer), self.parse_properties(offer), self.parse_location(offer)])}

    def parse_link(self, offer):
        return offer.select_one('a.offer-title__link')['href']        

    def parse_title(self, offer):
        return offer.select_one('h2.offer-title').text.strip()

    def parse_subtitle(self, offer):
        return offer.select_one('h3.offer-item__subtitle').text.strip()

    def parse_properties(self, offer):
        return offer.select_one('ul.ds-params-block').text.strip().replace('\n\n\n',' | ').replace('  ',' ')

    def parse_location(self, offer):
        return offer.select_one('h4.ds-location').text.strip().replace('\n',' ')
