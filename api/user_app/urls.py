from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # URL for logging out
    path('test/', views.user_detail, name='test'),  # URL for logging out

    path('users/', views.get_all_users, name='get_all_users'),  # URL for getting all users
    path('users/<int:pk>/', views.update_user, name='update_user'),
    path('<int:pk>/', views.delete_user, name='delete_user'),
]