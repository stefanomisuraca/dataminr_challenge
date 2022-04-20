"""Url dispatcher for v1 app."""
from django.urls import path
from v1 import views as api_views

urlpatterns = [
    # path('products/', api_views.ProductView.as_view()),
    # path('products/<int:id>/', api_views.ProductViewDetail.as_view()),
    # path('products/<age>/', api_views.ProductViewAge.as_view())
    path('test/', api_views.TestView.as_view())
]