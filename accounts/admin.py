from django.contrib import admin

from accounts.models import EnquiryDetails,CustomUser

# Register your models here.
admin.site.register(EnquiryDetails)
admin.site.register(CustomUser)
