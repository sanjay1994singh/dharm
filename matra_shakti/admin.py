from django.contrib import admin
from .models import MatraNagarPadadhikari, MatraPradeshPadadhikari, MatraDistrictPadadhikari

# Register your models here.
admin.site.register(MatraNagarPadadhikari)
admin.site.register(MatraPradeshPadadhikari)
admin.site.register(MatraDistrictPadadhikari)
