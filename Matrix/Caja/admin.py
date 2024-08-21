from django.contrib import admin
from .models import *

class CajaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha_apertura', 'saldo_inicial', 'fecha_cierre', 'saldo_final')

admin.site.register(Caja, CajaAdmin)

# Register your models here.