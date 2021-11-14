from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('helloworld/', views.helloworld, name="post_helloworld"),
    path('seja_agua_amigo/', views.post_brucelee, name="post_brucelee"),
]