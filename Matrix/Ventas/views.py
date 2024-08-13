from django.shortcuts import render, redirect
from Productos.models import producto

def ventas(request):
    lista_productos = producto.objects.all()
    return render(request, 'ventas.html', {'lista_productos': lista_productos})

def actualizar_cantidad(request, id_producto):
    lista_productos = producto.objects.all()
    producto_buscado = producto.objects.get(id=id_producto)
    if 'carrito' not in request.session:
        request.session['carrito'] = []
        
    carrito = request.session['carrito']

    producto_a_vender = {
        'id': producto_buscado.id,
        'nombre': producto_buscado.Nombre,
        'precio': float(producto_buscado.Precio),
        'cantidad': 1,
        'subtotal': float(producto_buscado.Precio)
    }
    
    producto_encontrado = False
    for item in carrito:
        if producto_a_vender['id'] == item['id']:
            producto_encontrado = True
            if request.method == 'POST':
                nueva_cantidad = int(request.POST.get('cantidad'))
                diferencia = nueva_cantidad - item['cantidad']
                
                if diferencia > 0:
                    producto_buscado.Existencias -= diferencia
                else:
                    producto_buscado.Existencias += abs(diferencia)
                
                item['cantidad'] = nueva_cantidad
                item['subtotal'] = item['cantidad'] * item['precio']
                producto_buscado.save()

    if not producto_encontrado:
        if request.method == 'POST':
            nueva_cantidad = int(request.POST.get('cantidad'))
            producto_a_vender['cantidad'] = nueva_cantidad
            producto_a_vender['subtotal'] = nueva_cantidad * producto_a_vender['precio']
            carrito.append(producto_a_vender)
            producto_buscado.Existencias -= nueva_cantidad
            producto_buscado.save()

    request.session.modified = True
    return render(request, 'ventas.html', {'carrito': carrito, 'lista_productos': lista_productos})

def eliminar_producto(request, id_producto):
    carrito = request.session.get('carrito', [])
    for item in carrito:
        if item['id'] == id_producto:
            producto_buscado = producto.objects.get(id=id_producto)
            producto_buscado.Existencias += item['cantidad']
            producto_buscado.save()
            carrito.remove(item)
            break
    
    request.session.modified = True
    return redirect('ventas')

def vaciar_carrito(request):
    request.session['carrito'] = []
    request.session.modified = True
    return redirect('ventas')
