from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(verbose_name="ФИО", max_length=30, blank=True)
    workWith = models.DateField(verbose_name="Работает с", null=True, blank=True)
    hoursModifier = models.IntegerField(verbose_name="Норма-часов (модификатор)", null=True, blank=True)
    categories = (
        ("Грузчик", "Грузчик"),
        ("Менеджер", "Менеджер"),
        ("Администратор", "Администратор"),
    )
    position = models.CharField(
        default="Грузчик",
        max_length=30,
        verbose_name="Должность",
        choices=categories
    )

    def __str__(self):
        return "{0}".format(self.user.username)

    def get_name(self):
        return self.user.username

    class Meta:
        verbose_name = u"Пользователь"
        verbose_name_plural = u"Пользователь"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
