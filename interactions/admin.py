"""Configuración del panel de administración de Django para la app INTERACTIONS"""

from django.contrib import admin
from .models import Voto, Reseña, Respuesta


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'creado_el')
    list_filter = ('creado_el', 'usuario')
    search_fields = ('usuario__nombre_usuario', 'producto__nombre')
    readonly_fields = ('id', 'creado_el')


@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'calificacion', 'esta_aprobada', 'creado_el')
    list_filter = ('calificacion', 'esta_aprobada', 'creado_el')
    search_fields = ('usuario__nombre_usuario', 'producto__nombre', 'comentario')
    readonly_fields = ('id', 'creado_el')
    fieldsets = (
        ('Información de Reseña', {
            'fields': ('id', 'usuario', 'producto')
        }),
        ('Contenido', {
            'fields': ('calificacion', 'comentario')
        }),
        ('Moderación', {
            'fields': ('esta_aprobada',)
        }),
        ('Timestamps', {
            'fields': ('creado_el',)
        }),
    )


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('reseña', 'usuario', 'creado_el')
    list_filter = ('creado_el', 'usuario')
    search_fields = ('usuario__nombre_usuario', 'reseña__producto__nombre', 'contenido')
    readonly_fields = ('id', 'creado_el')
