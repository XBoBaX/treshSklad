from django.db import models


class Shelving(models.Model):
    height = models.IntegerField(verbose_name="Высота стелажа (Одной полки)", null=True, blank=True)
    lengthS = models.IntegerField(verbose_name="Длина", null=True, blank=True)
    widthS = models.IntegerField(verbose_name="Ширина", null=True, blank=True)
    countShelf = models.IntegerField(verbose_name="Количество полок", null=True, blank=True)
    kg_polki = models.IntegerField(verbose_name="нагрузка, кг", null=True, blank=True)

    def get_s(self):
        return int(self.lengthS * self.widthS)

    class Meta:
        verbose_name = u"Стелаж"
        verbose_name_plural = u"Стелаж"
