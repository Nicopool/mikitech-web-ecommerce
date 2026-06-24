"""URLs de la aplicación interacciones — votos, reseñas y favoritos"""

from django.urls import path
from . import views

app_name = 'interactions'

urlpatterns = [
    path('votar/<uuid:id_producto>/', views.agregar_voto, name='add_vote'),
    path('reseñar/<uuid:id_producto>/', views.agregar_reseña, name='add_review'),
    path('responder/<uuid:id_reseña>/', views.agregar_respuesta, name='add_reply'),
    path('favorito/<uuid:id_producto>/', views.alternar_favorito, name='toggle_favorite'),
]
