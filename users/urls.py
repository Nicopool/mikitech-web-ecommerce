"""URLs de la aplicación usuarios — autenticación y área privada"""

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('ingreso/', views.vista_ingreso, name='login'),
    path('registro/', views.vista_registro, name='register'),
    path('salir/', views.vista_cerrar_sesion, name='logout'),
    path('perfil/', views.mi_perfil, name='profile'),
    path('perfil/editar/', views.editar_perfil, name='edit_profile'),
    path('favoritos/', views.mis_favoritos, name='favorites'),
    path('pedidos/', views.mis_pedidos, name='orders'),
    path('historial/', views.mi_historial, name='history'),
    path('reportes/', views.mis_reportes, name='reports'),
    path('recuperar/', views.olvide_contraseña, name='forgot_password'),
    path('recuperar/verificar/', views.restablecer_contraseña, name='reset_password'),
]
