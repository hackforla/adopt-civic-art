from django.db import models
from django.contrib import admin

class Artwork(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    lat = models.FloatField(blank=False)
    lon = models.FloatField(blank=False)
    artist_name = models.CharField(max_length=200, blank=False)
    creation_date = models.DateField(blank=False)
    date_description = models.TextField(blank=True)
    artwork_type = models.TextField(blank=False)
    medium = models.CharField(max_length=200, blank=False)
    location_name = models.CharField(max_length=200, blank=False)
    street_1 = models.CharField(max_length=200, blank=True)
    street_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=False)
    zipcode = models.IntegerField(blank=False)
    date_entered = models.DateField(auto_now_add=True)

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name')

admin.site.register(Artwork, ArtworkAdmin)