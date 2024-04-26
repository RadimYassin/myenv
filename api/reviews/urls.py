from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.get_all_reviews, name='review-list'),
    path('reviews/create/', views.create_review, name='create-review'),
    path('reviews/<int:pk>/', views.get_review_detail, name='review-detail'),
    path('reviews/<int:pk>/update/', views.update_review, name='update-review'),
    path('reviews/<int:pk>/delete/', views.delete_review, name='delete-review'),
]
