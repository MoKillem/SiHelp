from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('marketplace/', views.marketplace, name='blog-marketplace'),
    path('layout/', views.layout, name='blog-layout'),
    path('signuptutor/', views.SignUpTutor, name='blog-SignUp'),
    path('signupNt/', views.SignUpNt, name='blog-SignUp'),
    path('account/', views.Account, name='blog-Account'),
    path('entry/', views.Entry, name='blog-Entry'),
    path('profilepage/', views.ProfilePage, name='blog-ProfilePage'),

]

