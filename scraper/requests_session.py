import requests
import re
from utils.logger import Logger


class CreateSession():
    def __init__(self, source: str):
        self.logger = Logger().get_logger(__name__)
        self.service_id = 0
        self.service_name = ""
        self.rate_per_thousand = 0
        self.minimum_quantity = 0
        self.maximum_quantity = 0
        self.average_time = ""
        self.category_service = []
        self.description = ""
        self.source = source

    def get_requests(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    
    def get_post_requests(self, url: str, params: dict) -> dict:
        response = requests.post(url, data=params)
        response.raise_for_status()
        return response.json()
    
    def to_dict(self) -> dict:
        return {
            "service_id": int(self.service_id),
            "service_name": self.clean_string(self.service_name),
            "rate_per_thousand": self.clean_rate(self.rate_per_thousand),
            "minimum_quantity": self.clean_int(self.minimum_quantity),
            "maximum_quantity": self.clean_int(self.maximum_quantity),
            "average_time": self.clean_string(self.average_time),
            "category_service": self.category_service,
            "description": self.clean_string(self.description),
            "source": self.source
        }
    
    def clean_int(self, value):
        try:
            return int(re.sub(r'\D', '', str(value)))
        except ValueError:
            return 0
        
    def clean_rate(self, value):
        try:
            return float(re.sub(r'[^\d.]', '', str(value)))
        except ValueError:
            return 0.0
        
    def clean_string(self, input_string):
        return re.sub(r'[^\x00-\x7F]', '', input_string)
    
    def categorize_service(self, service_name: str) -> list:
        result = set()
        words = ["Instagram", "TikTok", "YouTube", "Facebook", "Twitter", "LinkedIn", "Snapchat", "Shopee", "Amazon", 
                 "Followers", "Likes", "Comments", "Shares", "Subscribers", "Video Views", "Live Stream Views", "Clicks"]
        for word in words:
            if re.search(rf"\b{re.escape(word)}\b", service_name, re.IGNORECASE):
                result.add(word)
        if not result:
            result.add("Other")
        return list(result)

