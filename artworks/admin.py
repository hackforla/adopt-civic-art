from django.contrib import admin
from .models import Artwork, ArtworkImage


class ArtworkImageInline(admin.StackedInline):
  model = ArtworkImage
  fields = ['image', 'author', 'url', 'license', 'caption']

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name')
    inlines = [ArtworkImageInline,]

admin.site.register(Artwork, ArtworkAdmin)
