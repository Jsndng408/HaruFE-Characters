from django.urls import path
from . import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # http://127.0.0.1:8000/blog/
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about') # http://127.0.0.1:8000/blog/about/
]