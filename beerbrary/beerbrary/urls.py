from django.contrib import admin
from django.urls import path
from files.views import get_beer, get_beers, change_theme, register_user, login
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beers', get_beers),
    path('beer', get_beer),
    path('change_theme', change_theme),
    path('register', register_user),
    path('login', login),
]
