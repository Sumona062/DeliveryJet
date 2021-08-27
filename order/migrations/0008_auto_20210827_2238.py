# Generated by Django 3.2.5 on 2021-08-27 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_productmodel_availquantity'),
        ('order', '0007_alter_orderschedulemodel_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='not checkout', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='ordermodel',
            unique_together={('buyer', 'product', 'status')},
        ),
    ]
