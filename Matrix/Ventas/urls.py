from django.urls import path
from . import views

urlpatterns = [
    path('panel_venta/', views.panel_venta, name='panel_venta'),
    path('agregar_producto/<int:id_producto>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('crear_factura/<int:id_venta>/', views.crear_factura, name='crear_factura'),
    path('nueva_venta', views.nueva_venta, name='nueva_venta')
]
