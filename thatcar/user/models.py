from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=32, verbose_name="Ник")
    first_name = models.CharField(max_length=32, verbose_name="Имя")
    last_name = models.CharField(max_length=32, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(max_length=32, verbose_name="Телефон")
    city = models.CharField(max_length=32, verbose_name="Город")
