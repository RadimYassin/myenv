from django.urls import path
from .views import get_hotels

urlpatterns = [
    path('fetch-hotels/',get_hotels , name='fetch_hotels'),
]