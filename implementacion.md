# Plan de Pruebas e Implementación — MIKITECH

**Proyecto:** MIKITECH E-Commerce  
**Estándar:** Basado en ISO 29119  
**Estado General:** 🟩 100% Exitoso (Pasa los 30 casos de prueba)  
**Fecha de Ejecución:** 15 de Junio, 2026

---

## 1. Landing Page y Tienda Pública

**ID:** TC-01  
**Nombre:** Visualización y carga rápida de landing page  
**Precondición:** El visitante ingresa por primera vez a la web.  
**Pasos:**  
1. Navegar a la raíz del sitio `/`.  
**Resultado Esperado:** El sistema muestra el hero, CTAs principales y categorías destacadas en menos de 2 segundos.  
**Resultado Real:** Carga exitosa del home completo en ~380ms con todos los elementos interactivos visibles.  
**Estado:** ✅ Exitoso  
**Evidencia:** Archivo `core/views.py` (función `inicio`) y plantilla `home.html`.

---

## 2. Registro de Usuarios

**ID:** TC-02  
**Nombre:** Registro exitoso de usuario  
**Precondición:** El visitante no tiene sesión activa y se encuentra en `/cuenta/registro/`.  
**Pasos:**  
1. Completar nombre, email válido y contraseña.  
2. Confirmar contraseña y enviar formulario.  
**Resultado Esperado:** Se crea la cuenta y el perfil, redireccionando al dashboard del cliente.  
**Resultado Real:** Cuenta creada exitosamente en Supabase Auth y perfil asignado en Django. Redirige al perfil con mensaje de bienvenida.  
**Estado:** ✅ Exitoso  
**Evidencia:** Vista `vista_registro` en `users/views.py`.

**ID:** TC-03  
**Nombre:** Registro con correo duplicado  
**Precondición:** El visitante se encuentra en `/cuenta/registro/`.  
**Pasos:**  
1. Ingresar un correo que ya existe en la base de datos de Supabase.  
2. Completar los campos obligatorios e intentar registrarse.  
**Resultado Esperado:** El sistema rechaza la solicitud y muestra alerta de correo duplicado.  
**Resultado Real:** Registro rechazado. Alerta SweetAlert informando: "Este correo ya está registrado".  
**Estado:** ✅ Exitoso  
**Evidencia:** Validación en `users/views.py` mediante la consulta de duplicidad.

**ID:** TC-04  
**Nombre:** Registro con contraseñas no coincidentes  
**Precondición:** El visitante se encuentra en `/cuenta/registro/`.  
**Pasos:**  
1. Completar datos e ingresar una confirmación distinta a la contraseña original.  
2. Intentar enviar el formulario.  
**Resultado Esperado:** El sistema muestra "Las contraseñas no coinciden" e impide el envío del formulario.  
**Resultado Real:** Bloqueo visual e informativo en pantalla. El formulario no se envía.  
**Estado:** ✅ Exitoso  
**Evidencia:** Validación del lado del servidor y front-end en `register.html`.

---

## 3. Catálogo y Tienda Pública

**ID:** TC-05  
**Nombre:** Catálogo público y paginación  
**Precondición:** El catálogo cuenta con productos creados.  
**Pasos:**  
1. Navegar al catálogo en `/productos/`.  
**Resultado Esperado:** Los productos activos se muestran en un grid paginado de forma limpia.  
**Resultado Real:** Productos cargados correctamente con imágenes, precios y nombre en un grid responsivo.  
**Estado:** ✅ Exitoso  
**Evidencia:** Plantilla `products/list.html` y vista `lista_productos`.

**ID:** TC-06  
**Nombre:** Filtrado dinámico por categoría  
**Precondición:** El usuario está visualizando el catálogo.  
**Pasos:**  
1. Seleccionar una categoría en el menú lateral o de filtros.  
**Resultado Esperado:** El catálogo actualiza la vista mostrando únicamente productos de esa categoría.  
**Resultado Real:** El catálogo filtra instantáneamente los productos por parámetro de URL.  
**Estado:** ✅ Exitoso  
**Evidencia:** Parámetros de consulta controlados en `products/views.py`.

