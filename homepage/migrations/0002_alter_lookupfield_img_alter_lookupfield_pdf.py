# Generated by Django 4.2.11 on 2024-05-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lookupfield',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='lookup_img/'),
        ),
        migrations.AlterField(
            model_name='lookupfield',
            name='pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='pdf'),
        ),
    ]
