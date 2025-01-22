from scraper.requests_session import CreateSession
from db.core import Db
from config.settings import settings

class Bulkfollows(CreateSession):
    def __init__(self):
        self.base_url = 'https://bulkfollows.com'
        super().__init__(self.base_url)
        self.url_services = self.source + '/api/v2'
    
    def scrape(self):
        try:
            params = {
                'key': settings.api_keys.bulkfollows,
                'action': 'services'
            }
            src = self.get_post_requests(self.url_services, params)
            content = self.get_content(src)
            if content:
                Db().bulk_insert_or_update(content)
        except Exception as ex:
            self.logger.error(ex)

    def get_content(self, rows: list[dict]) -> list:
        results = []
        for row in rows:
            try:
                self.service_id = row.get('service')
                self.service_name = row.get('name')
                self.rate_per_thousand = row.get('rate')
                self.minimum_quantity = row.get('min')
                self.maximum_quantity = row.get('max')
                self.average_time = ""
                self.category_service = self.categorize_service(self.service_name)
                self.description = ""
                results.append(self.to_dict())
            except Exception as ex:
                self.logger.error(ex)
        return results
