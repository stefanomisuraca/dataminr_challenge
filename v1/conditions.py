from .models import Subscriptions

def above(observers: Subscriptions.observers, api_target: int) -> bool:
    return api_target > observers.get("target")

def below(observers: Subscriptions.observers, api_target: int) -> bool:
    return api_target < observers.get("target")

def equal(observers: Subscriptions.observers, api_target: int) -> bool:
    return observers.get("target") == api_target

# Extend with more conditional functions

conditional_mapper = {"above": above, "below": below, "equal": equal}