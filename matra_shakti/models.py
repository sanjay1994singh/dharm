from django.db import models

# Create your models here.
from sangthan_suchi.models import Pradesh, District, Nagar


class MatraPradeshPadadhikari(models.Model):
    pradesh = models.ForeignKey(Pradesh, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    pad = models.CharField(max_length=256, null=True)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='pradesh_padadhikari_image')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'matra_pradesh_padadhikari'


class MatraDistrictPadadhikari(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    pad = models.CharField(max_length=256, null=True)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='district_padadhikari_image')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'matra_district_padadhikari'


class MatraNagarPadadhikari(models.Model):
    nagar = models.ForeignKey(Nagar, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    pad = models.CharField(max_length=256, null=True)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='nagar_padadhikari_image')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'matra_nagar_padadhikari'
