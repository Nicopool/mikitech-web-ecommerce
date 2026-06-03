"""Configuración del panel de administración de Django para la app USERS"""

from django.contrib import admin
from .models import Perfil, Notificacion


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'nombre_usuario', 'rol', 'esta_activo', 'creado_el')
    list_filter = ('rol', 'esta_activo', 'creado_el', 'pais')
    search_fields = ('nombre_completo', 'nombre_usuario', 'email', 'telefono')
    readonly_fields = ('id', 'creado_el', 'actualizado_el')
    fieldsets = (
        ('Identidad', {
            'fields': ('id', 'nombre_completo', 'nombre_usuario')
        }),
        ('Perfil', {
            'fields': ('biografia', 'url_avatar')
        }),
        ('Contacto', {
            'fields': ('telefono', 'ciudad', 'pais')
        }),
        ('Dirección', {
            'fields': ('direccion',)
        }),
        ('Administración', {
            'fields': ('rol', 'esta_activo')
        }),
        ('Timestamps', {
            'fields': ('creado_el', 'actualizado_el')
        }),
    )


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'esta_leida', 'creado_el')
    list_filter = ('esta_leida', 'creado_el', 'usuario')
    search_fields = ('usuario__nombre_usuario', 'mensaje')
    readonly_fields = ('id', 'creado_el')
