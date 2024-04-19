from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.get_all_restaurants, name='get_all_restaurants'),
    path('restaurants/create/', views.create_restaurant, name='create_restaurant'),
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
]
