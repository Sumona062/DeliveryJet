# Generated by Django 3.2.5 on 2021-08-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_orderschedulemodel_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderschedulemodel',
            name='postDate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]