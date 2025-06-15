from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin_login/', views.accueil_admin, name = 'admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
]