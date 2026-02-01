from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from shortener import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[

    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_url, name='create'),
    path('edit/<int:id>/', views.edit_url, name='edit'),
    path('delete/<int:id>/', views.delete_url, name='delete'),
    path('register/', views.register, name='register'),
    path('<str:code>/', views.redirect_url, name='redirect'),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)