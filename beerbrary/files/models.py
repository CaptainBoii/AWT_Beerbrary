from django.db import models

class PrefferedThemes(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    theme_id = models.ForeignKey(PrefferedThemes, on_delete=models.CASCADE)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    spotify_account = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Attributes(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class BeerType(models.Model):
    name = models.CharField(max_length=100)

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Beer(models.Model):
    name = models.CharField(max_length=100)
    line =  models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    price = models.FloatField()
    brewery_id = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    type_id = models.ForeignKey(BeerType, on_delete=models.CASCADE)

class BeerAttribute(models.Model):
    attribute_id = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    beer_id = models.ForeignKey(Beer, on_delete=models.CASCADE)