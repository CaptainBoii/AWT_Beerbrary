from django.db import models

class PrefferedThemes(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    theme = models.ForeignKey(PrefferedThemes, on_delete=models.CASCADE)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    spotify_account = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Attributes(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
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
    voltage = models.FloatField()
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    beertype = models.ForeignKey(BeerType, on_delete=models.CASCADE)

class BeerAttribute(models.Model):
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)