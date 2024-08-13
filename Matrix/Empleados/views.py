from django.shortcuts import render, redirect
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm 
def login_empleado (request):
    if request.method == 'GET':
        formulario_login=AuthenticationForm()
        return render(request, 'login.html', {'formulario_login': formulario_login})
    if request.method == 'POST':
        formulario_login=AuthenticationForm(request, data=request.POST)
        if formulario_login.is_valid():
            usuario = formulario_login.cleaned_data.get('username')
            contraseña = formulario_login.cleaned_data.get('password')
            validacion = authenticate(username = usuario, password = contraseña)
            if validacion is not None:
                login(request, validacion)
                return redirect('menu')
    return render(request, 'login.html', {'formulario_login': formulario_login})
def logout_empleado(request):
    logout(request)
    return redirect('login')