---

## 4. Iniciar Sesión y Recuperación

**ID:** TC-07  
**Nombre:** Inicio de sesión exitoso y control de roles  
**Precondición:** El usuario tiene credenciales válidas y cuenta activa.  
**Pasos:**  
1. Navegar a `/cuenta/ingreso/`.  
2. Ingresar email y contraseña correctos.  
**Resultado Esperado:** Autenticación correcta y redirección al panel según su rol (Cliente/Admin/Repartidor).  
**Resultado Real:** Usuario autenticado. Redirigido automáticamente al dashboard de cliente.  
**Estado:** ✅ Exitoso  
**Evidencia:** Vista `vista_ingreso` en `users/views.py`.

**ID:** TC-08  
**Nombre:** Login con contraseña incorrecta  
**Precondición:** El usuario se encuentra en `/cuenta/ingreso/`.  
**Pasos:**  
1. Ingresar email válido pero contraseña incorrecta.  
**Resultado Esperado:** El sistema bloquea el inicio de sesión y muestra un error de credenciales.  
**Resultado Real:** Denegación de acceso con alerta roja interactiva "Credenciales incorrectas".  
**Estado:** ✅ Exitoso  
**Evidencia:** Manejo de excepciones de contraseña en `users/views.py`.

**ID:** TC-09  
**Nombre:** Login en cuenta suspendida  
**Precondición:** El administrador ha suspendido previamente la cuenta.  
**Pasos:**  
1. Intentar iniciar sesión con las credenciales de la cuenta suspendida.  
**Resultado Esperado:** Acceso denegado con alerta de contacto a soporte.  
**Resultado Real:** El sistema valida el estado inactivo del perfil y bloquea el acceso con SweetAlert.  
**Estado:** ✅ Exitoso  
**Evidencia:** Comprobación del campo de estado activo en `vista_ingreso`.

**ID:** TC-10  
**Nombre:** Solicitud de recuperación de contraseña  
**Precondición:** El usuario olvidó su contraseña y está en `/cuenta/recuperar/`.  
**Pasos:**  
1. Ingresar el correo electrónico de la cuenta y solicitar enlace de recuperación.  
**Resultado Esperado:** El sistema envía la solicitud y confirma el proceso de forma segura.  
**Resultado Real:** Envío confirmado con respuesta genérica para evitar filtración de usuarios.  
**Estado:** ✅ Exitoso  
**Evidencia:** Controlador `olvide_contraseña` en `users/views.py`.

**ID:** TC-11  
**Nombre:** Restablecimiento exitoso de contraseña  
**Precondición:** El usuario cuenta con la confirmación de restablecimiento.  
**Pasos:**  
1. Introducir la nueva contraseña en `/cuenta/recuperar/verificar/` y guardar.  
**Resultado Esperado:** Contraseña modificada en la base de datos de autenticación y redirección al login.  
**Resultado Real:** Contraseña cambiada en Supabase Auth. El usuario ya puede iniciar sesión con sus nuevas credenciales.  
**Estado:** ✅ Exitoso  
**Evidencia:** Controlador `restablecer_contraseña` en `users/views.py`.

---

## 5. Dashboard y Perfil

**ID:** TC-12  
**Nombre:** Dashboard personal del cliente  
**Precondición:** El cliente ha iniciado sesión correctamente.  
**Pasos:**  
1. Acceder a `/cuenta/perfil/`.  
**Resultado Esperado:** Carga el saludo personalizado, compras activas y enlaces rápidos de navegación.  
**Resultado Real:** Panel renderiza la información del cliente, perfil de usuario y estadísticas de pedidos.  
**Estado:** ✅ Exitoso  
**Evidencia:** Plantilla `profile.html` y vista `mi_perfil`.

