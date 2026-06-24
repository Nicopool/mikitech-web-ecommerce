"""Modelos de usuarios — mapeados a la tabla 'profiles' en Supabase"""

import uuid
from django.db import models
from django.conf import settings


class Perfil(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    nombre_completo = models.CharField(max_length=200, blank=True, null=True, db_column='full_name')
    nombre_usuario = models.CharField(max_length=50, unique=True, blank=True, null=True, db_column='username')
    biografia = models.TextField(blank=True, null=True, db_column='bio')
    url_avatar = models.TextField(blank=True, null=True, db_column='avatar_url')
    telefono = models.CharField(max_length=20, blank=True, null=True, db_column='phone')
    direccion = models.TextField(blank=True, null=True, db_column='address')
    ciudad = models.CharField(max_length=100, blank=True, null=True, db_column='city')
    pais = models.CharField(max_length=100, default='Colombia', db_column='country')
    rol = models.CharField(max_length=20, default='client', choices=[('admin', 'Administrador'), ('client', 'Cliente'), ('repartidor', 'Repartidor')], db_column='role')
    esta_activo = models.BooleanField(default=True, db_column='is_active')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'profiles'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.nombre_completo or self.nombre_usuario or str(self.id)

    @property
    def es_administrador(self):
        return self.rol == 'admin'

    @property
    def nombre_mostrado(self):
        return self.nombre_completo or self.nombre_usuario or 'Usuario'

    @property
    def email(self):
        from django.db import connection
        from django.conf import settings
        table_name = '"auth.users"' if getattr(settings, 'USE_SQLITE', False) else 'auth.users'
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT email FROM {table_name} WHERE id = %s", [str(self.id)])
                row = cursor.fetchone()
                return row[0] if row else None
        except Exception as e:
            print(f"[Perfil.email] Error getting email: {e}")
            return None

    @email.setter
    def email(self, value):
        from django.db import connection
        from django.conf import settings
        table_name = '"auth.users"' if getattr(settings, 'USE_SQLITE', False) else 'auth.users'
        now_func = "datetime('now')" if getattr(settings, 'USE_SQLITE', False) else "NOW()"
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"UPDATE {table_name} SET email = %s, email_confirmed_at = {now_func} WHERE id = %s",
                    [value, str(self.id)]
                )
        except Exception as e:
            print(f"[Perfil.email] Error setting email: {e}")


class Notificacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='notificaciones', db_column='user_id')
    mensaje = models.TextField(db_column='message')
    esta_leida = models.BooleanField(default=False, db_column='is_read')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'notifications'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        return f"Notificación para {self.usuario.nombre_usuario}: {self.mensaje[:20]}..."
