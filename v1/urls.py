"""Url dispatcher for v1 app."""
from django.urls import path, include
from v1 import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'subscriptions', api_views.SubscriptionsView, basename='subscriptions')
router.register(r'alerts', api_views.AlertsView, basename='alerts')

urlpatterns = [
    path(r'', include(router.urls))
]