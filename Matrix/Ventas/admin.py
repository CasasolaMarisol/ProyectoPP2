from django.contrib import admin
from .models import venta

class VentasAdmin(admin.ModelAdmin):
    list_display = ('Producto', 'Precio_Unitario', 'Cantidad', 'Total')

admin.site.register(venta, VentasAdmin)

# Register your models here.