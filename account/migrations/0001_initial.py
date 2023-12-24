# Generated by Django 3.2.20 on 2023-12-23 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dob', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_image')),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(default='India', max_length=10)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('id_number', models.CharField(blank=True, max_length=30, null=True)),
                ('order_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('transaction_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('payment_status', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.gender')),
                ('member_type', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='account.membertype')),
            ],
        ),
    ]
