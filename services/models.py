from django.db import models

# Create your models here.
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='services_img/', null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
