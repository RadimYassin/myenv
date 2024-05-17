from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.destination_list_with_events, name='get_all_destinations'),
    path('destinations/create/', views.create_destination, name='create_destination'),
    path('destinations/<int:pk>/', views.get_destination_detail, name='get_destination_detail'),
    path('destinations/<int:pk>/update/', views.update_destination, name='update_destination'),
    path('destinations/<int:pk>/delete/', views.delete_destination, name='delete_destination'),
]
