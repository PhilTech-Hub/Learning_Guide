"""Defines URL patterns for users"""

from django.urls import path, include
from . import views

app_name = "Users"
urlpatterns = [
    # Include default auth urls.
    path("", include("django.contrib.auth.urls")),
    
    # Registration page.
    path('register/', views.register, name='register'),
    
    path('login/', views.login, name='login'),
    
]