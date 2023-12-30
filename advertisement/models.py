from django.db import models


# Create your models here.
class AdsType(models.Model):
    code = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ads_type'


class Advertisement(models.Model):
    type = models.ForeignKey(AdsType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='advertisement_images')

    def __str__(self):
        return str(self.type.title)

    class Meta:
        db_table = 'advertisement'
