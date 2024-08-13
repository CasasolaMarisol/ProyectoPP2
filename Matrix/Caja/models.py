from django.db import models
from Empleados.models import Empleado
from datetime import datetime
class caja(models.Model):
    Empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True,blank=True)
    Apertura_de_Caja=models.DateTimeField(default=datetime.now, null=True, blank=True)
    Saldo_Inicial=models.IntegerField(null=True,blank=True)
    Cierre_de_Caja=models.DateTimeField(default=datetime.now, null=True,blank=True)
    Saldo_Total=models.IntegerField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.Apertura_de_Caja} {self.Saldo_Inicial} {self.Cierre_de_Caja} {self.Saldo_Total}"

# Create your models here.