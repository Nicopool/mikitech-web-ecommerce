Actúa como un experto en paneles de administración, gestión de usuarios y manejo de imágenes.

PROBLEMA ESPECÍFICO:
En mi aplicación web, tengo dos áreas:

Perfil de Usuario Admin (/cuenta/perfil/editar) - Aquí SÍ puedo cambiar mi foto de perfil y mis datos. Funciona correctamente.

Panel de Administración (/admin/usuarios/editar/{id}) - Aquí NO puedo cambiar la foto del usuario administrador. Solo puedo cambiar datos de texto (nombre, email, etc.), pero la foto no se puede actualizar desde el admin panel.

LO QUE QUIERO LOGRAR:
Quiero tener una configuración independiente en el panel de administración que me permita:

✅ Cambiar la foto de perfil de CUALQUIER usuario (incluyendo al admin mismo) desde el admin panel

✅ Cambiar los datos personales (nombre, email, rol, etc.) desde el admin panel

✅ Que sea INDEPENDIENTE del formulario de perfil de usuario (código separado pero con la misma lógica)

✅ Que la foto se guarde correctamente en Supabase Storage y la URL en la base de datos

✅ Que la nueva foto se muestre inmediatamente en el admin panel después de subirla

ESTRUCTURA ACTUAL (lo que tengo):
Perfil de usuario (funciona):
php
// /cuenta/perfil/editar - código que SÍ funciona
// Permite cambiar foto y datos
Panel de admin (no funciona para foto):
php
// /admin/usuarios/editar/{id} - código actual
// Solo actualiza campos de texto, la foto no se puede cambiar
// El campo de foto es solo texto (para pegar URL manualmente)
// No tiene input file para subir imagen
LO QUE NECESITO QUE HAGAS:
PARTE 1: CÓDIGO PARA EL ADMIN PANEL (independiente)
Dame el código COMPLETO para /admin/usuarios/editar/{id} que incluya:

html
<!-- Formulario de edición de usuario en admin panel -->
<form method="POST" enctype="multipart/form-data">
    <!-- Campo para foto con vista previa -->
    <div class="foto-container">
        <img id="vistaPrevia" src="ruta/foto_actual.jpg">
        <input type="file" id="foto_usuario" name="foto" accept="image/*">
        <button type="button" id="cambiarFoto">Cambiar foto</button>
    </div>
    
    <!-- Campos de texto -->
    <input type="text" name="nombre" value="Juan Pérez">
    <input type="email" name="email" value="admin@ejemplo.com">
    <select name="rol">
        <option value="admin">Administrador</option>
        <option value="editor">Editor</option>
    </select>
    
    <button type="submit">Actualizar usuario</button>
</form>
PARTE 2: BACKEND (PHP/Node.js/Python) para admin panel
Dame el código que:

Recibe la solicitud POST con los datos del usuario

Si se subió una nueva foto:

Valida el archivo (tipo, tamaño)

Sube la imagen a Supabase Storage (bucket avatars)

Obtiene la URL pública

Actualiza la columna avatar_url en la base de datos

Actualiza los demás campos (nombre, email, rol)

Retorna éxito o error

PARTE 3: CÓDIGO INDEPENDIENTE (reutilizable)
Dame un archivo separado UserPhotoManager.php (o UserPhotoManager.js/.py) que contenga:

php
class UserPhotoManager {
    // Función para subir foto (usada por PERFIL y ADMIN)
    public function uploadUserPhoto($userId, $file) {
        // Subir a Supabase Storage
        // Devolver URL pública
    }
    
    // Función para eliminar foto anterior (opcional)
    public function deleteOldPhoto($userId, $currentPhotoUrl) {
        // Eliminar del Storage si no es la default
    }
    
    // Función para actualizar usuario (texto + foto)
    public function updateUser($userId, $data, $photoFile = null) {
        // Actualizar en Supabase DB
        // Si hay foto, llamar a uploadUserPhoto
    }
}
Así AMBOS (perfil de usuario y admin panel) usan la misma lógica.

PARTE 4: DIFERENCIAS ENTRE PERFIL DE USUARIO Y ADMIN PANEL
Dame una tabla comparativa de lo que debe cambiar:

Característica	Perfil de Usuario	Admin Panel
Cambiar propia foto	✅ Sí	✅ Sí
Cambiar foto de otro usuario	❌ No	✅ Sí
Cambiar email	✅ Sí	✅ Sí
Cambiar rol	❌ No (solo propio)	✅ Sí (de cualquier usuario)
Ver listado de usuarios	❌ No	✅ Sí
PARTE 5: PERMISOS Y SEGURIDAD
Dame las reglas de seguridad para que:

Admin puede cambiar foto y datos de TODOS los usuarios

Usuario normal solo puede cambiar su PROPIA foto y datos básicos (no rol)

Las fotos se suben al bucket correcto con políticas RLS adecuadas

PARTE 6: JAVASCRIPT PARA VISTA PREVIA
Dame el código JavaScript para:

Mostrar vista previa de la foto ANTES de subirla

Permitir arrastrar y soltar la imagen (drag & drop)