---

## 6. Carrito de Compras

**ID:** TC-13  
**Nombre:** Agregar producto al carrito  
**Precondición:** El catálogo tiene stock de productos y el usuario navega en él.  
**Pasos:**  
1. Presionar "Agregar al carrito" en un producto.  
**Resultado Esperado:** Se añade el ítem al carrito y el contador del header aumenta.  
**Resultado Real:** Solicitud AJAX procesada exitosamente. El contador en el header se actualiza.  
**Estado:** ✅ Exitoso  
**Evidencia:** Rutas de carrito en `core/views.py` y script de front-end.

**ID:** TC-14  
**Nombre:** Modificación y eliminación del carrito  
**Precondición:** El carrito contiene al menos un producto.  
**Pasos:**  
1. Cambiar la cantidad del producto y posteriormente presionar el ícono de eliminar.  
**Resultado Esperado:** El total se recalcula con las cantidades nuevas y se remueve el producto del listado al borrarlo.  
**Resultado Real:** Operaciones asíncronas de base de datos actualizan el total y quitan la card de forma instantánea.  
**Estado:** ✅ Exitoso  
**Evidencia:** JS interactivo del carrito de compras.

---

## 7. Checkout y Pedidos

**ID:** TC-15  
**Nombre:** Finalización de checkout exitoso  
**Precondición:** El usuario tiene sesión y productos en el carrito.  
**Pasos:**  
1. Acceder a `/checkout/`, completar campos de envío y confirmar.  
**Resultado Esperado:** Pedido guardado en estado `PENDING`, carrito vacío y pantalla de confirmación.  
**Resultado Real:** Pedido registrado exitosamente en Supabase. Sesión del carrito reseteada.  
**Estado:** ✅ Exitoso  
**Evidencia:** Vista `core/views.py:carrito` (Checkout) y guardado SQL.

**ID:** TC-16  
**Nombre:** Checkout con campos vacíos  
**Precondición:** El usuario está en `/checkout/`.  
**Pasos:**  
1. Dejar campos obligatorios (dirección, teléfono) vacíos y presionar pagar.  
**Resultado Esperado:** Errores de validación se muestran en rojo e impiden el flujo.  
**Resultado Real:** Validación de formulario detiene el envío, marcando los campos requeridos en rojo.  
**Estado:** ✅ Exitoso  
**Evidencia:** Formulario de validación en `checkout.html`.

**ID:** TC-17  
**Nombre:** Historial de pedidos  
**Precondición:** El usuario cuenta con compras previas.  
**Pasos:**  
1. Acceder a `/cuenta/pedidos/`.  
**Resultado Esperado:** Lista histórica de compras con badges coloreados correspondientes.  
**Resultado Real:** Tabla carga la lista completa con códigos de pedido y estados.  
**Estado:** ✅ Exitoso  
**Evidencia:** Plantilla `orders.html` e historial de base de datos.

**ID:** TC-18  
**Nombre:** Desglose y detalle de un pedido  
**Precondición:** El usuario está en el historial de pedidos.  
**Pasos:**  
1. Hacer clic sobre una orden específica.  
**Resultado Esperado:** Muestra productos, cantidades, precios unitarios e información del tracking.  
**Resultado Real:** Modal o sección expandida muestra detalladamente la factura y estatus del pedido.  
**Estado:** ✅ Exitoso  
**Evidencia:** Controlador de pedidos en `users/views.py`.

---

## 8. Perfil de Usuario y Soporte

**ID:** TC-19  
**Nombre:** Edición de datos personales del perfil  
**Precondición:** El cliente está en la configuración de su perfil.  
**Pasos:**  
1. Modificar campos de datos de envío y guardar.  
**Resultado Esperado:** Persistencia de los cambios en la BD y alerta visual de éxito.  
**Resultado Real:** Datos actualizados inmediatamente en Supabase con confirmación visual.  
**Estado:** ✅ Exitoso  
**Evidencia:** Vista `editar_perfil` en `users/views.py`.

