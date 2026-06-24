"""URLs de la aplicación núcleo (core) — Mapeadas a funciones en español"""

from django.urls import path
from . import views
from . import repartidor_views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='home'),
    path('buscar/', views.buscar, name='search'),
    path('perfil/<str:nombre_usuario>/', views.perfil_publico, name='public_profile'),
    
    # Carrito (vista de revisión pública, sin login)
    path('carrito/', views.ver_carrito, name='cart'),
    path('api/cart-status/', views.cart_status_api, name='cart_status_api'),
    path('carrito/agregar/<str:id_producto>/', views.agregar_al_carrito, name='add_to_cart'),
    path('carrito/eliminar/<str:id_producto>/', views.eliminar_del_carrito, name='remove_from_cart'),
    path('carrito/actualizar/<str:id_producto>/', views.actualizar_carrito, name='update_cart'),
    
    # Checkout (requiere login)
    path('checkout/', views.carrito, name='checkout'),
    
    # Repartidor
    path('repartidor/pasarela/', repartidor_views.pasarela_repartidor, name='repartidor_gateway'),
    path('repartidor/login/', repartidor_views.login_repartidor, name='repartidor_login'),
    path('repartidor/registro/', repartidor_views.registro_repartidor, name='repartidor_register'),
    path('repartidor/logout/', repartidor_views.cerrar_sesion_repartidor, name='repartidor_logout'),
    path('repartidor/', repartidor_views.panel_repartidor, name='repartidor'),
    path('repartidor/entregar/<str:id_pedido>/', repartidor_views.entregar_pedido, name='entregar_pedido'),
    path('repartidor/asignar/<str:id_pedido>/', repartidor_views.asignar_pedido, name='asignar_pedido'),
    
    path('contacto/', views.contacto, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('ping/', views.ping, name='ping'),
]
