#serializers.py - this file assigns an object-type model to each class from models.py, 
#defining fields contained within an object

from files.models import (
    User,
    PrefferedThemes,
    Genre,
    Attributes,
    BeerType,
    Brewery,
    Beer,
    BeerAttribute

)
from rest_framework import serializers


class PrefferedThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrefferedThemes
        fields = ("id", "name")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "password_hash",
            "login",
            "theme",
            "spotify_account"
        )

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "genre", "name")



class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ("id", "name")


class BeerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerType
        fields = ("id", "name")


class BrewerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        fields = ("id", "name", "location")


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ("id", "name", "line", "flavour", "price", "voltage", "brewery",
        "type")


class BeerAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerAttribute
        fields = ("id", "attribute", "beer")










