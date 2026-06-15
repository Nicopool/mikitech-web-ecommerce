# PROMPTS PARA CORREGIR ERRORES EN ANTIGRAVITY (O CUALQUIER IA)

> Este archivo contiene todos los prompts necesarios para corregir los errores de tu sitio web.
> Copia y pega cada prompt en Antigravity en el orden indicado.

---

## ÍNDICE DE PROBLEMAS A CORREGIR

| # | Problema | Dónde ocurre |
|---|----------|---------------|
| 1 | Las fotos no se guardan en la base de datos | Toda la página |
| 2 | Las fotos no se muestran después de guardar | Cuenta/perfil/editar |
| 3 | Las fotos no se guardan al subir un producto | Panel de productos |
| 4 | Los PDFs no descargan | Panel admin |
| 5 | Los reportes fallan | Panel usuario |
| 6 | Los PDFs son inconsistentes (diferente formato/logo) | Admin y usuario |
| 7 | El logo no aparece o se ve mal en los PDFs | Todos los PDFs |
| 8 | Diseño responsive roto en móvil | Panel de productos (GABINETES, etc.) |

---

## PROMPT 1: CORRECCIÓN DE FOTOS QUE NO SE GUARDAN EN BD (URGENTE)

> ⚠️ **EJECUTA ESTE PRIMERO** - Es el problema más crítico.

> Copia y pega esto exactamente en Antigravity:
Necesito que actúes como un experto en backend, bases de datos y manejo de archivos en producción.

Tengo un problema GRAVE que ocurre en el servidor web (en local funciona todo bien):

Problema principal:
Las fotos NO se guardan en la base de datos. Esto pasa en TODA la página, específicamente:

En la sección CUENTA/PERFIL/EDITAR - al subir una foto de perfil, no se guarda ni se muestra.

Al SUBIR UN PRODUCTO - las fotos del producto no se guardan en la base de datos.

En cualquier otro lugar donde se suba una imagen, el mismo error ocurre.

Síntomas:
La foto parece subirse (no da error visible), pero al recargar la página no aparece.

En la base de datos, el campo de la foto está vacío o con una ruta incorrecta.

Las imágenes físicas pueden o no estar en la carpeta del servidor.

Lo que necesito que hagas:

1. Diagnóstico de causas probables (las 7 más comunes)
Rutas relativas vs absolutas en producción

Permisos de carpetas (uploads/, images/, productos/, perfiles/)

Tamaño de archivo excedido (php.ini, nginx, .htaccess)

Error en la consulta SQL (campo incorrecto, tipo de dato)

Problema con el nombre del archivo (caracteres especiales, espacios)

El formulario no tiene enctype="multipart/form-data"

Variable $_FILES vacía por configuración del servidor

2. Solución paso a paso para cada causa
Comandos específicos para corregir permisos (Linux/Windows)

Código para depurar la subida (var_dump($_FILES) y errores)

Cómo verificar que la carpeta de destino existe

Cómo generar nombres únicos para evitar caché

3. Código de ejemplo CORREGIDO para:
Subir foto de perfil (cuenta/perfil/editar)

Subir foto de producto

Guardar la ruta en base de datos

Mostrar la foto correctamente

4. Script de verificación automática
Que revise:

Permisos de carpetas de uploads

Configuración de php.ini (upload_max_filesize, post_max_size)

Si la carpeta de destino existe

Si hay errores en los logs del servidor

5. Checklist de despliegue para fotos
Qué revisar CADA VEZ que se sube el sitio a producción

Cómo asegurar que las fotos se migren correctamente

Nota adicional:
Las fotos que ya existían antes en local no se ven en producción. Necesito también un script para migrar las imágenes existentes de local a producción con las rutas correctas.

Dame TODO en orden: diagnóstico, soluciones, código listo para copiar y pegar, y comandos.

---

## PROMPT 2: CORRECCIÓN DE PANEL ADMIN, PDFS, REPORTES Y LOGO

Necesito que actúes como un experto en despliegue web y solución de errores en producción.

Tengo que corregir los siguientes problemas que ocurren SOLO en el servidor web (en local funciona todo bien):

Problemas a corregir:
Panel de administrador (admin) - Descarga de PDFs no funciona

Los enlaces de descarga de PDF están rotos en el panel admin.

En local funcionan, al subirlos a la web dan error 404 o no cargan.

Panel de usuario - Reportes fallando

Todos los reportes (en PDF) que deberían generarse o descargarse desde el panel de usuario están fallando.

Diferentes reportes tienen diferentes errores (unos no generan, otros descargan vacíos, otros dan 404).

Inconsistencia en PDFs

