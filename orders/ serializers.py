from rest_framework import serializers

from orders.models import OrderCar, ModelCar, ColorCar, BrandCar


class OrderCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCar
        fields = '__all__'


class ModelCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCar
        fields = '__all__'


class ColorCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCar
        fields = '__all__'


class BrandCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCar
        fields = '__all__'
