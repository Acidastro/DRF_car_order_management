from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from orders.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/orders/', OrdersAPIList.as_view()),
    path('api/v1/colors/', ColorsAPIList.as_view()),
    path('api/v1/models/', ModelsAPIList.as_view()),
    path('api/v1/brands/', BrandsAPIList.as_view()),
    path('api/v1/colors/<int:pk>/', ColorsAPIUpdateDestroy.as_view()),
    path('api/v1/models/<int:pk>/', ModelsAPIUpdateDestroy.as_view()),
    path('api/v1/brands/<int:pk>/', BrandsAPIUpdateDestroy.as_view()),
    path('api/v1/orders-update-delete/<int:pk>/', OrdersAPIUpdateDestroy.as_view()),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

]
