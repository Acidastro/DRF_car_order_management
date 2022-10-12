from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from orders.models import OrderCar, ColorCar, ModelCar, BrandCar
from orders.serializers import OrderCarSerializer, ColorCarSerializer, BrandCarSerializer, ModelCarSerializer


# CRUD for orders:
class OrdersAPIListPagination(PageNumberPagination):
    page_size = 10  # количество записей на странице
    page_size_query_param = 'page_size'  # дополнительно можно написать: &page_size=4 для изменения пагинации
    max_page_size = 10000  # максимальное значение установленное вручную


class OrdersAPIList(generics.ListCreateAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Установит ограничение доступа
    pagination_class = OrdersAPIListPagination


class OrdersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    permission_classes = (IsAuthenticated,)  # Установит ограничение доступа
    authentication_classes = (
        TokenAuthentication,)  # Предоставляет доступ только авторизованным по токенам пользователям


class OrdersAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = OrderCar.objects.all()
    serializer_class = OrderCarSerializer
    permission_classes = (IsAuthenticated,)


# CRUD for colors:

class ColorsAPIList(generics.ListCreateAPIView):
    queryset = ColorCar.objects.all()
    serializer_class = ColorCarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Установит ограничение доступа
    pagination_class = OrdersAPIListPagination


class ColorsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ColorCar.objects.all()
    serializer_class = ColorCarSerializer
    permission_classes = (IsAuthenticated,)  # Установит ограничение доступа
    authentication_classes = (
        TokenAuthentication,)  # Предоставляет доступ только авторизованным по токенам пользователям


class ColorsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ColorCar.objects.all()
    serializer_class = ColorCarSerializer
    permission_classes = (IsAuthenticated,)


# CRUD for brands:

class BrandsAPIList(generics.ListCreateAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Установит ограничение доступа
    pagination_class = OrdersAPIListPagination


class BrandsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializer
    permission_classes = (IsAuthenticated,)  # Установит ограничение доступа
    authentication_classes = (
        TokenAuthentication,)  # Предоставляет доступ только авторизованным по токенам пользователям


class BrandsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = BrandCar.objects.all()
    serializer_class = BrandCarSerializer
    permission_classes = (IsAuthenticated,)


# CRUD for models:

class ModelsAPIList(generics.ListCreateAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Установит ограничение доступа
    pagination_class = OrdersAPIListPagination


class ModelsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer
    permission_classes = (IsAuthenticated,)  # Установит ограничение доступа
    authentication_classes = (
        TokenAuthentication,)  # Предоставляет доступ только авторизованным по токенам пользователям


class ModelsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer
    permission_classes = (IsAuthenticated,)
