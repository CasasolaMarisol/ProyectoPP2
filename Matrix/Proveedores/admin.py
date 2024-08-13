from django.contrib import admin
from .models import proveedore

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Telefono', 'Email', 'Dirección', 'Provincia')

admin.site.register(proveedore, ProveedoresAdmin)

# Register your models here.