from django.db import models


# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.type


class Karykram(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
