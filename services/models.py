from django.db import models


# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='services_img/', null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Rashi(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='rashi_image', null=True, blank=True)

    def __str__(self):
        return self.title


class DharmSandesh(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='dharm_sandesh_image', null=True, blank=True)
    video_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class DharmikAyojan(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='dharmik_ayojan', null=True, blank=True)
    video_link = models.TextField(null=True, blank=True)
    money = models.IntegerField(null=True, default=0, blank=True)

    def __str__(self):
        return self.title


class RajatShila(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='rajat_shila', null=True, blank=True)

    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class BrajYatraDetails(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    temple_name = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='braj_yatra', null=True, blank=True)

    def __str__(self):
        return self.temple_name


class BrajYatra(models.Model):
    temple_name = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='braj_yatra', null=True, blank=True)

    def __str__(self):
        return self.temple_name


class VastuUpay(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='vastu_upay', null=True, blank=True)

    def __str__(self):
        return self.title


class HelpLine(models.Model):
    place = models.CharField(max_length=1000, null=True, blank=True)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.place


class TvLink(models.Model):
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.desc


class JyotishSamadhan(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    dob_place = models.TextField(null=True, blank=True)
    dob_time = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=12, null=True, blank=True)
    question = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SixBox(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='six_box_image', null=True, blank=True)

    def __str__(self):
        return self.title

