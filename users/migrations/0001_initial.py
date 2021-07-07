# Generated by Django 3.2.5 on 2021-07-06 18:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_buyer', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('is_DeliveryMan', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressPhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('thana', models.CharField(blank=True, max_length=100, null=True)),
                ('areaName', models.CharField(blank=True, max_length=100, null=True)),
                ('holdingNo', models.CharField(blank=True, max_length=100, null=True)),
                ('postOffice', models.CharField(blank=True, max_length=100, null=True)),
                ('additonal', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, choices=[('9am-12pm', '9am-12pm'), ('12pm-3pm', '12pm-3pm'), ('3pm-6pm', '3pm-6pm'), ('6pm-9pm', '6pm-9pm')], max_length=255, null=True)),
                ('Day', models.CharField(blank=True, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('refill', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreferredAreaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryManModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('Drug store', 'Drug store'), ('Home Appliances Store', 'Home Appliances Store'), ('Electronic Store', 'Electronic Store'), ('Food marts', 'Food marts'), ('Fashion house', 'Fashion house'), ('Sports hub', 'Sports hub'), ('Lifestyle store', 'Lifestyle store'), ('Mom and kids', 'Mom and kids'), ('Cosmetics House', 'Cosmetics House'), ('book store', 'book store')], max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AvailabilityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.addressphonemodel')),
                ('slot_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.timeslotmodel')),
            ],
        ),
    ]