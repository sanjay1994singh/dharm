from django.db import models


# Create your models here.
class LookupField(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='lookup_img/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', default=None, null=True, blank=True)

    def __str__(self):
        return self.code


class ImageFolder(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_folder/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'image_folder'


class ImageGallery(models.Model):
    image_folder = models.ForeignKey(ImageFolder, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='lookup_img/', null=True)


class Gallery(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='lookup_img/', null=True)

    def __str__(self):
        return self.title


class Org(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class SangthanType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Post(models.Model):
    type = models.ForeignKey(SangthanType, on_delete=models.CASCADE, null=True, default=1)
    post_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.post_name


class Sangthan(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='sangthan_image')
    position = models.IntegerField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=1)
    address = models.TextField()
    contact = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
