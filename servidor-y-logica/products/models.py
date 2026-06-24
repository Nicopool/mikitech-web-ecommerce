"""Modelos de productos — mapeados a las tablas de Supabase (managed=False)"""

import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, db_column='name')
    enlace = models.SlugField(max_length=100, unique=True, db_column='slug')
    descripcion = models.TextField(blank=True, null=True, db_column='description')
    icono = models.CharField(max_length=50, blank=True, null=True, db_column='icon')
    url_imagen = models.TextField(blank=True, null=True, db_column='image_url')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'categories'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos', db_column='category_id')
    nombre = models.CharField(max_length=200, db_column='name')
    enlace = models.SlugField(max_length=200, unique=True, db_column='slug')
    descripcion = models.TextField(blank=True, null=True, db_column='description')
    descripcion_corta = models.CharField(max_length=500, blank=True, null=True, db_column='short_description')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, db_column='price')
    existencias = models.IntegerField(default=0, db_column='stock')
    marca = models.CharField(max_length=100, blank=True, null=True, db_column='brand')
    modelo = models.CharField(max_length=100, blank=True, null=True, db_column='model')
    codigo_sku = models.CharField(max_length=100, unique=True, blank=True, null=True, db_column='sku')
    especificaciones = models.JSONField(default=dict, blank=True, db_column='specifications')
    url_imagen_principal = models.TextField(blank=True, null=True, db_column='main_image_url')
    descuento_porcentaje = models.IntegerField(default=0, db_column='discount_percentage')
    descuento_expira_el = models.DateTimeField(null=True, blank=True, db_column='discount_expires_at')
    esta_activo = models.BooleanField(default=True, db_column='is_active')
    es_destacado = models.BooleanField(default=False, db_column='is_featured')
    conteo_vistas = models.IntegerField(default=0, db_column='views_count')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'products'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-creado_el']

    def __str__(self):
        return self.nombre

    @property
    def conteo_votos(self):
        return self.votos.count()

    @property
    def conteo_reseñas(self):
        return self.reseñas.count()

    @property
    def calificacion_promedio(self):
        reseñas = self.reseñas.all()
        if not reseñas:
            return 0
        return sum(r.calificacion for r in reseñas if r.calificacion) / reseñas.count()

    @property
    def descuento_activo(self):
        """Retorna True si hay un descuento activo y no expirado."""
        if not self.descuento_porcentaje or self.descuento_porcentaje <= 0:
            return False
        if self.descuento_expira_el and timezone.now() > self.descuento_expira_el:
            return False
        return True

    @property
    def precio_con_descuento(self):
        """Retorna el precio final tras aplicar el descuento activo."""
        from decimal import Decimal
        if self.descuento_activo:
            # Calcular multiplicador de descuento: e.g. 0.90 para 10%
            multiplicador = Decimal(1) - (Decimal(self.descuento_porcentaje) / Decimal(100))
            return (self.precio * multiplicador).quantize(Decimal('1.'))
        return self.precio

    @property
    def en_stock(self):
        return self.existencias > 0


class ImagenProducto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes', db_column='product_id')
    url_imagen = models.TextField(db_column='image_url')
    texto_alt = models.CharField(max_length=200, blank=True, null=True, db_column='alt_text')
    orden = models.IntegerField(default=0, db_column='sort_order')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'product_images'
        managed = getattr(settings, 'USE_SQLITE', False)
        ordering = ['orden']

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"
