"""URLs del panel administrativo — con pasarela de seguridad SENA-2026"""

from django.urls import path
from core import admin_views

urlpatterns = [
    path('pasarela/', admin_views.pasarela, name='admin_gateway'),
    path('login/', admin_views.login_administrador, name='admin_login'),
    path('registro/', admin_views.registro_administrador, name='admin_register'),
    path('logout/', admin_views.cerrar_sesion_administrador, name='admin_logout'),
    path('', admin_views.tablero_administrador, name='admin_dashboard'),
    
    # Gestión de productos
    path('productos/', admin_views.gestion_productos, name='admin_products'),
    path('productos/crear/', admin_views.crear_producto, name='admin_product_create'),
    path('productos/editar/<str:id_producto>/', admin_views.editar_producto, name='admin_product_edit'),
    path('productos/eliminar/<str:id_producto>/', admin_views.eliminar_producto, name='admin_product_delete'),
    path('productos/carga-masiva/', admin_views.carga_masiva_productos, name='admin_product_bulk_upload'),
    path('productos/plantilla-excel/', admin_views.descargar_plantilla_excel, name='admin_excel_template'),
    
    # Gestión de categorías
    path('categorias/', admin_views.gestion_categorias, name='admin_categories'),
    path('categorias/crear/', admin_views.crear_categoria, name='admin_category_create'),
    path('categorias/editar/<str:id_cat>/', admin_views.editar_categoria, name='admin_category_edit'),
    path('categorias/eliminar/<str:id_cat>/', admin_views.eliminar_categoria, name='admin_category_delete'),
    
    # Gestión de usuarios
    path('usuarios/', admin_views.gestion_usuarios, name='admin_users'),
    
    # Moderación de interacciones
    path('resenas/', admin_views.moderacion_resenas, name='admin_reviews'),
    path('resenas/notificar/<str:id_resena>/', admin_views.enviar_notificacion_resena, name='admin_review_notify'),
    path('resenas/eliminar/<str:id_resena>/', admin_views.eliminar_resena, name='admin_review_delete'),
    
    # Logística y Despachos
    path('logistica/', admin_views.gestion_logistica, name='admin_logistics'),
    path('logistica/asignar/<str:id_pedido>/', admin_views.asignar_repartidor_admin, name='admin_assign_driver'),
    path('logistica/actualizar/<str:id_pedido>/', admin_views.cambiar_estado_pedido, name='admin_order_update'),
    path('logistica/factura/<str:id_pedido>/', admin_views.ver_factura_pedido, name='admin_order_invoice'),
    
    # Reportes
    path('reportes/', admin_views.reportes_dashboard, name='admin_reports'),
]
