# Generated by Django 3.2.5 on 2021-08-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_orderschedulemodel_postdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderschedulemodel',
            name='is_marked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]