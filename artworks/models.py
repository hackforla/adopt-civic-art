from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class ArtworkImage(models.Model):
    artwork = models.ForeignKey('Artwork')
    image = models.ImageField(
        upload_to='artworks/',
        blank=True,
        help_text='Image file upload size limit is 2.5MB.'
    )
    url = models.CharField(max_length=200, blank=False)
    license = models.CharField(max_length=200, blank=True)
    caption = models.CharField(max_length=200, blank=True)


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
    date_entered = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.title


class Adoption(models.Model):
    user = models.ForeignKey(User)
    artwork = models.ForeignKey('Artwork')
    timestamp = models.DateTimeField(auto_now_add=True)


class CheckinImage(models.Model):
    checkin = models.ForeignKey('Checkin')
    image = models.ImageField(upload_to='checkins/', blank=False)


class Checkin(models.Model):
    user = models.ForeignKey(User)
    artwork = models.ForeignKey('Artwork')
    condition = models.CharField(
        max_length=200, blank=False, choices=[
            ('C', 'Chipping or cracking'),
            ('D', 'Dirt, dust, bird droppings, or spiderwebs'),
            ('G', 'Graffiti or vandalism'),
            ('R', 'Corrosion'),
        ])
    damaged = models.BooleanField(blank=False)
    damaged_description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
