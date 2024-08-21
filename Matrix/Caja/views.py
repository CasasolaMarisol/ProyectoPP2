from django.shortcuts import render, redirect
from .forms import *
from Empleados.models import Empleado
from .models import Caja
from Ventas.models import *
from datetime import datetime

def apertura_view(request):
    if request.method == 'GET':
        
        formulario_apertura=apertura()
        return render(request, 'apertura.html', {'formulario_apertura': formulario_apertura})

    if request.method == 'POST':
        formulario_apertura=apertura(request.POST)
        formulario_apertura.instance.Empleado=Empleado.objects.get(username=request.user.username)
        if formulario_apertura.is_valid():
            formulario_apertura.save()
            return redirect('menu')
        return render(request, 'apertura.html', {'formulario_apertura': formulario_apertura})

def cierre_view(request):
    if request.method == 'GET':
        formulario_cierre=cierre()
        return render(request, 'cierre.html', {'formulario_cierre': formulario_cierre})

    if request.method == 'POST':
        caja_a_cerrar=Caja.objects.filter(Empleado=request.user).latest('Apertura_de_Caja')
        formulario_cierre=cierre(request.POST, instance=caja_a_cerrar)
        if formulario_cierre.is_valid():
            formulario_cierre.save()
            return redirect('menu')
        return render(request, 'cierre.html', {'formulario_cierre': formulario_cierre})
# Create your views here.
