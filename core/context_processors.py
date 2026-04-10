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
    
    return {
        'nav_categorias': nav_categorias,
        'conteo_carrito': conteo_carrito,
    }
