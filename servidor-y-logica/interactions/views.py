"""Vistas de la aplicación interacciones — votos, favoritos, reseñas y respuestas — MIKITECH"""

import uuid
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from products.models import Producto
from .models import Voto, Reseña, Respuesta, Favorito
from users.models import Perfil


def agregar_voto(petición, id_producto):
    """Permite a un usuario dar 'Like' a un producto (máximo uno por usuario)."""
    if petición.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    usuario_id = petición.session.get('usuario_id')
    if not usuario_id:
        return JsonResponse({'error': 'Debes iniciar sesión para votar.'}, status=401)

    producto = get_object_or_404(Producto, id=id_producto)
    
    try:
        perfil = Perfil.objects.get(id=usuario_id)
        
        # Lógica de alternancia (voto/quitar voto)
        voto_existente = Voto.objects.filter(usuario=perfil, producto=producto).first()
        
        if voto_existente:
            voto_existente.delete()
            acción = 'removido'
        else:
            Voto.objects.create(usuario=perfil, producto=producto)
            acción = 'agregado'
            
        return JsonResponse({
            'success': True, 
            'accion': acción,
            'conteo': producto.votos.count()
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def agregar_reseña(petición, id_producto):
    """Permite a un usuario registrado dejar un comentario y calificación."""
    producto = get_object_or_404(Producto, id=id_producto)
    
    if petición.method != 'POST':
        return redirect('products:detail', enlace=producto.enlace)

    usuario_id = petición.session.get('usuario_id')
    if not usuario_id:
        from django.contrib import messages
        messages.error(petición, 'Debes iniciar sesión para dejar una reseña.')
        return redirect('users:login')

    calificación = petición.POST.get('calificacion')
    comentario = petición.POST.get('comentario', '').strip()

    if not calificación or not comentario:
        from django.contrib import messages
        messages.error(petición, 'Por favor completa la calificación y el comentario.')
        return redirect('products:detail', enlace=producto.enlace)

    try:
        perfil = Perfil.objects.get(id=usuario_id)
        
        # Crear la reseña técnica
        Reseña.objects.create(
            usuario=perfil,
            producto=producto,
            calificacion=int(calificación),
            comentario=comentario
        )
        
        from django.contrib import messages
        messages.success(petición, '¡Gracias por compartir tu experiencia!')
    except Exception as e:
        from django.contrib import messages
        messages.error(petición, f'Fallo al guardar reseña: {str(e)}')

    return redirect('products:detail', enlace=producto.enlace)


def agregar_respuesta(petición, id_reseña):
    """Responder a una reseña existente (comunidad)."""
    if petición.method != 'POST':
        return JsonResponse({'error': 'No permitido'}, status=405)

    usuario_id = petición.session.get('usuario_id')
    if not usuario_id:
        return JsonResponse({'error': 'Inicia sesión para responder.'}, status=401)

    reseña = get_object_or_404(Reseña, id=id_reseña)
    contenido = petición.POST.get('contenido', '').strip()

    if not contenido:
        return JsonResponse({'error': 'La respuesta está vacía'}, status=400)

    try:
        perfil = Perfil.objects.get(id=usuario_id)
        respuesta = Respuesta.objects.create(
            reseña=reseña,
            usuario=perfil,
            contenido=contenido
        )
        
        return JsonResponse({
            'success': True,
            'usuario': perfil.nombre_mostrado,
            'contenido': respuesta.contenido,
            'fecha': 'Hace un momento'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def alternar_favorito(petición, id_producto):
    """Añadir o quitar producto de la sección de Favoritos del usuario."""
    if petición.method != 'POST':
        return JsonResponse({'error': 'No permitido'}, status=405)

    usuario_id = petición.session.get('usuario_id')
    if not usuario_id:
        return JsonResponse({'error': 'Inicia sesión para guardar favoritos.'}, status=401)

    producto = get_object_or_404(Producto, id=id_producto)
    
    try:
        perfil = Perfil.objects.get(id=usuario_id)
        favorito_existente = Favorito.objects.filter(usuario=perfil, producto=producto).first()
        
        if favorito_existente:
            favorito_existente.delete()
            es_favorito = False
        else:
            Favorito.objects.create(usuario=perfil, producto=producto)
            es_favorito = True
            
        return JsonResponse({
            'success': True,
            'es_favorito': es_favorito
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
