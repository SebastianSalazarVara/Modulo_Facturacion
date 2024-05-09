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
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    #path('productos/buscar/', views.buscar_producto, name='buscar_producto'),

]
