from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.get_all_destinations, name='destination-list'),
    path('destinations/create/', views.create_destination, name='destination-create'),
    path('destinations/<int:pk>/', views.destination_detail, name='destination-detail'),
]
