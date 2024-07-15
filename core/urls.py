from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, form_producto, eliminar, total_compra, mostrar, modificar, receta, inicio, nosotros, iniciosesion, listadoproducto, registrar, generarBoleta, agregar_producto, restar_producto, limpiar_carrito, crear, tienda, salir, productos

urlpatterns = [
    path('home/', home, name='home'),
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('listadoproducto/', listadoproducto, name='listadoproducto'),
    path('tienda/', tienda, name='tienda'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('registrar/', registrar, name='registrar'),
    path('salir/', salir, name='salir'),
    path('productos/', productos, name='productos'),
    path('receta/', receta, name='receta'),
    path('mostrar/', mostrar, name='mostrar'),

    path('form_producto/', form_producto, name='form_producto'),
    path('crear/', crear, name='crear'),
    path('generarBoleta/', generarBoleta, name='generarBoleta'),
    path('agregar/<id>/', agregar_producto, name='agregar'),
    path('eliminar/<id>/', eliminar, name='eliminar'),
    path('restar/<id>/', restar_producto, name='restar'),
    path('limpiar/', limpiar_carrito, name='limpiar'),
    path('modificar/<id>/', modificar, name='modificar'),

    path('total_compra/', total_compra, name= 'total_compra'),
 
]
