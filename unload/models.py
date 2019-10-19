from django.db import models
from datetime import datetime
from WarehouseSpace.models import WarehouseSpace


class Unloader(models.Model):
    dateRegister = models.DateTimeField(default=datetime.now, verbose_name="Дата регистрации")
    dateArrival = models.DateTimeField(null=True, blank=True, verbose_name="Ожидаемое время начала разгрузки")
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата разгрузки")
    timeProc = models.IntegerField(default=0, verbose_name="Минут на разгрузку", null=True, blank=True)
    coutPalletAll = models.IntegerField(verbose_name="Кол-во паллет", null=True, blank=True)
    loads = models.BooleanField(default=False, null=True, blank=True, verbose_name="Загрузка")

    categories2 = (
        ("Ожидание", "Ожидание"),
        ("Загрузка", "Загрузка"),
        ("Отправлен", "Отправлен"),
    )
    status = models.CharField(
        default="Ожидание",
        max_length=30,
        verbose_name="Статус",
        choices=categories2
    )

    def __str__(self):
        return "{0}_{1}".format(self.dateRegister, self.status)

    class Meta:
        verbose_name = u"Разгрузка"
        verbose_name_plural = u"Разгрузка"



