# Generated by Django 3.2.5 on 2021-08-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_orderschedulemodel_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderschedulemodel',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]