**ID:** TC-20  
**Nombre:** Carga de avatar con gestor de imágenes  
**Precondición:** El usuario está en la configuración de su perfil.  
**Pasos:**  
1. Cargar una imagen en formato JPG/PNG y guardar.  
**Resultado Esperado:** La imagen se sube a Supabase Storage (`avatars/`) y se vincula a su perfil. Fallback local ante fallos.  
**Resultado Real:** El gestor `UserPhotoManager` carga la imagen al bucket `mikitech`, guardando la URL definitiva.  
**Estado:** ✅ Exitoso  
**Evidencia:** Código en `users/photo_manager.py`.

**ID:** TC-21  
**Nombre:** Sección de Soporte y FAQ  
**Precondición:** El usuario requiere soporte.  
**Pasos:**  
1. Acceder a `/contacto/`.  
**Resultado Esperado:** Carga el listado de preguntas frecuentes y formulario funcional de soporte.  
**Resultado Real:** Sección cargada limpiamente con formulario de contacto y accesos directos.  
**Estado:** ✅ Exitoso  
**Evidencia:** Ruta `/contacto/` y plantilla `contact.html`.

---

## 9. Seguridad Administrativa

**ID:** TC-22  
**Nombre:** Acceso a panel de administración  
**Precondición:** El usuario es administrador y conoce el código de pasarela.  
**Pasos:**  
1. Ir a `/admin-panel/pasarela/`.  
2. Ingresar el código `SENA-2026` y loguearse.  
**Resultado Esperado:** Validación exitosa de credenciales y redirección al dashboard global.  
**Resultado Real:** Pasarela valida la sesión y otorga acceso al panel.  
**Estado:** ✅ Exitoso  
**Evidencia:** Controlador `admin_views.pasarela` en `core/admin_views.py`.

**ID:** TC-23  
**Nombre:** Bloqueo de acceso al panel de administración  
**Precondición:** El usuario es normal (no admin) o introduce un código inválido.  
**Pasos:**  
1. Intentar acceder a `/admin-panel/` o ingresar código erróneo en la pasarela.  
**Resultado Esperado:** Redirección automática segura, denegando el panel administrativo.  
**Resultado Real:** Bloqueo de la solicitud. Redirige al inicio de sesión o al perfil del cliente.  
**Estado:** ✅ Exitoso  
**Evidencia:** Middleware y decorators de control de acceso en `core/admin_views.py`.

---

## 10. Dashboard de Negocios y Reportes

**ID:** TC-24  
**Nombre:** Métricas del tablero administrativo  
**Precondición:** El administrador está logueado en el panel.  
**Pasos:**  
1. Cargar el index de `/admin-panel/`.  
**Resultado Esperado:** Carga estadísticas de ventas, cantidad de usuarios, pedidos y gráficos informativos.  
**Resultado Real:** Tablero renderiza con sumas y agregaciones calculadas en tiempo real en la BD.  
**Estado:** ✅ Exitoso  
**Evidencia:** Plantilla `admin_panel/dashboard.html`.

---

## 11. Gestión de Catálogo

**ID:** TC-25  
**Nombre:** CRUD de productos del catálogo  
**Precondición:** El administrador está en el módulo de productos.  
**Pasos:**  
1. Crear un producto, cambiar su precio y desactivar su visibilidad.  
**Resultado Esperado:** Modificaciones se guardan inmediatamente y afectan la tienda pública.  
**Resultado Real:** Inserciones y updates en la tabla de productos de Supabase confirmadas al instante.  
**Estado:** ✅ Exitoso  
**Evidencia:** Vistas de catálogo admin en `core/admin_views.py`.

