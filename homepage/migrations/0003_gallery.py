# Generated by Django 3.2.19 on 2023-06-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_lookupfield_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('img', models.ImageField(null=True, upload_to='lookup_img/')),
            ],
        ),
    ]
