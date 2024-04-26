from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


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
    path('api/', include('attraction.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('ScrpingData.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)