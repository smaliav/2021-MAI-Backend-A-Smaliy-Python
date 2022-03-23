from django.db import models


class User(models.Model):
    nickName = models.CharField(max_length=32, verbose_name="Ник")
    firstName = models.CharField(max_length=32, verbose_name="Имя")
    lastName = models.CharField(max_length=32, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(max_length=32, verbose_name="Телефон")
    city = models.CharField(max_length=32, verbose_name="Город")
