from django.db import models

# Create your models here.
class LookupField(models.Model):
    code  = models.CharField(max_length=100)
    title  = models.CharField(max_length=1000)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='lookup_img/', null=True)
    pdf = models.FileField(upload_to='pdf', default=None,null=True)

    def __str__(self):
        return self.code
    
class Gallery(models.Model):
    code  = models.CharField(max_length=100)
    title  = models.CharField(max_length=1000)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='lookup_img/', null=True)

    def __str__(self):
        return self.title
    
class Org(models.Model):
    title  = models.CharField(max_length=1000)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
