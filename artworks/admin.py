from django.contrib import admin
from .models import Artwork, ArtworkImage, Adoption, Checkin, CheckinImage


#  Admin for artworks
class ArtworkImageInline(admin.StackedInline):
    model = ArtworkImage
    fields = ['image', 'url', 'license', 'caption']


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name')
    inlines = [ArtworkImageInline, ]

admin.site.register(Artwork, ArtworkAdmin)


# Admin for adopted artworks
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'user', 'timestamp')

admin.site.register(Adoption, AdoptionAdmin)


# Admin for Check-ins
class CheckinImageInline(admin.StackedInline):
    model = CheckinImage
    fields = ['image', ]


class CheckinAdmin(admin.ModelAdmin):
    list_display = ('user', 'artwork', 'condition',
                    'damaged', 'damaged_description', 'timestamp')
    inlines = [CheckinImageInline, ]

admin.site.register(Checkin, CheckinAdmin)
