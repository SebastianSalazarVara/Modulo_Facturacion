from django.urls import path
from . import views

urlpatterns = [
    path('', views.facturacion_view, name='home'),
    path('facturacion/', views.facturacion_view, name='facturacion'),
    path('productos/', views.productos_view, name='productos'),
    path('impuestos/', views.impuestos_view, name='impuestos'),
    path('informes/', views.informes_view, name='informes'),
    path('busqueda/', views.busqueda_view, name='busqueda'),
    path('empresa/', views.empresa_view, name='empresa'),
    path('clientes/', views.clientes_view, name='clientes'),
]
