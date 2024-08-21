from django.db import models
from Empleados.models import Empleado
from datetime import datetime
class Caja(models.Model):
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)
    fecha_apertura=models.DateTimeField(default=datetime.now, null=True, blank=True)
    saldo_inicial=models.IntegerField(null=True,blank=True)
    fecha_cierre=models.DateTimeField(default=datetime.now, null=True,blank=True)
    saldo_final=models.IntegerField(null=True,blank=True)    
    
    def __str__(self):
        return f"{self.empleado} {self.fecha_apertura} {self.fecha_cierre} {self.saldo_final}"

# Create your models here.