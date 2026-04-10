"""URLs de la aplicación núcleo (core) — Mapeadas a funciones en español"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='home'),
    path('buscar/', views.buscar, name='search'),
    path('perfil/<str:nombre_usuario>/', views.perfil_publico, name='public_profile'),
    
    # Carrito (vista de revisión pública, sin login)
    path('carrito/', views.ver_carrito, name='cart'),
    path('carrito/agregar/<str:id_producto>/', views.agregar_al_carrito, name='add_to_cart'),
    path('carrito/eliminar/<str:id_producto>/', views.eliminar_del_carrito, name='remove_from_cart'),
    path('carrito/actualizar/<str:id_producto>/', views.actualizar_carrito, name='update_cart'),
    
    # Checkout (requiere login)
    path('checkout/', views.carrito, name='checkout'),
    
    path('contacto/', views.contacto, name='contact'),
    path('blog/', views.blog, name='blog'),
]
