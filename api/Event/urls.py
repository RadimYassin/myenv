from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.get_all_events, name='event-list'),
    path('events/create/', views.create_event, name='event-create'),
    path('events/<int:pk>/', views.event_detail, name='event-detail'),
]