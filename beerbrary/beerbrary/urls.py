from django.contrib import admin
from django.urls import path
import files.views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beers', get_beers),
    path('beer', get_beer),
]
