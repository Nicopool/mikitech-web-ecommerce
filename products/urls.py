"""URLs de la aplicación productos — catálogo y detalles"""

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.lista_productos, name='list'),
    path('<slug:enlace>/', views.detalle_producto, name='detail'),
]
