from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.get_all_restaurants, name='get_all_restaurants'),
    path('restaurants/create/', views.create_restaurant, name='create_restaurant'),
    path('restaurants/<int:pk>/', views.get_restaurant_detail, name='get_restaurant_detail'),
    path('restaurants/<int:pk>/update/', views.update_restaurant, name='update_restaurant'),
    path('restaurants/<int:pk>/delete/', views.delete_restaurant, name='delete_restaurant'),
]
