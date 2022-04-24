from time import sleep
from typing import Dict, List
from v1.conditions import above, below, equal
from v1.models import Alerts, Subscriptions
from .weather_wrapper import WeatherWrapper
from .conditions import conditional_mapper
import logging

logger = logging.getLogger("dataminr")

def polling_weather(*, subscription: Subscriptions) -> None:
    weather_api = WeatherWrapper()
    count = 0
    while result := weather_api.get_weather(location=subscription.location):  
        alert = Alerts(subscription=subscription)
        for obs in subscription.observers:
            condition = obs.get("condition")
            key = obs.get("key")
            conditional_callback = conditional_mapper.get(condition)
            result = alert.check_conditions(
                conditional_callback(obs, result.get("main").get(key))
            )
        count += 1
        yield (count, result)
        sleep(3)


def run_polling(*, subscription: Subscriptions) -> None:
    polling = polling_weather(subscription=subscription)
    for i in polling:
        logger.info(i)