from django.urls import path

from . import views

urlpatterns = [
    path('', views.compras, name='Compras'),
    path('compra_proveedor', views.compra_by_proveedor, name='compra_proveedor'),

]