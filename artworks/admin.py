from django.contrib import admin
from .models import Artwork, ArtworkImage, Adoption


class ArtworkImageInline(admin.StackedInline):
  model = ArtworkImage
  fields = ['image', 'url', 'license', 'caption']

class ArtworkAdmin(admin.ModelAdmin):
  list_display = ('title', 'artist_name')
  inlines = [ArtworkImageInline,]

admin.site.register(Artwork, ArtworkAdmin)


class AdoptionAdmin(admin.ModelAdmin):
  list_display = ('artwork', 'user')

admin.site.register(Adoption, AdoptionAdmin)
