from django.db import models
from Proveedores.models import proveedore

class producto(models.Model):
    Nombre=models.CharField(max_length=100)
    Precio=models.DecimalField(max_digits=6, decimal_places=2) 
    Existencias=models.IntegerField()
    Proveedores=models.ForeignKey(proveedore, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Nombre} ${self.Precio}"

# Create your models here.