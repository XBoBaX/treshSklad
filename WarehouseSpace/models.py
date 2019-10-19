from django.db import models
from shelving.models import Shelving


class WarehouseSpace(models.Model):
    name = models.CharField(verbose_name="Название склада", max_length=30, blank=True)
    height = models.IntegerField(verbose_name="Размеры помещения (высота)", null=True, blank=True)
    size = models.IntegerField(verbose_name="Площадь помещения", null=True, blank=True)
    optimumTemperature = models.IntegerField(verbose_name="Температура склада", null=True, blank=True)
    shelving = models.ForeignKey(Shelving, on_delete=models.CASCADE, null=True, verbose_name="Стеллажи")
    count = models.IntegerField(verbose_name="Кол-во стеллажей", null=True, blank=True)
    secToPal = models.IntegerField(verbose_name="Секунд на разгрузку 1 паллету", default=12)
    secToPalZ = models.IntegerField(verbose_name="Секунд на загрузку 1 паллету", default=12)
    categories = (
        ("Сухие товары", "Сухие товары"),
        ("Скоропортящиеся товары", "Скоропортящиеся товары"),
        ("Хрупкие товары", "Хрупкие товары"),
    )
    typeProduct = models.CharField(
        default="Сухие товары",
        max_length=30,
        verbose_name="Тип склада",
        choices=categories
    )

    def get_S_pol(self):
        S_shelving = (self.shelving.lengthS/1000) * (self.shelving.widthS/1000)
        return round(S_shelving * self.count)

    def __str__(self):
        return "{0}_{1}".format(self.name, self.typeProduct)

    class Meta:
        verbose_name = u"Склад"
        verbose_name_plural = u"Склад"