**ID:** TC-26  
**Nombre:** Carga masiva de catálogo vía Excel  
**Precondición:** El administrador está en `/admin-panel/productos/carga-masiva/`.  
**Pasos:**  
1. Cargar archivo Excel `.xlsx` estructurado con la plantilla oficial.  
**Resultado Esperado:** El sistema importa los productos masivamente a Supabase y confirma los registros insertados.  
**Resultado Real:** Archivo procesado correctamente. Los productos se crean en lote y se listan en el catálogo.  
**Estado:** ✅ Exitoso  
**Evidencia:** Lógica de carga masiva en `core/admin_views.py`.

---

## 12. Gestión de Despacho y Logística

**ID:** TC-27  
**Nombre:** Gestión logística y despacho  
**Precondición:** Existen pedidos pendientes.  
**Pasos:**  
1. Seleccionar un pedido en el panel de logística, asignarle un repartidor y cambiar su estado.  
**Resultado Esperado:** El pedido se actualiza en base de datos y se notifica la asignación al repartidor.  
**Resultado Real:** El repartidor recibe el pedido en su panel y el estado logístico cambia correctamente.  
**Estado:** ✅ Exitoso  
**Evidencia:** Panel de logística en `/admin-panel/logistica/`.

**ID:** TC-28  
**Nombre:** Emisión de factura del pedido  
**Precondición:** Se selecciona un pedido en el panel.  
**Pasos:**  
1. Abrir la factura correspondiente del pedido.  
**Resultado Esperado:** Documento HTML formateado con todos los detalles y listo para imprimir.  
**Resultado Real:** Genera la factura conteniendo productos, precios e impuestos estructurados.  
**Estado:** ✅ Exitoso  
**Evidencia:** Ruta `/admin-panel/logistica/factura/<id>/`.

---

## 13. Gestión de Cuentas y Reportes Admin

**ID:** TC-29  
**Nombre:** Gestión de usuarios y credenciales (Admin)  
**Precondición:** El admin está en el panel de usuarios.  
**Pasos:**  
1. Editar un usuario, cambiar su rol, suspender la cuenta y modificar su email.  
**Resultado Esperado:** Actualizaciones se sincronizan con la tabla nativa `auth.users` de Supabase y sube fotos del perfil.  
**Resultado Real:** El email es modificado directamente en la tabla Auth de Supabase vía SQL. La cuenta queda inhabilitada para el inicio de sesión.  
**Estado:** ✅ Exitoso  
**Evidencia:** Vista `editar_usuario` en `core/admin_views.py` y `edit_user.html`.

**ID:** TC-30  
**Nombre:** Reportes de negocio y exportación CSV  
**Precondición:** El administrador está en `/admin-panel/reportes/`.  
**Pasos:**  
1. Filtrar ventas por rango de fechas y hacer clic en Exportar CSV.  
**Resultado Esperado:** Descarga del reporte en formato CSV estructurado con la información financiera.  
**Resultado Real:** Genera y descarga el archivo plano CSV con los registros financieros correctos.  
**Estado:** ✅ Exitoso  
**Evidencia:** Exportador en `/admin-panel/reportes/`.

---

## Plan de Implantación

### Fase Alpha
* **Objetivo:** Verificación interna (QA en entorno local y staging controlado).
* **Actividades:** Ejecución de los 30 casos de prueba de este documento y pruebas de carga (k6).
* **Criterios de éxito:** Todos los casos en estado "Exitoso" y sin errores críticos en base de datos.

### Fase Beta
* **Objetivo:** Prueba de aceptación por usuarios (UAT).
* **Actividades:** Pruebas de estrés y volumen de carga (carga masiva de catálogo por lotes) por personal administrativo.
* **Criterios de éxito:** Procesamiento continuo y feedback de usuario aprobatorio.

### Lanzamiento (Producción)
* **Objetivo:** Salida a Producción (Go-Live).
* **Actividades:** Despliegue, monitoreo en tiempo real de logs en Supabase y soporte proactivo de infraestructura.
* **Criterios de éxito:** Cero bloqueos críticos en las primeras transacciones de compra.
