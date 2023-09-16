from django.contrib import admin

from .models import JyotishSamadhan, Service, Rashi, DharmSandesh, DharmikAyojan, RajatShila, BrajYatra, \
    VastuUpay, HelpLine, BrajYatraDetails, Place, SixBox, AyojanEnquiry

# Register your models here.

admin.site.register(Service)
admin.site.register(Rashi)
admin.site.register(DharmSandesh)
admin.site.register(DharmikAyojan)
admin.site.register(RajatShila)
admin.site.register(BrajYatra)
admin.site.register(VastuUpay)
admin.site.register(HelpLine)
admin.site.register(BrajYatraDetails)
admin.site.register(JyotishSamadhan)
admin.site.register(Place)
admin.site.register(SixBox)
admin.site.register(AyojanEnquiry)
