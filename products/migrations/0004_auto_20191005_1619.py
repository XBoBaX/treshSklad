# Generated by Django 2.2.5 on 2019-10-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190921_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Отправлен', 'Отправлен'), ('В обработке', 'В обработке'), ('Принят', 'Принят'), ('Отменен', 'Отменен')], default='Отправлен', max_length=30, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='product',
            name='typeProduct',
            field=models.CharField(choices=[('Сухие товары', 'Сухие товары'), ('Скоропортящиеся товары', 'Скоропортящиеся товары'), ('Хрупкие товары', 'Хрупкие товары')], default='Сухие товары', max_length=30, verbose_name='Тип продукта'),
        ),
    ]