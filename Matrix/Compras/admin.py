from django.contrib import admin
from .models import compra

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('Producto','Proveedor', 'Precio_Unitario', 'Cantidad', 'Total')

admin.site.register(compra, ComprasAdmin)