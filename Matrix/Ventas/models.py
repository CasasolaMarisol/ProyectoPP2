from django.db import models
from Productos.models import Producto
from datetime import datetime
Metodos_Pagos=[('',''),('Efectivo','Efectivo'),('Transferencia','Transferencia'),
               ('Tarjeta_de_Debito','Tarjeta de Debito'),('Tarjeta_de_Credito','Tarjeta de Credito')]
class Venta(models.Model):
    fecha=models.DateTimeField(default=datetime.now)
    productos=models.ManyToManyField(Producto, through='Productos_Vendidos')
    total_venta=models.IntegerField(default=0)
    metodo_pago=models.CharField(max_length=25, choices=Metodos_Pagos,default='')
    id_sesion=models.CharField(max_length=100)
class Productos_Vendidos(models.Model):
    venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    subtotal=models.IntegerField()
    