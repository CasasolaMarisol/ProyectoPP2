from django.db import models

class proveedore(models.Model):
    Nombre=models.CharField(max_length=100)
    Telefono=models.IntegerField()
    Email=models.CharField(max_length=100)
    Dirección=models.CharField(max_length=100)
    Provincia=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Nombre}"
# Create your models here.
