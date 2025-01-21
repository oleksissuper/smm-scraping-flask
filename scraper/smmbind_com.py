from bs4 import BeautifulSoup
from scraper.requests_session import CreateSession
from db.core import Db


class Smmbind(CreateSession):
    def __init__(self):
        self.base_url = 'https://smmbind.com'
        super().__init__(self.base_url)
        self.url_services = self.source + '/services'
        
    def scrape(self):
        try:
            src = self.get_requests(self.url_services)
            content = self.get_content(src)
            if content:
                Db().bulk_insert_or_update(content)
        except Exception as ex:
            self.logger.error(ex)

    def get_content(self, src: str) -> list:
        results = []
        soup = BeautifulSoup(src, 'lxml')
        table = soup.find('table', id='service-table')
        if not table:
            raise Exception('Something wrong with https://smmbind.com/services page content.')
        rows = table.select("tbody tr")
        for row in rows:
            try:
                tds = row.find_all('td')
                if len(tds) < 4:
                    continue
                self.service_id = self.get_td_text(tds, 0)
                self.service_name = self.get_td_text(tds, 1)
                self.rate_per_thousand = self.get_td_text(tds, 2)
                self.minimum_quantity = self.get_td_text(tds, 3)
                self.maximum_quantity = self.get_td_text(tds, 4)
                self.average_time = self.get_td_text(tds, 5)
                self.category_service = self.categorize_service(self.service_name)
                self.description = self.get_description(soup)
                results.append(self.to_dict())
            except Exception as ex:
                self.logger.error(ex)
        return results
    
    def get_td_text(self, tds: list[BeautifulSoup], number_list: int) -> str:
        value = ""
        if len(tds) > number_list:
            value = tds[number_list].text.strip()
        return value
    
    def get_description(self, row: BeautifulSoup) -> str:
        section = row.find('td', class_="service-description")
        if not section:
            return ""
        body = section.find('div', class_="modal-body")
        if not body:
            return ""
        return body.text.strip()


