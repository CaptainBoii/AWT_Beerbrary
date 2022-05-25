import imp
import json
import datetime
from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from files.serializers import (
    PrefferedThemesSerializer,
    UserSerializer,
    GenreSerializer,
    AttributesSerializer,
    BeerTypeSerializer,
    BrewerySerializer,
    BeerSerializer,
    BeerAttributeSerializer
)

from files.models import (
    PrefferedThemes,
    User,
    Genre,
    Attributes,
    BeerType,
    Brewery,
    Beer,
    BeerAttribute
)


class PrefferedThemesViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PrefferedThemesSerializer
    queryset = PrefferedThemes.objects.all()

class UserViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class GenreViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class AttributesViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = AttributesSerializer
    queryset = Attributes.objects.all()

class BeerTypeViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = BeerTypeSerializer
    queryset = BeerType.objects.all()

class BreweryViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = BrewerySerializer
    queryset = Brewery.objects.all()

class BeerViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = BeerSerializer
    queryset = Beer.objects.all()

class BeerAttributeViewSet(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = BeerAttributeSerializer
    queryset = BeerAttribute.objects.all()

def change_theme(request):
    response_data = {}
    request_data = decode(request)
    user_id = request_data['user_id']
    new_theme = request_data['theme']
    user = User.objects.get(id=user_id)
    user.theme = PrefferedThemes.objects.get(id=new_theme)
    user.save()
    return JsonResponse({"status": "ok"})

def get_beer(request):
    response_data = {}
    request_data = decode(request)
    beer_id = request_data['beer']
    beer = Beer.objects.get(id = beer_id)
    response_data.__setitem__("id", beer.id)
    response_data.__setitem__("name", beer.name)
    response_data.__setitem__("line", beer.line)
    response_data.__setitem__("flavour", beer.flavour)
    response_data.__setitem__("price", beer.price)
    response_data.__setitem__("brewery", beer.brewery.name)
    response_data.__setitem__("brewery_id", beer.brewery.id)
    response_data.__setitem__("voltage", beer.voltage)
    response_data.__setitem__("type_id", beer.beertype.id)
    response_data.__setitem__("type", beer.beertype.name)
    return HttpResponse(json.dumps(response_data))

def get_beers(request):
    response_data = {}
    for beer in Beer.objects.raw('SELECT * FROM files_beer'):
        response_data.__setitem__(beer.id, {"name": beer.name, "line": beer.line, "flavour": beer.flavour, "price": beer.price,
            "voltage": beer.voltage, "brewery": beer.brewery.name, "brewery_id": beer.brewery.id, "type_id": beer.beertype.id, "type": beer.beertype.name})
    return HttpResponse(json.dumps(response_data))

def register_user(request):
    response_data = {}
    request_data = decode(request)
    username = request_data['username']
    password = request_data['password']
    login = request_data['login']
    password_duplicate = False
    name_duplicate = False
    login_duplicate = False
    for user in User.objects.raw('SELECT * FROM files_user'):
        if user.name == username:
            name_duplicate = True
        if user.password == password:
            password_duplicate = True
        if user.login == login:
            login_duplicate = True
    if not password_duplicate and not login_duplicate and not name_duplicate:
        user = User()
        user.name = username
        user.login = login
        user.password = password
        user.theme_id = PrefferedThemes.objects.get(id=1)
        user.save()
        return JsonResponse({"status": "ok"})
    else:
        response_data.__setitem__("login", login_duplicate)
        response_data.__setitem__("username", name_duplicate)
        response_data.__setitem__("password", password_duplicate)
        return HttpResponse(json.dumps(response_data))

def login(request):
    response_data = {}
    request_data = decode(request)
    login = request_data['login']
    password = request_data['password']
    login_not_found = True
    for user in User.objects.raw('SELECT * FROM files_user'):
        if user.login == login:
            if user.password == password:
                return JsonResponse({"status": "ok"})
            else:
                return JsonResponse({"status": "password_mismatch"})
    return JsonResponse({"status": "login_not_found"})

def decode(request):
    temp = request.body.decode().split("&")
    result = {}
    for i in temp:
        t1 = i.split("=")
        result.__setitem__(t1[0], t1[1])
    return result
    
