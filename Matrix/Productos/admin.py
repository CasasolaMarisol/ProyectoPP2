from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'existencias', 'proveedores')

admin.site.register(Producto, ProductoAdmin)

# Register your models here.