from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from orders.models import OrderCar, ColorCar, ModelCar, BrandCar
from orders.serializers import OrderCarSerializer, ColorCarSerializer, BrandCarSerializer, ModelCarSerializer


# CRUD for orders:
class OrdersAPIListPagination(PageNumberPagination):
    page_size = 10  # количество записей на странице
    page_size_query_param = 'page_size'  # дополнительно можно написать: &page_size=4 для изменения пагинации
    max_page_size = 10000  # максимальное значение установленное вручную


class OrdersAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer


class OrdersAPIList(generics.ListCreateAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    pagination_class = OrdersAPIListPagination


# CRUD for Colors:

class ColorsAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ColorCar.objects.all()
    serializer_class = ColorCarSerializer


class ColorsAPIList(generics.ListCreateAPIView):
    queryset = ColorCar.objects.all()
    serializer_class = ColorCarSerializer
    pagination_class = OrdersAPIListPagination


# CRUD for Brands:

class BrandsAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializer


class BrandsAPIList(generics.ListCreateAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializer
    pagination_class = OrdersAPIListPagination


# CRUD for Models:

class ModelsAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer


class ModelsAPIList(generics.ListCreateAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer
    pagination_class = OrdersAPIListPagination
