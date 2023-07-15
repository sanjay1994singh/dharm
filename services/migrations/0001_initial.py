# Generated by Django 3.2.19 on 2023-06-03 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='services_img/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]