from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login, name="login"),
    # path('logout/', views.logout, name="logout"),
    path('', views.signup_view, name="signup"),
    path('signup/', views.signup_view, name="signup"),
    
]