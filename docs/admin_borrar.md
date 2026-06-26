@# PROMPT PARA ANTIGRAVITY - SISTEMA DE INVITACIÓN PARA ADMINISTRADORES

## CONTEXTO ACTUAL
Mi aplicación actualmente tiene un registro público de usuarios donde:
- Cualquier persona puede registrarse como administrador
- El formulario de registro de admin está visible para todos
- No hay control sobre quién se convierte en administrador
- Los admins se crean directamente en la base de datos

## OBJETIVO PRINCIPAL
Quiero implementar un sistema **SOLO POR INVITACIÓN** donde:

1. **ELIMINAR** completamente el registro público de administradores
2. **ELIMINAR** la vista/página de registro de admin
3. **ELIMINAR** cualquier endpoint API que permita crear admins públicamente
4. **IMPLEMENTAR** un sistema donde YO (superadmin) pueda:
   - Crear usuarios administradores desde un panel privado
   - Generar credenciales únicas (usuario + contraseña temporales)
   - Enviar un correo de invitación con las credenciales
   - El admin invitado debe usar esas credenciales para iniciar sesión
   - Forzar cambio de contraseña en el primer inicio de sesión

## REQUERIMIENTOS DETALLADOS

### 1. ELIMINACIÓN DEL REGISTRO PÚBLICO

**Frontend:**
- Eliminar completamente el componente/página de "Registro de Administrador"
- Eliminar cualquier botón/enlace que redirija a registro de admin
- Eliminar rutas como `/admin/register`, `/register-admin`, `/signup-admin`
- Si existe un registro general de usuarios, asegurar que solo cree usuarios normales (rol = 'usuario')

**Backend:**
- Eliminar endpoint `POST /api/auth/register-admin` o similar
- Eliminar cualquier controlador que permita crear admins sin verificación
- Deshabilitar cualquier método que asigne rol 'admin' sin autorización
- Modificar el registro normal de usuarios para que SOLO pueda crear rol 'usuario'

**Base de Datos:**
- No eliminar la tabla de usuarios (solo ajustar lógica de creación)
- Asegurar que el rol 'admin' solo pueda ser asignado por el sistema de invitación

### 2. SISTEMA DE INVITACIÓN PARA ADMINISTRADORES

**Panel de Superadmin (solo para mí):**
- Crear una sección "Gestionar Administradores" en el dashboard de superadmin
- Formulario para invitar nuevo admin con:
  - Campo: Email del administrador (obligatorio)
  - Campo: Nombre completo (opcional)
  - Campo: Notas internas (opcional)
- Botón "Enviar Invitación" que genera credenciales y envía correo

**Generación de Credenciales:**
- **Usuario único:** Generado automáticamente con formato:
  - `admin_[nombre][apellido_inicial][numeros]` 
  - Ejemplo: `admin_juanp_3829`
  - O usar email como usuario: `juan.perez@empresa.com`
- **Contraseña temporal:** Generada automáticamente con alta seguridad:
  - Mínimo 12 caracteres
  - Mayúsculas, minúsculas, números y símbolos
  - Ejemplo: `Xk9#mP2$vL@7`
  - Caduca después de 7 días si no se usa

