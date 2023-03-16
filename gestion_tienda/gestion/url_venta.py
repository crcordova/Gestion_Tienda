from django.urls import path

from . import views

urlpatterns = [
    path('', views.ventas, name='Ventas'),
    path('ventas_product', views.venta_by_product, name='ventas_product'),
    path('ventas_region', views.venta_by_region, name='ventas_region'),
]
