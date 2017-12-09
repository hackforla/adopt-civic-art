from django.db import models
from django.contrib import admin
from django.conf import settings
from django.core import urlresolvers

from .models import AboutPage, Artwork, ArtworkImage, ArtworkType, \
    ArtworkMedium, Adoption, Tip, Checkin, CheckinImage, CheckinDamage
from django.forms import CheckboxSelectMultiple
from django.utils.safestring import mark_safe


admin.site.site_header = 'ArtWatcher Administration'

# Admin for about page fields
admin.site.register(AboutPage)


# Admin for artworks
class ArtworkImageInline(admin.StackedInline):
    model = ArtworkImage
    fields = ['image_preview', 'image', 'url', 'license', 'caption']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return mark_safe(
            """<img src="%s%s" style="max-width: 800px" />"""
            % (settings.MEDIA_URL, obj.image))


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name')
    inlines = (ArtworkImageInline,)

admin.site.register(Artwork, ArtworkAdmin)


# Admin for artwork type and medium lists
admin.site.register(ArtworkType)
admin.site.register(ArtworkMedium)


# Admin for adopted artworks
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'user', 'timestamp')
    readonly_fields = ('artwork', 'user', 'timestamp')

admin.site.register(Adoption, AdoptionAdmin)


# Admin for Check In Damage Descriptions
class CheckInPhotoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'status', 'timestamp', 'image_preview')
    readonly_fields = ('checkin', 'link', 'image', 'timestamp', 'image_preview')
    list_filter = ('status',)

    def link(self, obj):
        link = urlresolvers.reverse("admin:artworks_checkin_change", args=[obj.checkin.id])

        return '<a href="' + link + '">' + obj.checkin.artwork.title + ' Check In</a>'

    link.allow_tags = True

    def image_preview(self, obj):
        return mark_safe(
            """<img src="%s%s" style="max-width: 800px" />"""
            % (settings.MEDIA_URL, obj.image))


admin.site.register(CheckinImage, CheckInPhotoAdmin)


# Admin for Check-ins
class CheckinImageInline(admin.StackedInline):
    model = CheckinImage
    fields = ('image_preview', 'image')
    readonly_fields = ('image_preview', 'image')

    def image_preview(self, obj):
        return mark_safe(
            """<img src="%s%s" style="max-width: 800px" />"""
            % (settings.MEDIA_URL, obj.image))


class CheckinAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'condition', 'user', 'timestamp')
    readonly_fields = ('user', 'artwork', 'condition',
                       'damage', 'damaged_description', 'timestamp')
    inlines = (CheckinImageInline,)

    # Override ManyToManyField to use CheckboxSelectMultiple
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Checkin, CheckinAdmin)


class TipAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'condition', 'timestamp')
    readonly_fields = ('artwork', 'condition', 'timestamp')


admin.site.register(Tip, TipAdmin)
