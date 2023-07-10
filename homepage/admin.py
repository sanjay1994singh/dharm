from django.contrib import admin

from homepage.models import LookupField,Gallery,Org,SangthanType,Sangthan,Post

# Register your models here.

admin.site.register(Org)
admin.site.register(LookupField)
admin.site.register(Gallery)
admin.site.register(SangthanType)
admin.site.register(Sangthan)
admin.site.register(Post)

