from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from shortener import views

urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_url, name='create'),
    path('edit/<int:id>/', views.edit_url, name='edit'),
    path('delete/<int:id>/', views.delete_url, name='delete'),
    path('register/', views.register, name='register'),
    path('<str:code>/', views.redirect_url, name='redirect'),
   

]