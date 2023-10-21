from django.contrib import admin

from .models import LookupField, Gallery, Org, SangthanType, Sangthan, Post, ImageFolder, ImageGallery

# Register your models here.

admin.site.register(ImageFolder)
admin.site.register(ImageGallery)
admin.site.register(Org)
admin.site.register(LookupField)
admin.site.register(Gallery)
admin.site.register(SangthanType)
admin.site.register(Sangthan)
admin.site.register(Post)
