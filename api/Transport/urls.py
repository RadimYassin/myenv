from django.urls import path
from .views import get_all_transports, create_transport, transport_detail

urlpatterns = [
    path('transports/', get_all_transports, name='get_all_transports'),
    path('transports/create/', create_transport, name='create_transport'),
    path('transports/<int:pk>/', transport_detail, name='transport_detail'),
]
