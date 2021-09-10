# Generated by Django 3.2.5 on 2021-09-06 04:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deliverymanmodel',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
