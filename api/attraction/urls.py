from django.urls import path
from . import views

urlpatterns = [
    path('attractions/', views.get_all_attractions, name='attraction-list'),
    path('attractions/create/', views.create_attraction, name='attraction-create'),
    path('attractions/<int:pk>/', views.get_attraction_detail, name='attraction-detail'),
    path('attractions/<int:pk>/update/', views.update_attraction, name='attraction-update'),
    path('attractions/<int:pk>/delete/', views.delete_attraction, name='attraction-delete'),
]
