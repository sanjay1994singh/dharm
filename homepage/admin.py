from django.contrib import admin

from .models import LookupField, Gallery, Org, SangthanType, Sangthan, Post, ImageFolder, ImageGallery


# Register your models here.

class SangthanAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'post', 'address', 'contact', 'id')
    search_fields = ('name', 'address', 'contact', 'id',)  # search bar
    list_filter = ('position', 'post')  # right sidebar filters
    ordering = ('id',)  # default order
    list_per_page = 20  # pagination

admin.site.register(ImageFolder)
admin.site.register(ImageGallery)
admin.site.register(Org)
admin.site.register(LookupField)
admin.site.register(Gallery)
admin.site.register(SangthanType)
admin.site.register(Sangthan, SangthanAdmin)
admin.site.register(Post)
