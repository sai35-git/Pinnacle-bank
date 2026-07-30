from django.contrib import admin
from django.urls import path
from accounts import views  # Imports views from your accounts app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                     # Main page
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard page
]