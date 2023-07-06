from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class EnquiryDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.message
    
class MemberType(models.Model):
    type = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.type

class Gender(models.Model):
    gender = models.CharField(max_length=50, null=True,blank=True)

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100,null=True,blank=True,unique=True)
    mobile = models.CharField(max_length=15, null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    dob = models.CharField(max_length=20,null=True,blank=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_image',null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    id_number = models.CharField(max_length=30,null=True,blank=True)
    member_type = models.ForeignKey(MemberType,on_delete=models.CASCADE,null=True,blank=True,default='')

    def __str__(self):
        return self.fullname
    
class SangthanSuchi(models.Model):
    pass


