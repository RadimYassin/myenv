# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('transports/', views.get_all_transports, name='get_all_transports'),
    path('transports/create/', views.create_transport, name='create_transport'),
    path('transports/<int:pk>/', views.get_transport_detail, name='get_transport_detail'),
    path('transports/<int:pk>/update/', views.update_transport, name='update_transport'),
    path('transports/<int:pk>/delete/', views.delete_transport, name='delete_transport'),
]
