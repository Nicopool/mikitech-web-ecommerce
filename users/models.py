"""Modelos de usuarios — mapeados a la tabla 'profiles' en Supabase"""

import uuid
from django.db import models
from django.conf import settings


class Permiso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, db_column='name')
    codigo = models.CharField(max_length=50, unique=True, db_column='code')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'permissions'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, db_column='name')
    codigo = models.CharField(max_length=50, unique=True, db_column='code')
    permisos = models.ManyToManyField(Permiso, related_name='roles', db_table='role_permissions')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = 'roles'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class InvitacionAdmin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=150, unique=True, db_column='email')
    nombre_completo = models.CharField(max_length=200, blank=True, null=True, db_column='full_name')
    usuario_generado = models.CharField(max_length=100, unique=True, db_column='generated_username')
    password_temporal_hash = models.CharField(max_length=255, db_column='temp_password_hash')
    fecha_envio = models.DateTimeField(auto_now_add=True, db_column='sent_at')
    fecha_expiracion = models.DateTimeField(db_column='expires_at')
    estado = models.CharField(
        max_length=20, 
        default='pendiente', 
        choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('expirada', 'Expirada'), ('revocada', 'Revocada')],
        db_column='status'
    )
    notas_internas = models.TextField(blank=True, null=True, db_column='internal_notes')
    creado_por = models.ForeignKey('Perfil', on_delete=models.SET_NULL, null=True, blank=True, related_name='invitaciones_creadas', db_column='created_by')
    fecha_aceptacion = models.DateTimeField(blank=True, null=True, db_column='accepted_at')
    ip_origen = models.GenericIPAddressField(blank=True, null=True, db_column='source_ip')

    class Meta:
        db_table = 'admin_invitations'
        managed = getattr(settings, 'USE_SQLITE', False)
        verbose_name = 'Invitación Administrador'
        verbose_name_plural = 'Invitaciones Administrador'
        ordering = ['-fecha_envio']

    def __str__(self):
        return f"Invitación para {self.email} ({self.estado})"


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
    rol_rbac = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios', db_column='role_id')
    rol = models.CharField(max_length=20, default='client', choices=[('admin', 'Administrador'), ('client', 'Cliente'), ('repartidor', 'Repartidor')], db_column='role')
    esta_activo = models.BooleanField(default=True, db_column='is_active')
    fecha_primer_login = models.DateTimeField(blank=True, null=True, db_column='first_login_at')
    invitacion = models.ForeignKey(InvitacionAdmin, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios', db_column='invitation_id')
    password_cambiada = models.BooleanField(default=True, db_column='password_changed')
    creado_el = models.DateTimeField(auto_now_add=True, db_column='created_at')
    actualizado_el = models.DateTimeField(auto_now=True, db_column='updated_at')

    def save(self, *args, **kwargs):
        # Sincronizar bidireccionalmente el rol y el rol_rbac para compatibilidad
        if not self.rol_rbac and self.rol:
            try:
                self.rol_rbac = Rol.objects.get(codigo=self.rol)
            except Exception:
                pass
        elif self.rol_rbac:
            self.rol = self.rol_rbac.codigo
        super().save(*args, **kwargs)

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
