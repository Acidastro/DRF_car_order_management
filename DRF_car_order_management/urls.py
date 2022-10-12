from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from orders.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),
    path('api/v1/orders/', OrdersAPIList.as_view()),
    path('api/v1/orders/', ColorsAPIList.as_view()),
    path('api/v1/orders/', ModelsAPIList.as_view()),
    path('api/v1/orders/', BrandsAPIList.as_view()),
    path('api/v1/orders/<int:pk>/', OrdersAPIUpdate.as_view()),
    path('api/v1/orders/<int:pk>/', ColorsAPIUpdate.as_view()),
    path('api/v1/orders/<int:pk>/', ModelsAPIUpdate.as_view()),
    path('api/v1/orders/<int:pk>/', BrandsAPIUpdate.as_view()),
    path('api/v1/ordersdelete/<int:pk>/', OrdersAPIDestroy.as_view()),
    path('api/v1/ordersdelete/<int:pk>/', ColorsAPIDestroy.as_view()),
    path('api/v1/ordersdelete/<int:pk>/', ModelsAPIDestroy.as_view()),
    path('api/v1/ordersdelete/<int:pk>/', BrandsAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
