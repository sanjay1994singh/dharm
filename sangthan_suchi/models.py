from django.db import models


# Create your models here.
class Pradesh(models.Model):
    name = models.CharField(max_length=256, null=True)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pradesh_image', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pradesh'


class District(models.Model):
    pradesh = models.ForeignKey(Pradesh, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='district_image', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'district'


class Nagar(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=True)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='nagar_image', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'nagar'


class PradeshPadadhikari(models.Model):
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
        db_table = 'pradesh_padadhikari'


class DistrictPadadhikari(models.Model):
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
        db_table = 'district_padadhikari'


class NagarPadadhikari(models.Model):
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
        db_table = 'nagar_padadhikari'
