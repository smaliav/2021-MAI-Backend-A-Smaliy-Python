from django.db import models
from user.models import User
from car.models import Car, CarColor


class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Авто")
    price = models.IntegerField(verbose_name="Цена")
    milage = models.IntegerField(verbose_name="Пробег")
    color = models.ForeignKey(CarColor, on_delete=models.CASCADE, verbose_name="Цвет")
    vin = models.CharField(max_length=17, verbose_name="VIN")
    power = models.IntegerField(verbose_name="Лошадиные силы")
