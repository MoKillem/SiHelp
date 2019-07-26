from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserDetailView
from . import views

urlpatterns = [
    path('', views.homeroute, name='homeroute'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='ad-detail'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('post/new/', PostCreateView.as_view(), name='ad-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='ad-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='ad-delete'),
    path('post/<int:pk>/rate/', views.add_comment_to_post, name='add-comment-to-post'),
    path('marketplace/', views.marketplace, name='blog-marketplace'),
   

]

