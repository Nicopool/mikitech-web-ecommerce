"""Configuración del panel de administración de Django para la app PRODUCTS"""

from django.contrib import admin
from .models import Categoria, Producto, ImagenProducto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'enlace', 'creado_el')
    list_filter = ('creado_el', 'actualizado_el')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'enlace': ('nombre',)}
    readonly_fields = ('id', 'creado_el', 'actualizado_el')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'existencias', 'esta_activo', 'es_destacado')
    list_filter = ('categoria', 'esta_activo', 'es_destacado', 'creado_el', 'descuento_activo')
    search_fields = ('nombre', 'enlace', 'marca', 'modelo', 'codigo_sku')
    prepopulated_fields = {'enlace': ('nombre',)}
    readonly_fields = ('id', 'conteo_vistas', 'conteo_votos', 'conteo_reseñas', 'calificacion_promedio', 'creado_el', 'actualizado_el')
    fieldsets = (
        ('Información Básica', {
            'fields': ('id', 'nombre', 'enlace', 'categoria', 'marca', 'modelo', 'codigo_sku')
        }),
        ('Descripción', {
            'fields': ('descripcion', 'descripcion_corta')
        }),
        ('Precios y Stock', {
            'fields': ('precio', 'existencias', 'descuento_porcentaje', 'descuento_expira_el')
        }),
        ('Especificaciones', {
            'fields': ('especificaciones',)
        }),
        ('Imágenes', {
            'fields': ('url_imagen_principal',)
        }),
        ('Estado y Visibilidad', {
            'fields': ('esta_activo', 'es_destacado')
        }),
        ('Analítica', {
            'fields': ('conteo_vistas', 'conteo_votos', 'conteo_reseñas', 'calificacion_promedio')
        }),
        ('Timestamps', {
            'fields': ('creado_el', 'actualizado_el')
        }),
    )


@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'orden', 'creado_el')
    list_filter = ('producto', 'creado_el')
    search_fields = ('producto__nombre',)
    readonly_fields = ('id', 'creado_el')