**Correo de Invitación:**
- Enviar email con:
  - Saludo personalizado
  - Sus credenciales únicas (usuario + contraseña temporal)
  - Enlace de inicio de sesión (https://miapp.com/login)
  - Mensaje: "Esta es tu contraseña temporal, debes cambiarla al iniciar sesión"
  - Instrucciones claras de primeros pasos
  - Enlace para cambiar contraseña
  - Tiempo de expiración de la invitación

### 3. FLUJO DEL ADMIN INVITADO

**Primer inicio de sesión:**
1. Admin recibe correo con credenciales
2. Inicia sesión con usuario + contraseña temporal
3. **FORZAR** cambio de contraseña inmediato (redirigir a /change-password)
4. No permitir acceso al dashboard hasta cambiar contraseña
5. Mostrar modal/página de cambio de contraseña obligatorio

**Características de seguridad:**
- La contraseña temporal expira a los 7 días (si no la usa, debe pedir nueva invitación)
- La invitación expira a los 7 días (si no la acepta, se cancela)
- Log de todas las invitaciones enviadas (fecha, email, estado)
- Posibilidad de revocar una invitación antes de que sea aceptada
- Posibilidad de desactivar un admin activo

### 4. TABLAS/MODELOS NUEVOS (si es necesario)

**Tabla `invitaciones_admin` (o `admin_invitations`):**
- `id` (PK)
- `email` (string, unique)
- `nombre_completo` (string, nullable)
- `usuario_generado` (string, unique)
- `password_temporal_hash` (string)
- `fecha_envio` (timestamp)
- `fecha_expiracion` (timestamp, 7 días después)
- `estado` (enum: 'pendiente', 'aceptada', 'expirada', 'revocada')
- `notas_internas` (text, nullable)
- `creado_por` (FK → usuarios.id, el superadmin que invitó)
- `fecha_aceptacion` (timestamp, nullable)
- `ip_origen` (string, nullable)

**Modificar tabla `usuarios`:**
- Agregar campo `fecha_primer_login` (timestamp, nullable)
- Agregar campo `invitacion_id` (FK → invitaciones_admin.id, nullable)
- Agregar campo `password_cambiada` (boolean, default: false)

### 5. ENDPOINTS API REQUERIDOS

**Protegidos (solo superadmin):**
- `GET /api/admin/invitations` - Listar todas las invitaciones
- `POST /api/admin/invitations` - Crear nueva invitación
- `DELETE /api/admin/invitations/:id` - Revocar invitación
- `PUT /api/admin/users/:id/deactivate` - Desactivar admin
- `GET /api/admin/users` - Listar admins activos

**Públicos/Autenticados (admin invitado):**
- `POST /api/auth/verify-invitation` - Verificar si invitación es válida
- `POST /api/auth/accept-invitation` - Aceptar invitación y cambiar contraseña
- `POST /api/auth/resend-invitation` - Reenviar correo de invitación (solo si expiró)

### 6. MIDDLEWARES Y VALIDACIONES

**Validaciones en el login:**
```javascript
// Pseudocódigo
async function login(usuario, password) {
    const user = await findUserByUsername(usuario);
    
    // Verificar si es admin y fue invitado
    if (user.rol === 'admin' && !user.password_cambiada) {
        // Redirigir a cambio de contraseña OBLIGATORIO
        return { 
            success: true, 
            requiere_cambio_password: true,
            token: jwt_generado_con_permiso_limitado
        };
    }
    
    // Verificar que la invitación no haya expirado
    if (user.rol === 'admin') {
        const invitacion = await getInvitacionById(user.invitacion_id);
        if (invitacion.estado === 'expirada') {
            return { error: 'Tu invitación ha expirado. Contacta al administrador.' };
        }
    }
    
    // Login normal
    return { success: true, token: jwt_normal };
}
7. INTERFAZ DE USUARIO (UI)
Panel de Superadmin → Invitaciones:

Tabla con columnas: Email, Usuario, Fecha Envío, Estado (Pendiente/Aceptada/Expirada), Acciones

Botón "Nueva Invitación" → Modal con formulario

Indicadores visuales de invitaciones próximas a expirar (amarillo)

Indicadores de invitaciones expiradas (rojo)

Opción "Reenviar correo" para invitaciones pendientes

Página de Login para admin invitado:

Si es admin y no ha cambiado password, después de login:

Redirigir a /forced-password-change

Mostrar mensaje: "Es tu primera vez. Debes cambiar tu contraseña."

Formulario con: contraseña actual (temporal), nueva contraseña, confirmar

Correo de invitación (diseño):

html
Asunto: [App Name] - Has sido invitado como Administrador

Hola [Nombre],

Has sido invitado para ser administrador de [App Name].

Tus credenciales de acceso:
- Usuario: [usuario_generado]
- Contraseña temporal: [password_temporal]

⚠️ Esta contraseña es temporal y caducará en 7 días.
Por seguridad, deberás cambiarla en tu primer inicio de sesión.

Inicia sesión aquí: [LINK DE LOGIN]
¿Necesitas ayuda? Contacta a soporte@[app].com

Este enlace expirará en 7 días.
8. SEGURIDAD ADICIONAL
Rate limiting: Máximo 5 invitaciones por hora (evita spam)

Logs de auditoría: Registrar quién invitó, cuándo, desde qué IP

Doble factor: Opcional para admins (2FA)

Revocación inmediata: Poder desactivar un admin en segundos

Notificaciones: Alertar al superadmin cuando un admin acepta la invitación

9. MIGRACIONES Y SEEDS
Scripts necesarios:

Crear tabla admin_invitations

Agregar columnas a users (fecha_primer_login, invitacion_id, password_cambiada)

Insertar superadmin inicial (si no existe) con método seguro

Script de limpieza: eliminar invitaciones expiradas (cron job diario)

Script para verificar admins que no cambiaron password (alerta)

10. FLUJO COMPLETO (PASO A PASO)
text
1. Superadmin abre panel → "Gestionar Admins" → "Nueva Invitación"
2. Completa email y opcionales → Click "Enviar"
3. Sistema genera usuario y contraseña segura
4. Sistema guarda en tabla admin_invitations (estado: 'pendiente')
5. Sistema envía correo al email con credenciales
6. Admin recibe correo → Click en enlace de login
7. Admin inicia sesión con credenciales temporales
8. Sistema detecta que no ha cambiado password → Redirige a cambio forzado
9. Admin cambia password → Estado cambia a 'aceptada' y password_cambiada = true
10. Admin accede al dashboard con permisos completos
11. Superadmin recibe notificación: "Juan Pérez ha aceptado su invitación"
TECNOLOGÍAS QUE USO
[COMPLETA ESTO]

Backend: [Ej: Node.js/Express]

Frontend: [Ej: React/Next.js]

Base de datos: [Ej: PostgreSQL/MySQL]

Email: [Ej: Nodemailer, SendGrid, AWS SES]

Autenticación: [JWT + bcrypt]

ORM: [Ej: Prisma, TypeORM, Sequelize]

RESULTADO ESPERADO
Necesito el código completo para:

✅ Eliminar el registro público de admins (frontend + backend)

✅ Panel de invitaciones para superadmin

✅ Generación de credenciales únicas

✅ Envío de correos de invitación

✅ Flujo de primer login + cambio de contraseña forzado

✅ Tablas/migraciones necesarias

✅ Middlewares de seguridad

✅ Logs de auditoría

✅ Scripts de mantenimiento (limpieza, notificaciones)

NOTAS ADICIONALES
No quiero que NINGÚN usuario pueda registrarse como admin por sí mismo

Solo YO (superadmin) puedo crear admins mediante invitación

Las contraseñas temporales deben ser seguras y únicas

El usuario generado debe ser único (evitar duplicados)

La UI del panel de invitaciones debe ser intuitiva y limpia

Necesito que el flujo sea robusto y maneje casos edge (email inválido, expiración, etc.)

Por favor, proporciona una solución completa, segura y bien documentada.

text

---

## 📌 ¿Quieres que afine alguna parte específica?

Puedo ayudarte a adaptar este prompt si:

1. **Tienes un stack específico** (¿React + Node? ¿Laravel? ¿Django?)
2. **Quieres usar un servicio de email en particular** (SendGrid, AWS SES, Mailgun)
3. **Necesitas que el usuario sea el email** (en lugar de generar un username)
4. **Quieres añadir verificación de dominio** (solo emails de tu empresa pueden ser invitados)
5. **Necesitas un sistema de "múltiples superadmins"** (no solo tú)
