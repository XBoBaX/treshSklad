# Generated by Django 2.2.5 on 2019-10-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarehouseSpace', '0005_warehousespace_sectopal'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehousespace',
            name='secToPalZ',
            field=models.IntegerField(default=12, verbose_name='Секунд на загрузку 1 паллету'),
        ),
    ]