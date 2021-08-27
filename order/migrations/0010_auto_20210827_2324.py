# Generated by Django 3.2.5 on 2021-08-27 17:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_productmodel_availquantity'),
        ('order', '0009_alter_ordermodel_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderschedulemodel',
            name='postDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='ordermodel',
            unique_together={('buyer', 'product', 'status')},
        ),
    ]