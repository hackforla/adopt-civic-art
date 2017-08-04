from django.db import models
from django.contrib import admin
from .models import Artwork, ArtworkImage, Adoption, \
    Checkin, CheckinImage, CheckinDamage
from django.forms import CheckboxSelectMultiple


# Admin for artworks
class ArtworkImageInline(admin.StackedInline):
    model = ArtworkImage
    fields = ['image', 'url', 'license', 'caption']


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name')
    inlines = (ArtworkImageInline, )

admin.site.register(Artwork, ArtworkAdmin)


# Admin for adopted artworks
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'user', 'timestamp')
    readonly_fields = ('artwork', 'user', 'timestamp')

admin.site.register(Adoption, AdoptionAdmin)


# Admin for Check In Damage Descriptions
admin.site.register(CheckinDamage)


# Admin for Check-ins
class CheckinImageInline(admin.StackedInline):
    model = CheckinImage
    fields = ('image', )
    readonly_fields = ('image', )


class CheckinAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'condition', 'user', 'timestamp')
    readonly_fields = ('user', 'artwork', 'condition',
                       'damage', 'damaged_description', 'timestamp')
    inlines = (CheckinImageInline, )

    # Override ManyToManyField to use CheckboxSelectMultiple
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Checkin, CheckinAdmin)
