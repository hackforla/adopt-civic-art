from django.contrib import admin
from .models import Artwork, ArtworkImage, Adoption, Checkin


class ArtworkImageInline(admin.StackedInline):
    model = ArtworkImage
    fields = ['image', 'url', 'license', 'caption']


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name')
    inlines = [ArtworkImageInline, ]

admin.site.register(Artwork, ArtworkAdmin)


class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'user', 'timestamp')

admin.site.register(Adoption, AdoptionAdmin)


class CheckinAdmin(admin.ModelAdmin):
    list_display = ('user', 'artwork', 'condition', 'damaged', 'damaged_description', 'timestamp')

admin.site.register(Checkin, CheckinAdmin)
