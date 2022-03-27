from django.db import models


class CarColor(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")
    rgb = models.CharField(max_length=7, verbose_name="Код", unique=True)


class CarBrand(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название", unique=True)


class CarCategory(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название", unique=True)


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, verbose_name="Производитель")
    model = models.CharField(max_length=32, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, verbose_name="Категория", null=True, blank=True)
