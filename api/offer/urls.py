from django.urls import path
from . import views

urlpatterns = [
    path('offres/', views.get_all_offres, name='get_all_offres'),
    path('offres/create/', views.create_offre, name='create_offre'),
    path('offres/<int:pk>/', views.get_offre_detail, name='get_offre_detail'),
    path('offres/<int:pk>/update/', views.update_offre, name='update_offre'),
    path('offres/<int:pk>/delete/', views.delete_offre, name='delete_offre'),
]
