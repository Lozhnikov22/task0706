from django.urls import path
from rest_framework import views

from socialnet_api import views
from socialnet_api.views import add_like

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view()),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('posts/add-like/', add_like),
]
