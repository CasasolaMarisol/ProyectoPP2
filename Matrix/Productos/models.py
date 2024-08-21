from django.db import models
from Proveedores.models import proveedore

class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=6, decimal_places=2) 
    existencias=models.IntegerField()
    proveedores=models.ForeignKey(proveedore, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre} ${self.precio}"

# Create your models here.