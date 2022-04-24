import os
from typing import Dict
from django.conf import settings
import requests
import logging
logger = logging.getLogger("dataminr")

class WeatherWrapper:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPEN_WEATHER_KEY")
        self.api_url = settings.OPEN_WEATHER_API.get("url")
        
    def get_weather(self, *, location:str) -> Dict[str, int]:

        api_endpoint = f"{self.api_url}?q={location}&APPID={self.api_key}&units=metric"
        try:
            result = requests.get(api_endpoint, timeout=5)
            if result.status_code == 404:
                logger.info("Location not found")
                return False
            return result.json()
        except requests.Timeout as e:
            logger.error(e)
