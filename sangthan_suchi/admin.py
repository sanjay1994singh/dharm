from django.contrib import admin
from .models import Pradesh, PradeshPadadhikari, DistrictPadadhikari, District, NagarPadadhikari, Nagar

# Register your models here.
admin.site.register(Pradesh)
admin.site.register(PradeshPadadhikari)
admin.site.register(District)

admin.site.register(DistrictPadadhikari)
admin.site.register(Nagar)
admin.site.register(NagarPadadhikari)
