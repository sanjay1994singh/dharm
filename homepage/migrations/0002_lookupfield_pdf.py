# Generated by Django 3.2.19 on 2023-06-23 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookupfield',
            name='pdf',
            field=models.FileField(default=None, null=True, upload_to='pdf'),
        ),
    ]
