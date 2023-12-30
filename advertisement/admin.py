from django.contrib import admin
from .models import Advertisement, AdsType

# Register your models here.
admin.site.register(AdsType)
admin.site.register(Advertisement)
