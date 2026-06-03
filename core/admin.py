"""Configuración del panel de administración de Django para la app CORE"""

from django.contrib import admin
from .models import Carrito, DetalleCarrito, Pedido, DetallePedido, Favorito


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'cantidad_articulos', 'total', 'creado_el')
    list_filter = ('creado_el', 'actualizado_el')
    search_fields = ('usuario__nombre_usuario', 'usuario__nombre_completo')
    readonly_fields = ('id', 'creado_el', 'actualizado_el')


@admin.register(DetalleCarrito)
class DetalleCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_filter = ('creado_el', 'carrito__usuario')
    search_fields = ('producto__nombre', 'carrito__usuario__nombre_usuario')
    readonly_fields = ('id', 'subtotal', 'creado_el', 'actualizado_el')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero_pedido', 'usuario', 'estado', 'total', 'creado_el')
    list_filter = ('estado', 'creado_el', 'ciudad_entrega')
    search_fields = ('numero_pedido', 'usuario__nombre_usuario', 'cedula_cliente')
    readonly_fields = ('id', 'numero_pedido', 'creado_el', 'actualizado_el', 'fecha_entrega')
    fieldsets = (
        ('Información del Pedido', {
            'fields': ('id', 'numero_pedido', 'usuario', 'estado')
        }),
        ('Dirección de Entrega', {
            'fields': ('direccion_entrega', 'ciudad_entrega', 'codigo_postal', 'cedula_cliente')
        }),
        ('Totales Financieros', {
            'fields': ('subtotal', 'iva', 'total')
        }),
        ('Pago', {
            'fields': ('metodo_pago', 'referencia_pago')
        }),
        ('Notas y Timestamps', {
            'fields': ('notas', 'creado_el', 'actualizado_el', 'fecha_entrega')
        }),
    )


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_filter = ('pedido__creado_el', 'pedido__usuario')
    search_fields = ('pedido__numero_pedido', 'producto__nombre')
    readonly_fields = ('id', 'subtotal')


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'creado_el')
    list_filter = ('creado_el', 'usuario')
    search_fields = ('usuario__nombre_usuario', 'producto__nombre')
    readonly_fields = ('id', 'creado_el')
