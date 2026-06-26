@# PROMPT PARA ANTIGRAVITY - SISTEMA DE ROLES Y PERMISOS

## CONTEXTO ACTUAL
Mi aplicación NO tiene implementado un sistema de roles y permisos. Actualmente:
- No existe diferenciación entre usuario normal, admin, superadmin, etc.
- Cualquier usuario puede acceder a cualquier funcionalidad
- No hay un modelo entidad-relación definido para usuarios/roles/permisos
- La base de datos no tiene tablas de roles ni permisos
- El frontend muestra botones y opciones a todos por igual
- Las rutas/endpoints del backend no validan autorización

## OBJETIVO PRINCIPAL
Quiero implementar un sistema completo de Roles y Permisos (RBAC) que incluya:

### 1. MODELO ENTIDAD-RELACIÓN (MER)
Necesito que diseñes el modelo de datos con las siguientes entidades:

- **Usuarios** (ya existe, pero hay que agregarle role_id)
- **Roles** (admin, usuario, superadmin, invitado, etc.)
- **Permisos** (acciones específicas: crear_usuario, eliminar_producto, ver_reportes, etc.)
- **Roles_Permisos** (tabla pivote que relaciona roles con permisos)

**Requisitos del MER:**
- Diagrama entidad-relación en texto o formato Mermaid
- Relaciones claras (1:N, N:N)
- Tipos de datos sugeridos para cada campo
- Claves primarias y foráneas bien definidas
- Índices recomendados para búsquedas frecuentes

### 2. ESTRUCTURA DE ROLES SUGERIDA
Define al menos estos roles con sus permisos específicos:

- **SUPERADMIN**: Acceso total a todo (gestión de usuarios, roles, permisos, configuraciones)
- **ADMIN**: Gestión de contenido, usuarios (excepto roles/permisos), reportes
- **USUARIO**: Acceso a su perfil, funcionalidades básicas de la app
- **INVITADO**: Solo lectura de contenido público
- **MODERADOR**: Moderación de contenido (aprobar/rechazar publicaciones)

### 3. IMPLEMENTACIÓN BACKEND (API/REST)
Necesito código para:

- **Middleware de autenticación** que verifique token JWT y extraiga el rol
- **Middleware de autorización** que verifique si el usuario tiene el permiso específico
- **Endpoints protegidos** con decoradores o anotaciones según el rol
- **Sistema de verificación** en cada endpoint: "¿Este usuario tiene permiso para ejecutar esta acción?"

**Ejemplo de lógica:**