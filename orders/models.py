from django.db import models
from datetime import datetime
from django.utils import timezone


class OrderCar(models.Model):
    """
    Модель для хранения заказов авто. Заказ должен включать в себя цвет, модель, количество, дату (по умолчанию текущая)
    """

    color = models.ForeignKey('ColorCar', on_delete=models.CASCADE, blank=False, null=True, verbose_name='Цвет')
    brand = models.ForeignKey('BrandCar', on_delete=models.CASCADE, blank=False, null=True, verbose_name='Бренд')
    model = models.ForeignKey('ModelCar', on_delete=models.CASCADE, blank=False, null=True, verbose_name='Модель')
    amount = models.IntegerField(null=False, default=1, verbose_name='Количество')
    date = models.DateField(default=timezone.now, verbose_name='Дата и время')

    def __str__(self):
        return f'{self.brand} {self.model} {self.color} {self.date}'


class BrandCar(models.Model):
    """
    Марки автомобилей
    """
    brand = models.CharField(max_length=100, blank=False, null=True, verbose_name='Бренд')

    def __str__(self):
        return f'{self.brand}'


class ModelCar(models.Model):
    """
    Модели автомобилей
    """
    model = models.CharField(max_length=100, blank=False, null=True, verbose_name='Модель')
    brand = models.ForeignKey('BrandCar', on_delete=models.CASCADE, blank=False, null=True, verbose_name='Бренд')

    def __str__(self):
        return f' {self.model}'


class ColorCar(models.Model):
    """
    Цвета
    """
    color = models.CharField(max_length=100, blank=False, null=True, verbose_name='Цвет')

    def __str__(self):
        return f'{self.color}'
