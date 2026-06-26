def global_context(request):
    """Contexto global para todas las plantillas — MIKITECH.
    Las categorías se cachean 5 minutos para evitar queries a Supabase en cada petición.
    """
    from django.core.cache import cache
    
    # Categorías cacheadas (evita 1 query a Supabase por petición)
    nav_categorias = cache.get('nav_categorias')
    if nav_categorias is None:
        from products.models import Categoria
        nav_categorias = list(Categoria.objects.all().order_by('nombre'))
        cache.set('nav_categorias', nav_categorias, 300)  # 5 min
    
    # Conteo de carrito (solo de sesión, sin DB)
    carrito = request.session.get('cart', {})
    conteo_carrito = sum(carrito.values()) if carrito else 0
    
    # Conteo de notificaciones (si hay sesión)
    conteo_notificaciones = 0
    notificaciones_previas = []
    usuario_id = request.session.get('usuario_id')
    
    if usuario_id:
        # Si el usuario es admin, asegurar alertas del sistema antes de cargar
        if request.session.get('rol_usuario') == 'admin':
            try:
                from core.admin_views import asegurar_notificaciones_admin
                asegurar_notificaciones_admin(usuario_id)
            except Exception as e:
                print("Error al generar notificaciones de admin:", e)
                
        from users.models import Notificacion
        todas_notif_no_leidas = list(
            Notificacion.objects.filter(
                usuario_id=usuario_id,
                esta_leida=False
            ).order_by('-creado_el')
        )
        
        # Mutar para extraer mensaje visible y link
        for n in todas_notif_no_leidas:
            if '|' in n.mensaje:
                partes = n.mensaje.split('|')
                n.mensaje_visible = partes[0]
                n.url_destino = partes[1]
            else:
                n.mensaje_visible = n.mensaje
                n.url_destino = '#'
                
        conteo_notificaciones = len(todas_notif_no_leidas)
        notificaciones_previas = todas_notif_no_leidas[:5]  # Mostrar máximo 5
    
    from django.conf import settings
    
    return {
        'nav_categorias': nav_categorias,
        'conteo_carrito': conteo_carrito,
        'conteo_notificaciones': conteo_notificaciones,
        'ultimas_notificaciones': notificaciones_previas,
        'debug': settings.DEBUG,
    }
