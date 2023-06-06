from django.db import models

# Create your models here.
class EnquiryDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.message