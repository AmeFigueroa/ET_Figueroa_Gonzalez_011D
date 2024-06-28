from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Boleta, detalle_boleta
from .forms import ProductoForm, RegistroUserForm, CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .compra import Carrito

def inicio (request):
     return render(request, 'index.html')

def nosotros (request):
     return render(request, 'archivo2.html')

def receta (request):
     return render(request, 'receta.html')
 
def mostrar(request):
    productitos = Producto.objects.all()
    datos={
        'productitos':productitos
    }
    return render(request, 'mostrar.html', datos)


def iniciosesion (request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html',{
            'form': CustomAuthenticationForm()
        })
    else:
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
    if user is None:
        return render(request,'inicio_sesion.html',{
            'form':CustomAuthenticationForm(),
            'error':'Datos incorrectos'
        })
    else:
        login(request,user)
        return redirect('inicio')


def listadoproducto (request):
     return render(request, 'productos.html')

def productos (request):
     return render(request, 'crear.html')

@login_required
def home(request):
    productitos = Producto.objects.all()
    datos={
        'productitos':productitos
    }
    return render(request, 'home.html', datos)


@login_required
def crear(request):
    if request.method == "POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect('home')
    else:
        productoform = ProductoForm()
    return render(request, 'crear.html', {'productoform': productoform})


@login_required
def eliminar(request, id):
    productoEliminado = get_object_or_404(Producto, idProducto=id)
    productoEliminado.delete()
    return redirect('home')

@login_required
def modificar(request, id):
    productoModificado = get_object_or_404(Producto, idProducto=id)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = ProductoForm(instance=productoModificado)
    return render(request, 'modificar.html', {'form': formulario})

def registrar(request):
    data={                         
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('inicio') 
        data["form"]=formulario           
    return render(request, 'registrate.html',data)

def tienda(request):
    productitos = Producto.objects.all()
    datos={
        'productitos':productitos
    }
    return render(request, 'tienda.html', datos)

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.agregar(producto=producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(idProducto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html', datos)

def form_producto(request):
    if request.method=='POST': 
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect('home')
    else:
        productoform= ProductoForm()
    return render(request, 'core/form_producto.html', {'producto_form': productoform})

def salir(request):
    logout(request)
    return redirect('inicio')