from django.db import models
from datetime import datetime
from WarehouseSpace.models import WarehouseSpace
from traffic.models import Traffic
from unload.models import Unloader


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50, blank=True)
    optimumTemperature = models.IntegerField(verbose_name="Оптимальная температура товара", null=True, blank=True)
    shelfLife = models.DateTimeField(verbose_name="Срок годности до", null=True, blank=True)
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата загрузки")
    dateUnUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата разгрузки")
    sklad = models.ForeignKey(WarehouseSpace, on_delete=models.CASCADE, null=True, verbose_name="Склад")
    traffic = models.ForeignKey(Traffic, on_delete=models.CASCADE, null=True, verbose_name="Грузопоток")
    Unloader = models.ForeignKey(Unloader, on_delete=models.CASCADE, null=True, verbose_name="Грузопоток разгрузки")
    countPallet = models.IntegerField(verbose_name="Количество паллет", null=True, blank=True)
    height = models.IntegerField(default=1500, verbose_name="Высота паллета", null=True, blank=True)
    categories = (
        ("Сухие товары", "Сухие товары"),
        ("Скоропортящиеся товары", "Скоропортящиеся товары"),
        ("Хрупкие товары", "Хрупкие товары"),
    )
    categories2 = (
        ("Отправлен", "Отправлен"),
        ("В обработке", "В обработке"),
        ("Принят", "Принят"),
        ("Отменен", "Отменен"),
        ("Загрузка", "Загрузка"),
    )
    typeProduct = models.CharField(
        default="Сухие товары",
        max_length=30,
        verbose_name="Тип продукта",
        choices=categories
    )
    status = models.CharField(
        default="Отправлен",
        max_length=30,
        verbose_name="Статус",
        choices=categories2
    )

    def __str__(self):
        return "{0}_{1}".format(self.name, self.dateUpload)

    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукт"


