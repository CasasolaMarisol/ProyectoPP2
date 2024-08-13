from django.contrib import admin
from .models import caja

class CajaAdmin(admin.ModelAdmin):
    list_display = ('Empleado', 'Apertura_de_Caja', 'Saldo_Inicial', 'Cierre_de_Caja', 'Saldo_Total')

admin.site.register(caja, CajaAdmin)

# Register your models here.