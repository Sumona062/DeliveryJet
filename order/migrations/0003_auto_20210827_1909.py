# Generated by Django 3.2.5 on 2021-08-27 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderschedulemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderschedulemodel',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.ordermodel'),
        ),
        migrations.AlterUniqueTogether(
            name='orderschedulemodel',
            unique_together=set(),
        ),
    ]