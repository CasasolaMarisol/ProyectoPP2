from django.db import models
from Productos.models import Producto
from Proveedores.models import proveedore

class compra(models.Model):
    Producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    Proveedor=models.ForeignKey(proveedore, on_delete=models.CASCADE)
    Precio_Unitario=models.DecimalField(max_digits=6, decimal_places=2)
    Cantidad=models.IntegerField()
    Total=models.IntegerField()
    def __str__(self):
        return f"{self.Producto} {self.Proveedor} {self.Precio_Unitario} {self.Cantidad} {self.Total}"

# Create your models here.