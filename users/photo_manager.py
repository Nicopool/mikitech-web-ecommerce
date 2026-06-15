import os
import uuid
from django.conf import settings
from django.core.files.storage import default_storage
from users.models import Perfil
from users.supabase_auth import subir_a_supabase_storage

class UserPhotoManager:
    @staticmethod
    def upload_user_photo(user_id, file):
        """
        Sube la foto de perfil del usuario a Supabase Storage.
        Si falla, cae en el fallback local.
        Retorna la URL pública.
        """
        extension = os.path.splitext(file.name)[1].lower()
        if extension not in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            raise ValueError("Formato de archivo no válido. Use JPG, PNG, GIF o WEBP.")
        
        nombre_archivo = f"avatars/{user_id}{extension}"
        try:
            datos_archivo = file.read()
            file.seek(0)
            public_url, error = subir_a_supabase_storage(nombre_archivo, datos_archivo, file.content_type)
            if public_url:
                return public_url
            else:
                print(f"[UserPhotoManager] Fallback a local por error: {error}")
        except Exception as e:
            print(f"[UserPhotoManager] Fallback a local por excepción: {e}")
            
        nombre_guardado = default_storage.save(nombre_archivo, file)
        return f"/media/{nombre_guardado}"

    @staticmethod
    def delete_old_photo(user_id, current_photo_url):
        """
        Elimina la foto anterior del storage (si es necesario).
        """
        pass

    @staticmethod
    def update_user(user_id, data, photo_file=None):
        """
        Actualiza los datos del usuario (texto + foto) en la base de datos.
        """
        try:
            perfil = Perfil.objects.get(id=user_id)
        except Perfil.DoesNotExist:
            return None, "El usuario no existe."

        # Actualizar campos de texto en Perfil
        if 'nombre_completo' in data:
            perfil.nombre_completo = data['nombre_completo']
        if 'nombre_usuario' in data:
            perfil.nombre_usuario = data['nombre_usuario']
        if 'rol' in data:
            perfil.rol = data['rol']
        if 'esta_activo' in data:
            perfil.esta_activo = data['esta_activo']
        if 'telefono' in data:
            perfil.telefono = data['telefono']
        if 'biografia' in data:
            perfil.biografia = data['biografia']
        if 'ciudad' in data:
            perfil.ciudad = data['ciudad']
        if 'pais' in data:
            perfil.pais = data['pais']

        # Si hay foto, subirla y actualizar url_avatar
        if photo_file:
            try:
                url_avatar = UserPhotoManager.upload_user_photo(user_id, photo_file)
                perfil.url_avatar = url_avatar
            except Exception as e:
                return None, f"Error al subir la foto: {str(e)}"

        perfil.save()

        # Actualizar email en auth.users si se pasa en los datos
        if 'email' in data:
            from django.db import connection
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE auth.users SET email = %s, email_confirmed_at = NOW() WHERE id = %s",
                        [data['email'], str(user_id)]
                    )
            except Exception as e:
                print(f"[UserPhotoManager] Error actualizando email en auth.users: {e}")
                # No fallamos la transacción entera, pero registramos el error
                
        return perfil, None
