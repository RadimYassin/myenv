from django.urls import path
from . import views

urlpatterns = [
    path('offres/', views.get_all_offres, name='get_all_offres'),
    path('offres/create/', views.create_offre, name='create_offre'),
    path('offres/<int:pk>/', views.offre_detail, name='offre_detail'),
]
