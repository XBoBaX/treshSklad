from django.db import models
from datetime import datetime
from WarehouseSpace.models import WarehouseSpace


class Traffic(models.Model):
    name = models.CharField(verbose_name="Юр.лицо", max_length=50, blank=True)
    dateRegister = models.DateTimeField(default=datetime.now, verbose_name="Дата регистрации")
    dateArrival = models.DateTimeField(null=True, blank=True, verbose_name="Ожидаемое прибытие")
    dateUpload = models.DateTimeField(null=True, blank=True, verbose_name="Дата прибытия")
    timeProc = models.IntegerField(default=0, verbose_name="Минут на разгрузку", null=True, blank=True)
    sklad = models.ForeignKey(WarehouseSpace, on_delete=models.CASCADE, null=True, verbose_name="На склад")
    coutPalletAll = models.IntegerField(verbose_name="Кол-во паллет", null=True, blank=True)
    unloads = models.BooleanField(default=False, null=True, blank=True, verbose_name="Разгрузка")

    categories2 = (
        ("Отправлен", "Отправлен"),
        ("Прибыл", "Прибыл"),
        ("Принят", "Принят"),
        ("Отменен", "Отменен"),
    )

    status = models.CharField(
        default="Отправлен",
        max_length=30,
        verbose_name="Статус",
        choices=categories2
    )

    def __str__(self):
        return "{0}_{1}".format(self.name, self.dateRegister)
    class Meta:
        verbose_name = u"Грузопоток"
        verbose_name_plural = u"Грузопоток"



