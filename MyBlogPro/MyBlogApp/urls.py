from django.urls import path
from . import views

urlpatterns = [
    # Blog URLs
    path('', views.BlogView.as_view()),
    path('blogs/', views.BlogView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    # Comment URLs
    path('comments/', views.CommentView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]
