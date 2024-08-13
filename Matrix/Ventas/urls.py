from django.urls import path
from . import views

urlpatterns = [
    path('ventas/', views.ventas, name='ventas'),
    path('actualizar_cantidad/<int:id_producto>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]

