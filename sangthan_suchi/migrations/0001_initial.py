# Generated by Django 3.2.20 on 2023-12-23 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='district_image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='Nagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='nagar_image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sangthan_suchi.district')),
            ],
            options={
                'db_table': 'nagar',
            },
        ),
        migrations.CreateModel(
            name='Pradesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pradesh_image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pradesh',
            },
        ),
        migrations.CreateModel(
            name='PradeshPadadhikari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('pad', models.CharField(max_length=256, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(upload_to='pradesh_padadhikari_image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('pradesh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sangthan_suchi.pradesh')),
            ],
            options={
                'db_table': 'pradesh_padadhikari',
            },
        ),
        migrations.CreateModel(
            name='NagarPadadhikari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('pad', models.CharField(max_length=256, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(upload_to='nagar_padadhikari_image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('nagar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sangthan_suchi.nagar')),
            ],
            options={
                'db_table': 'nagar_padadhikari',
            },
        ),
        migrations.CreateModel(
            name='DistrictPadadhikari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('pad', models.CharField(max_length=256, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.ImageField(upload_to='district_padadhikari_image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sangthan_suchi.district')),
            ],
            options={
                'db_table': 'district_padadhikari',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='pradesh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sangthan_suchi.pradesh'),
        ),
    ]