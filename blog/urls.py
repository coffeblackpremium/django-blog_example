from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/comandosbasicoparalinux', views.linux_basico, name="post_linux_basico"),
    path('post/sejacomoaagua', views.post_brucelee, name="post_brucelee"),
]