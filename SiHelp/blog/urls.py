from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='ad-detail'),
    path('post/new/', PostCreateView.as_view(), name='ad-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='ad-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='ad-delete'),
    path('about/', views.about, name='blog-about'),
    path('marketplace/', views.marketplace, name='blog-marketplace'),
    path('layout/', views.layout, name='blog-layout'),
    path('signuptutor/', views.SignUpTutor, name='blog-SignUp'),
    path('signupNt/', views.SignUpNt, name='blog-SignUp'),
    path('account/', views.Account, name='blog-Account'),
    path('entry/', views.Entry, name='blog-Entry'),
    path('profilepage/', views.ProfilePage, name='blog-ProfilePage'),

]