Los PDFs no son iguales entre sí (cambian formatos, estilos, márgenes o contenidos).

Necesito que TODOS los PDFs (tanto en admin como en usuario) tengan el MISMO formato, logo, tipografía y estructura.

Logo no aparece o se ve mal

El logo no se muestra correctamente en los PDFs generados.

En algunos PDFs aparece, en otros no, o se ve distorsionado.

Lo que necesito que hagas:
Diagnóstico: Dame una lista de las 5 causas más probables.

Solución paso a paso para corregir las rutas de los PDFs.

Código unificado para generar reportes consistentes (PHP/Node/Python).

Script de verificación de PDFs y logo.

Checklist de despliegue para PDFs.

Dame el código, comandos y explicaciones ordenadas en secciones claras.

---

## PROMPT 3: CORRECCIÓN DE DISEÑO RESPONSIVE (MÓVIL)

Necesito CSS responsive para móvil.

Tengo un panel de productos que en móvil se rompe:

Título "GABINETES Y REFRIGERACIÓN PREMIUM" se desborda

Botón "EXPLORAR GABINETES" se corta

Tarjetas de productos (TODOS LOS PRODUCTOS) se superponen

Precios ($3.000.000, $2.700.000) se ven mal

Etiquetas (STOCK DISPONIBLE, AGOTADO) se superponen

Necesito:

CSS completo con media queries para 480px, 768px y 1024px

Las tarjetas a 1 columna en móvil

Meta tag viewport

Checklist de verificación

Dame el código directamente.

---

## PROMPT 4: PROMPTAZO ÚNICO (TODOS LOS PROBLEMAS JUNTOS)

Soy desarrollador web y tengo UNA PÁGINA COMPLETA EN PRODUCCIÓN con múltiples errores que NO ocurren en localhost. Necesito que me des la solución COMPLETA para todos estos problemas:

LISTA DE ERRORES (todos solo en producción):
ERROR 1 - FOTOS
Las fotos no se guardan en la base de datos

Sucede en: cuenta/perfil/editar y al subir productos

En BD el campo foto queda vacío

ERROR 2 - PDFs ADMIN
Los PDFs no descargan desde el panel admin (error 404)

ERROR 3 - REPORTES USUARIO
Los reportes en PDF fallan (diferentes errores según el reporte)

ERROR 4 - PDFs INCONSISTENTES
Cada PDF tiene formato, logo y estilo diferente

ERROR 5 - LOGO
El logo no aparece en algunos PDFs o se ve mal

ERROR 6 - DISEÑO RESPONSIVE
El panel de productos se rompe en móvil (título, tarjetas, precios, etiquetas)

LO QUE NECESITO:
Para CADA error:

Causa más probable

Solución paso a paso con comandos y código

Script de verificación

Además:

Un script que unifique TODOS los PDFs con el mismo logo y formato

Un checklist de despliegue para que NUNCA más vuelvan a ocurrir estos errores

Comandos para migrar fotos y PDFs de local a producción

Dame TODO en un solo mensaje, ordenado por error, con código listo para copiar y pegar.

---

## INSTRUCCIONES RÁPIDAS DE USO

| Paso | Acción |
|------|--------|
+| 1 | Copia el **PROMPT 1** y pégalo en Antigravity → resuelve lo de las FOTOS |
+| 2 | Copia el **PROMPT 2** y pégalo en Antigravity → resuelve lo de PDFs y REPORTES |
+| 3 | Copia el **PROMPT 3** y pégalo en Antigravity → resuelve el DISEÑO RESPONSIVE |
+| 4 | Opcional: Copia el **PROMPT 4** si quieres todo junto |

---

## COMANDOS ÚTILES PARA CORREGIR PERMISOS (ejecutar en el servidor)

```bash
# Corregir permisos de carpetas de imágenes
find /ruta/web/uploads -type d -exec chmod 755 {} \;
find /ruta/web/uploads -type f -exec chmod 644 {} \;

# Corregir permisos de carpetas de PDFs
find /ruta/web/pdfs -type d -exec chmod 755 {} \;
find /ruta/web/pdfs -type f -exec chmod 644 {} \;

# Verificar dueño de archivos
chown -R www-data:www-data /ruta/web/uploads
chown -R www-data:www-data /ruta/web/pdfs

# Verificar configuración PHP
php -i | grep upload_max_filesize
php -i | grep post_max_size
```

RECORDATORIO FINAL
Antes de subir cualquier cosa a producción, ejecuta estos 3 pasos:

Verificar permisos de carpetas de imágenes y PDFs

Verificar que las rutas sean absolutas (empiecen con /)

Ejecutar script de verificación automática
