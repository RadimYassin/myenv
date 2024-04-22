from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_app.urls')),
    path('api/', include('destination_app.urls')),
    path('api/', include('restaurant.urls')),
    path('api/', include('Transport.urls')),
    path('api/', include('hotel_app.urls')),
    path('api/', include('Event.urls')),
    path('api/', include('chat_app.urls')),
    path('api/', include('offer.urls')),
    path('api/', include('ScrpingData.urls')),
]
