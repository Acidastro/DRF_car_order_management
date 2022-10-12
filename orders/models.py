from django.db import models
from datetime import datetime
from django.utils import timezone


class OrderCar(models.Model):
    """
    Модель для хранения заказов авто. Заказ должен включать в себя цвет, модель, количество, дату (по умолчанию текущая)
    """

    color = models.ForeignKey('ColorCar', on_delete=models.CASCADE, null=False, verbose_name='Цвет')
    brand = models.ForeignKey('BrandCar', on_delete=models.CASCADE, null=False, verbose_name='Бренд')
    model = models.ForeignKey('ModelCar', on_delete=models.CASCADE, null=False, verbose_name='Модель')
    date = models.DateField(default=timezone.now, verbose_name='Дата и время')

    def __str__(self):
        return f'{self.brand} {self.model} {self.color} {self.date}'


class BrandCar(models.Model):
    """
    Марки автомобилей
    """
    brand = models.CharField(max_length=100, null=False, verbose_name='Бренд')


class ModelCar(models.Model):
    """
    Модели автомобилей
    """
    model = models.CharField(max_length=100, null=False, verbose_name='Модель')


class ColorCar(models.Model):
    """
    Цвета
    """
    color = models.CharField(max_length=100, null=False, verbose_name='Цвет')
