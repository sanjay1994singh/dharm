from django.contrib import admin

from homepage.models import LookupField,Gallery,Org

# Register your models here.

admin.site.register(Org)
admin.site.register(LookupField)
admin.site.register(Gallery)

