# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.get_all_events, name='get_all_events'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:pk>/', views.get_event_detail, name='get_event_detail'),
    path('events/<int:pk>/update/', views.update_event, name='update_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),
]
