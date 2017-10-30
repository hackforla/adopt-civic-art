from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class AboutPage(models.Model):
    first_row_header = models.CharField(max_length=200, blank=True)
    first_row_text = models.TextField(blank=True)
    second_row_header = models.CharField(max_length=200, blank=True)
    second_row_column_one_header = models.CharField(max_length=200, blank=True)
    second_row_column_one_text = models.TextField(blank=True)
    second_row_column_two_header = models.CharField(max_length=200, blank=True)
    second_row_column_two_text = models.TextField(blank=True)
    second_row_column_three_header = \
        models.CharField(max_length=200, blank=True)
    second_row_column_three_text = models.TextField(blank=True)
    call_to_action_text = models.TextField(blank=True)
    call_to_action_button = models.CharField(max_length=200, blank=True)
    call_to_action_link = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'About Page'

    def __str__(self):
        return 'About Page'


class ArtworkImage(models.Model):
    artwork = models.ForeignKey('Artwork')
    image = models.ImageField(
        upload_to='artworks/',
        blank=False,
        help_text='Image file upload size limit is 2.5MB.'
    )
    url = models.CharField(max_length=200, blank=True)
    license = models.CharField(max_length=200, blank=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artwork.title


class ArtworkType(models.Model):
    artwork_type = models.CharField(max_length=200)

    class Meta:
        ordering = ['artwork_type']
        verbose_name = 'Artwork Type'
        verbose_name_plural = 'Artwork Type List'

    def __str__(self):
        return self.artwork_type


class ArtworkMedium(models.Model):
    medium = models.CharField(max_length=200)

    class Meta:
        ordering = ['medium']
        verbose_name = 'Artwork Medium'
        verbose_name_plural = 'Artwork Medium List'

    def __str__(self):
        return self.medium


class Artwork(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    lat = models.FloatField(blank=False)
    lon = models.FloatField(blank=False)
    artist_name = models.CharField(max_length=200, blank=False)
    creation_date = models.IntegerField(
        blank=False,
        help_text='Enter a year in YYYY format, like 1978 or 2017',
        null=True)
    date_description = models.TextField(blank=True)
    show_date_description = models.BooleanField(
        default=False,
        blank=False,
        help_text='Checking this will show the date description \
        instead of creation date on the artwork page')
    artwork_type = models.ManyToManyField(ArtworkType)
    medium = models.ManyToManyField(ArtworkMedium)
    location_name = models.CharField(max_length=200, blank=False)
    street_1 = models.CharField(max_length=200, blank=True)
    street_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=False)
    zipcode = models.IntegerField(blank=False)
    date_entered = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.title


class Adoption(models.Model):
    user = models.ForeignKey(User)
    artwork = models.ForeignKey('Artwork')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artwork.title


class CheckinImage(models.Model):
    checkin = models.ForeignKey('Checkin')
    image = models.ImageField(upload_to='checkins/', blank=False)


class CheckinDamage(models.Model):
    damage = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Check In Damage Description'

    def __str__(self):
        return self.damage


class Checkin(models.Model):
    user = models.ForeignKey(User)
    artwork = models.ForeignKey('Artwork')
    condition = models.CharField(
        max_length=100, blank=False, choices=[
            ('G', 'Good Condition'),
            ('D', 'Damaged'),
        ])
    damage = models.ManyToManyField(CheckinDamage)
    damaged_description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Check In'

    def __str__(self):
        return self.artwork.title
