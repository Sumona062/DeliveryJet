# Generated by Django 3.2.5 on 2021-08-02 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210802_1207'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='availabilitymodel',
            unique_together={('buyer', 'slot_id', 'address')},
        ),
    ]