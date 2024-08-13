from django.contrib.auth.models import AbstractUser
from django.db import models

class Empleado(AbstractUser):
    DNI=models.IntegerField(null=True, blank=True)
    Dirección=models.CharField(null=True, blank=True, max_length=150)
    Telefono=models.IntegerField(null=True, blank=True)

# Create your models here.