"""Modelos de la aplicación CORE — Carrito, Pedidos, Checkout — MIKITECH"""

import uuid
from decimal import Decimal
from django.db import models
from django.utils import timezone
from products.models import Producto
from users.models import Perfil


class Carrito(models.Model):
    """Carrito de compras — persistencia en sesión con modelo auxiliar"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='carrito', db_column='user_id')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'carts'
        managed = False
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        return f"Carrito de {self.usuario.nombre_usuario}"

    @property
    def total(self):
        """Calcula el total del carrito usando Decimal para precisión"""
        return sum(Decimal(str(item.subtotal)) for item in self.detalles.all())

    @property
    def cantidad_articulos(self):
        """Retorna el número total de artículos en el carrito"""
        return sum(item.cantidad for item in self.detalles.all())


class DetalleCarrito(models.Model):
    """Detalles individuales del carrito"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='detalles', db_column='cart_id')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='product_id')
    cantidad = models.PositiveIntegerField(default=1, db_column='quantity')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, db_column='unit_price')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'cart_items'
        managed = False
        verbose_name = 'Detalle del Carrito'
        verbose_name_plural = 'Detalles del Carrito'
        unique_together = ('carrito', 'producto')

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.carrito}"

    @property
    def subtotal(self):
        """Calcula el subtotal del detalle (cantidad × precio unitario)"""
        return Decimal(str(self.cantidad)) * Decimal(str(self.precio_unitario))


class Pedido(models.Model):
    """Modelo maestro de pedidos — Estados: pending, processing, shipped, delivered"""
    ESTADO_CHOICES = [
        ('pending', 'Pendiente'),
        ('processing', 'Procesando'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='pedidos', db_column='user_id')
    numero_pedido = models.CharField(max_length=20, unique=True, db_column='order_number')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pending', db_column='status')
    
    # Dirección de entrega
    direccion_entrega = models.TextField(db_column='delivery_address')
    ciudad_entrega = models.CharField(max_length=100, db_column='delivery_city')
    codigo_postal = models.CharField(max_length=10, blank=True, null=True, db_column='postal_code')
    cedula_cliente = models.CharField(max_length=50, db_column='customer_cedula')
    
    # Información de pago y totales (usando Decimal para precisión)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='subtotal')
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='tax')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='total')
    
    # Detalles adicionales
    notas = models.TextField(blank=True, null=True, db_column='notes')
    metodo_pago = models.CharField(max_length=50, blank=True, null=True, db_column='payment_method')
    referencia_pago = models.CharField(max_length=100, blank=True, null=True, db_column='payment_reference')
    
    # Timestamps
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')
    fecha_entrega = models.DateTimeField(null=True, blank=True, db_column='delivered_at')

    class Meta:
        db_table = 'orders'
        managed = False
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-creado_el']

    def __str__(self):
        return f"Pedido {self.numero_pedido} — {self.usuario.nombre_usuario}"

    @property
    def puede_ser_entregado(self):
        """Verifica si el pedido está en estado 'shipped' para poder entregarlo"""
        return self.estado == 'shipped'

    def marcar_como_entregado(self):
        """Marca el pedido como entregado y registra la fecha"""
        self.estado = 'delivered'
        self.fecha_entrega = timezone.now()
        self.save()


class DetallePedido(models.Model):
    """Detalles de líneas en cada pedido"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles', db_column='order_id')
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, db_column='product_id')
    cantidad = models.PositiveIntegerField(db_column='quantity')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, db_column='unit_price')
    
    class Meta:
        db_table = 'order_items'
        managed = False
        verbose_name = 'Detalle del Pedido'
        verbose_name_plural = 'Detalles del Pedido'

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en {self.pedido.numero_pedido}"

    @property
    def subtotal(self):
        """Calcula el subtotal de la línea"""
        return Decimal(str(self.cantidad)) * Decimal(str(self.precio_unitario))


class Favorito(models.Model):
    """Sistema de favoritos — Productos guardados por usuarios"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='favoritos', db_column='user_id')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='favoritos', db_column='product_id')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'favorites'
        managed = False
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('usuario', 'producto')

    def __str__(self):
        return f"{self.usuario.nombre_usuario} marcó como favorito {self.producto.nombre}"