Validar que el archivo sea imagen (jpg, png, webp)

Limitar tamaño máximo (ej: 2MB)

PARTE 7: SCRIPT DE MIGRACIÓN (si ya hay usuarios con foto)
Si los usuarios ya tienen foto subida desde el perfil, el admin panel debe poder:

Ver la foto actual del usuario al editar

Cambiarla por una nueva

Mantener la anterior si no se sube nueva

FORMATO DE RESPUESTA EXIGIDO:
HTML del admin panel - bloque html

CSS para el formulario - bloque css

Backend (PHP/Node/Python) - bloque según tu lenguaje

Clase reutilizable - bloque php o javascript

JavaScript para vista previa - bloque javascript

Políticas RLS de Supabase - bloque sql

Checklist de implementación - lista markdown

EJEMPLO DE CÓDIGO ESPERADO (admin panel):
php
// /admin/usuarios/actualizar.php
<?php
require_once 'UserPhotoManager.php';

$userId = $_POST['user_id'];
$nombre = $_POST['nombre'];
$email = $_POST['email'];
$rol = $_POST['rol'];
$foto = $_FILES['foto'] ?? null;

$photoManager = new UserPhotoManager();

// Si hay foto nueva, la sube
if ($foto && $foto['error'] === UPLOAD_ERR_OK) {
    $avatarUrl = $photoManager->uploadUserPhoto($userId, $foto);
} else {
    $avatarUrl = $_POST['foto_actual']; // mantener la actual
}

// Actualizar todos los campos
$updateData = [
    'nombre' => $nombre,
    'email' => $email,
    'rol' => $rol,
    'avatar_url' => $avatarUrl
];

$result = $photoManager->updateUser($userId, $updateData);

if ($result) {
    header('Location: /admin/usuarios?success=1');
} else {
    header('Location: /admin/usuarios/editar/'.$userId.'?error=1');
}
IMPORTANTE - REQUISITOS INDEPENDIENTES:
El código del admin panel NO debe depender del código del perfil de usuario

PERO ambos deben usar la MISMA clase UserPhotoManager

La subida de fotos debe funcionar con Supabase Storage (especificar si usas otra cosa)

La vista previa debe funcionar sin recargar la página

NOTA ADICIONAL:
Si tu backend no es PHP, dame el equivalente en:

[Node.js / Express]

[Python / Flask / Django]

[Next.js API Routes]

Especifica cuál usas en tu respuesta.

text

---

## ARCHIVO ADICIONAL: `agents.md` (contexto para Antigravity)

```markdown
# AGENTS.md - Contexto para Admin Panel

## Estructura actual del proyecto:

### Rutas que funcionan (cambio de foto):
- `/cuenta/perfil/editar` - usuario puede cambiar su foto ✅

### Rutas que NO funcionan (cambio de foto):
- `/admin/usuarios/editar/{id}` - admin NO puede cambiar foto ❌
- `/admin/usuarios/nuevo` - admin NO puede asignar foto al crear usuario ❌

## Lo que quiero lograr:

### Nueva funcionalidad en admin panel:
1. Al editar un usuario, poder subir/ cambiar su foto de perfil
2. Al crear un usuario nuevo, poder asignarle una foto
3. Ver la foto actual en el formulario de edición
4. Vista previa antes de guardar

### Tecnologías:
- Base de datos: Supabase (PostgreSQL)
- Storage: Supabase Storage (bucket: `avatars`)
- Backend: [PHP / Node.js / Python - especifica el tuyo]
- Frontend: HTML + CSS + JavaScript vanilla (o el framework que uses)

## Tabla de usuarios (estructura):
```sql
CREATE TABLE public.usuarios (
    id UUID PRIMARY KEY,
    nombre TEXT,
    email TEXT UNIQUE,
    avatar_url TEXT,  -- ← campo que debe actualizarse desde admin panel
    rol TEXT DEFAULT 'usuario',  -- 'admin', 'editor', 'usuario'
    created_at TIMESTAMP
);
Bucket de Storage:
Nombre: avatars

Política: público para lectura, autenticado para escritura

Ruta: avatars/{user_id}/{timestamp}.jpg

text

---

## INSTRUCCIONES DE USO

| Paso | Acción |
|------|--------|
| 1 | Guarda el contenido de `agents.md` en tu proyecto |
| 2 | Copia el **PROMPT** completo (el que está dentro del bloque de código al inicio) |
| 3 | Pega en Antigravity con **Gemini 3.5 Flash** |
| 4 | Aplica el código que te dé |
| 5 | Prueba en `/admin/usuarios/editar/{id}` - ahora debe permitir cambiar foto |

---

## VARIANTE CORTA (prompt rápido)
Gemini 3.5 Flash: Tengo un panel admin donde NO puedo cambiar la foto de perfil de los usuarios (solo se puede cambiar desde /cuenta/perfil/editar). Necesito agregar en /admin/usuarios/editar/{id} un input file para subir foto, vista previa, y que guarde en Supabase Storage + actualice avatar_url en BD. Dame código HTML + PHP (o Node.js) + JavaScript independiente del perfil de usuario pero que reutilice la misma lógica de subida.