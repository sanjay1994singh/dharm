from django.contrib import admin
from .models import EnquiryDetails,Gender,MemberType,CustomUser
# Register your models here.
admin.site.register(EnquiryDetails)
admin.site.register(Gender)
admin.site.register(MemberType)
admin.site.register(CustomUser)
