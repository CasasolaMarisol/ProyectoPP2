from django.contrib import admin
from .models import producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Precio', 'Existencias', 'Proveedores')

admin.site.register(producto, ProductoAdmin)

# Register your models here.