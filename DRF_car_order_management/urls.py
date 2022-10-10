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
    # path('api/v1/women/', OrderAPIList.as_view()),
    # path('api/v1/women/<int:pk>/', OrderAPIUpdate.as_view()),
    # path('api/v1/womendelete/<int:pk>/', OrderAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
