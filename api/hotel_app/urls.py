from django.urls import path
from .views import get_all_hotels, add_hotel_api_view, get_hotel_detail, update_hotel, delete_hotel

urlpatterns = [
    path('hotels/', get_all_hotels, name='hotel-list'),
    path('hotels/create/', add_hotel_api_view, name='hotel-create'),
    path('hotels/<int:pk>/', get_hotel_detail, name='hotel-detail'),
    path('hotels/<int:pk>/update/', update_hotel, name='hotel-update'),
    path('hotels/<int:pk>/delete/', delete_hotel, name='hotel-delete'),
]
