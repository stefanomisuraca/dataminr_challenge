from .models import Subscriptions

def above(observer: Subscriptions.observer, api_target: int) -> bool:
    return observer.get("target") > api_target

def below(observer: Subscriptions.observer, api_target: int) -> bool:
    return observer.get("target") < api_target

def equal(observer: Subscriptions.observer, api_target: int) -> bool:
    return observer.get("target") == api_target

# Extend with more conditional functions

conditional_mapper = {"above": above, "below": below, "equal": equal}