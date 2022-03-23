from django.db import models


class CarColor(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")
    rgb = models.CharField(max_length=7, verbose_name="Код")


class CarBrand(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")


class CarCategory(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name="Производитель")
    model = models.CharField(max_length=32, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, verbose_name="Категория")
