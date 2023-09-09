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

    def __str__(self):
        return self.title


class RajatShila(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='rajat_shila', null=True, blank=True)

    def __str__(self):
        return self.title


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
