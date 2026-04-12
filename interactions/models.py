"""Modelos de interacciones — votos, favoritos, reseñas y respuestas — MIKITECH"""

import uuid
from django.db import models


class Voto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey('users.Perfil', on_delete=models.CASCADE, related_name='votos', db_column='user_id')
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='votos', db_column='product_id')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'votes'
        managed = False
        unique_together = ('usuario', 'producto')
        verbose_name = 'Voto'
        verbose_name_plural = 'Votos'

    def __str__(self):
        return f"Voto de {self.usuario.nombre_usuario} por {self.producto.nombre}"


class Reseña(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey('users.Perfil', on_delete=models.CASCADE, related_name='reseñas', db_column='user_id')
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='reseñas', db_column='product_id')
    calificacion = models.IntegerField(default=5, db_column='rating')
    comentario = models.TextField(db_column='content')
    esta_aprobada = models.BooleanField(default=True, db_column='is_approved')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'reviews'
        managed = False
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'

    def __str__(self):
        return f"Reseña de {self.usuario.nombre_usuario} sobre {self.producto.nombre}"


class Respuesta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reseña = models.ForeignKey(Reseña, on_delete=models.CASCADE, related_name='respuestas', db_column='review_id')
    usuario = models.ForeignKey('users.Perfil', on_delete=models.CASCADE, related_name='respuestas_interacciones', db_column='user_id')
    contenido = models.TextField(db_column='content')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'review_replies'
        managed = False
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return f"Respuesta de {self.usuario.nombre_usuario} a reseña {self.reseña.id}"


class Favorito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey('users.Perfil', on_delete=models.CASCADE, related_name='favoritos', db_column='user_id')
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='favoritos', db_column='product_id')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'favorites'
        managed = False
        unique_together = ('usuario', 'producto')
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        return f"{self.producto.nombre} en favoritos de {self.usuario.nombre_usuario}"

class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey('users.Perfil', on_delete=models.CASCADE, related_name='pedidos', db_column='user_id')
    estado = models.CharField(max_length=50, default='Pendiente', db_column='status')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, db_column='total_amount')
    direccion_envio = models.TextField(db_column='shipping_address')
    cedula = models.CharField(max_length=50, null=True, blank=True, db_column='document_id')
    telefono = models.CharField(max_length=30, null=True, blank=True, db_column='phone')
    repartidor = models.ForeignKey('users.Perfil', on_delete=models.SET_NULL, null=True, blank=True, related_name='entregas', db_column='driver_id')
    notas = models.TextField(null=True, blank=True, db_column='notes')
    entregado_el = models.DateTimeField(null=True, blank=True, db_column='delivered_at')
    notas_repartidor = models.TextField(null=True, blank=True, db_column='delivery_notes')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'orders'
        managed = False
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"


class DetallePedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles', db_column='order_id')
    producto = models.ForeignKey('products.Producto', on_delete=models.CASCADE, related_name='ventas', db_column='product_id')
    cantidad = models.IntegerField(db_column='quantity')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, db_column='unit_price')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'order_items'
        managed = False
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedido'

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} (Pedido {self.pedido.id})"
