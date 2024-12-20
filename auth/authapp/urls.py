from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    # Other URLs like home, logout, etc.
]
