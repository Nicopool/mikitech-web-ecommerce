from django.db import migrations
import uuid

def populate_roles_and_permissions(apps, schema_editor):
    Rol = apps.get_model('users', 'Rol')
    Permiso = apps.get_model('users', 'Permiso')
    
    # 1. Definir los permisos y crearlos
    permisos_def = [
        # Usuarios
        ('gestionar_usuarios', 'Gestionar Usuarios'),
        ('ver_usuarios', 'Ver Usuarios'),
        # RBAC
        ('gestionar_rbac', 'Gestionar Roles y Permisos'),
        # Productos
        ('crear_producto', 'Crear Producto'),
        ('editar_producto', 'Editar Producto'),
        ('eliminar_producto', 'Eliminar Producto'),
        ('ver_catalogo', 'Ver Catálogo'),
        # Pedidos
        ('crear_pedido', 'Crear Pedido'),
        ('gestionar_pedidos', 'Gestionar Pedidos'),
        ('entregar_pedido', 'Entregar Pedido'),
        # Reportes y Contenido
        ('ver_reportes', 'Ver Reportes'),
        ('moderar_contenido', 'Moderar Contenido'),
    ]
    
    permisos_instancias = {}
    for codigo, nombre in permisos_def:
        permiso, _ = Permiso.objects.get_or_create(
            codigo=codigo,
            defaults={'nombre': nombre, 'id': uuid.uuid4()}
        )
        permisos_instancias[codigo] = permiso

    # 2. Definir los roles y asociar sus permisos
    roles_def = {
        'superadmin': {
            'nombre': 'Super Administrador',
            'permisos': [
                'gestionar_usuarios', 'ver_usuarios', 'gestionar_rbac',
                'crear_producto', 'editar_producto', 'eliminar_producto', 'ver_catalogo',
                'crear_pedido', 'gestionar_pedidos', 'ver_reportes', 'moderar_contenido'
            ]
        },
        'admin': {
            'nombre': 'Administrador',
            'permisos': [
                'ver_usuarios', 'crear_producto', 'editar_producto', 'ver_catalogo',
                'gestionar_pedidos', 'ver_reportes'
            ]
        },
        'moderador': {
            'nombre': 'Moderador',
            'permisos': ['ver_catalogo', 'moderar_contenido']
        },
        'repartidor': {
            'nombre': 'Repartidor',
            'permisos': ['entregar_pedido']
        },
        'client': {
            'nombre': 'Cliente',
            'permisos': ['ver_catalogo', 'crear_pedido']
        },
        'guest': {
            'nombre': 'Invitado',
            'permisos': ['ver_catalogo']
        }
    }

    for code, info in roles_def.items():
        rol, _ = Rol.objects.get_or_create(
            codigo=code,
            defaults={'nombre': info['nombre'], 'id': uuid.uuid4()}
        )
        # Asignar permisos
        permisos_a_asignar = [permisos_instancias[p_code] for p_code in info['permisos'] if p_code in permisos_instancias]
        rol.permisos.set(permisos_a_asignar)


def unload_roles_and_permissions(apps, schema_editor):
    Rol = apps.get_model('users', 'Rol')
    Permiso = apps.get_model('users', 'Permiso')
    Rol.objects.all().delete()
    Permiso.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_permiso_rol_perfil_rol_rbac'),
    ]

    operations = [
        migrations.RunPython(populate_roles_and_permissions, unload_roles_and_permissions),
    ]
