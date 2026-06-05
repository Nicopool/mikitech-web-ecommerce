# 📋 Historias de Usuario — MIKITECH E-Commerce
> **Columnas:** Identificador (ID) · Rol · Característica / Funcionalidad · Razón / Resultado · N° Escenario · Criterio de aceptación · Contexto · Evento · Resultado / Comportamiento esperado

---

## 🔵 BLOQUE 1 — VISITANTE (Sin Login)

| Identificador (ID) de la historia | Rol | Característica / Funcionalidad | Razón / Resultado | Número (#) de escenario | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|---|---|---|---|---|---|---|---|---|
| HU-01 | Como visitante | Visualizar la landing page de Mikitech | Con la finalidad de entender qué vende la plataforma y cómo funciona | 1 | Carga rápida y contenido principal visible | En caso de que el visitante ingrese por primera vez a la web | Cuando se carga la página principal `/` | El sistema muestra el hero, CTAs y secciones clave en menos de 2 segundos |
| HU-01 | Como visitante | Visualizar la landing page de Mikitech | Con la finalidad de entender qué vende la plataforma y cómo funciona | 2 | Acceso claro a Explorar Kits y Explorar Tienda | En caso de que el visitante quiera empezar a navegar el catálogo | Cuando hace clic en "Explorar kits" o "Explorar tienda" | El sistema redirige a la vista correspondiente conservando el estilo y la navegación |
| HU-01 | Como visitante | Visualizar la landing page de Mikitech | Con la finalidad de entender qué vende la plataforma y cómo funciona | 3 | Sección de categorías tecnológicas disponible | En caso de que el visitante quiera ver qué tipo de productos existen | Cuando se desplaza a la sección de categorías | El sistema muestra cards de categorías (Kits por objetivo, Periféricos, Audio, Video) |
| HU-02 | Como visitante | Registrarse como usuario | Con la finalidad de comprar productos/kits, ver mis pedidos y acceder al dashboard | 1 | Registro exitoso de usuario | En caso de que el visitante complete correctamente el formulario | Cuando envía nombre, email y contraseña válida | El sistema crea la cuenta y redirige al dashboard de usuario |
| HU-02 | Como visitante | Registrarse como usuario | Con la finalidad de comprar productos/kits, ver mis pedidos y acceder al dashboard | 2 | Registro con datos incompletos | En caso de que falten campos obligatorios o el formato sea inválido | Cuando el visitante intenta registrarse con datos incompletos | El sistema muestra validaciones claras y solicita completar la información |
| HU-02 | Como visitante | Registrarse como usuario | Con la finalidad de comprar productos/kits, ver mis pedidos y acceder al dashboard | 3 | Email ya registrado | En caso de que el email ya exista en la base de datos | Cuando el visitante intenta registrarse con un email existente | El sistema informa la duplicidad y ofrece iniciar sesión o recuperar contraseña |
| HU-02 | Como visitante | Registrarse como usuario | Con la finalidad de comprar productos/kits, ver mis pedidos y acceder al dashboard | 4 | Contraseñas no coinciden | En caso de que los campos de contraseña sean diferentes | Cuando el visitante escribe confirmación distinta a la contraseña | El sistema muestra "Las contraseñas no coinciden" y bloquea el envío |
| HU-03 | Como visitante | Ver catálogo público de productos | Con la finalidad de conocer los productos disponibles antes de registrarse | 1 | Catálogo carga correctamente | En caso de que el visitante navegue al catálogo | Cuando entra a `/catalogo/` | El sistema muestra productos con imagen, nombre y precio en grid paginado |
| HU-03 | Como visitante | Ver catálogo público de productos | Con la finalidad de conocer los productos disponibles antes de registrarse | 2 | Filtrar por categoría | En caso de que quiera ver solo una categoría | Cuando selecciona una categoría del filtro | El sistema actualiza el grid mostrando solo los productos de esa categoría |
| HU-03 | Como visitante | Ver catálogo público de productos | Con la finalidad de conocer los productos disponibles antes de registrarse | 3 | Ver detalle de producto | En caso de que quiera saber más de un producto | Cuando hace clic en la card del producto | El sistema muestra imagen, descripción, precio y especificaciones técnicas |
| HU-03 | Como visitante | Ver catálogo público de productos | Con la finalidad de conocer los productos disponibles antes de registrarse | 4 | Bloqueo de compra sin login | En caso de que intente agregar al carrito sin sesión | Cuando hace clic en "Agregar al carrito" | El sistema redirige a `/login/` con mensaje "Inicia sesión para comprar" |

---

## 🟢 BLOQUE 2 — USUARIO AUTENTICADO (Con Login)

| Identificador (ID) de la historia | Rol | Característica / Funcionalidad | Razón / Resultado | Número (#) de escenario | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|---|---|---|---|---|---|---|---|---|
| HU-04 | Como usuario | Iniciar sesión en Mikitech | Con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades | 1 | Inicio de sesión exitoso | En caso de que el usuario ingrese credenciales correctas | Cuando envía email y contraseña válidos | El sistema autentica, asigna rol y redirige al dashboard correspondiente |
| HU-04 | Como usuario | Iniciar sesión en Mikitech | Con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades | 2 | Contraseña incorrecta | En caso de que la contraseña no coincida | Cuando envía contraseña errónea | El sistema niega el acceso y muestra "Credenciales inválidas. Intenta de nuevo." |
| HU-04 | Como usuario | Iniciar sesión en Mikitech | Con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades | 3 | Email no registrado | En caso de que el email no exista en la BD | Cuando envía un email inexistente | El sistema muestra "No encontramos una cuenta con ese email." |
| HU-04 | Como usuario | Iniciar sesión en Mikitech | Con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades | 4 | Cuenta suspendida | En caso de que la cuenta esté desactivada | Cuando el usuario intenta iniciar sesión | El sistema bloquea el ingreso y muestra estado de cuenta y canal de soporte |
| HU-04 | Como usuario | Iniciar sesión en Mikitech | Con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades | 5 | Formulario vacío | En caso de que no llene ningún campo | Cuando intenta enviar sin datos | El sistema aplica validación requerida y no permite avanzar |
| HU-05 | Como usuario | Recuperar contraseña olvidada | Con la finalidad de recuperar el acceso a mi cuenta si olvidé mis credenciales | 1 | Solicitud de recuperación exitosa | En caso de que el email pertenezca a una cuenta existente | Cuando solicita "Olvidé mi contraseña" con email válido | El sistema envía un enlace de recuperación y confirma la acción en pantalla |
| HU-05 | Como usuario | Recuperar contraseña olvidada | Con la finalidad de recuperar el acceso a mi cuenta si olvidé mis credenciales | 2 | Email no registrado | En caso de que el email no exista en la BD | Cuando envía email inexistente | El sistema responde "Si el email existe, recibirás un correo" (respuesta genérica por seguridad) |
| HU-05 | Como usuario | Recuperar contraseña olvidada | Con la finalidad de recuperar el acceso a mi cuenta si olvidé mis credenciales | 3 | Restablecimiento exitoso | En caso de que el usuario acceda al enlace del email | Cuando ingresa y confirma la nueva contraseña | El sistema actualiza la contraseña y redirige al login con mensaje de éxito |
| HU-06 | Como usuario | Ver mi dashboard personal | Con la finalidad de tener un resumen de mi actividad y accesos rápidos | 1 | Dashboard carga correctamente | En caso de que el usuario esté autenticado | Cuando entra a `/dashboard/` | El sistema muestra saludo, resumen de pedidos activos y accesos rápidos |
| HU-06 | Como usuario | Ver mi dashboard personal | Con la finalidad de tener un resumen de mi actividad y accesos rápidos | 2 | Acceso rápido al catálogo | En caso de que quiera seguir comprando | Cuando hace clic en "Ir al catálogo" | El sistema redirige al catálogo con el carrito activo |
| HU-07 | Como usuario | Agregar productos al carrito | Con la finalidad de seleccionar lo que quiero comprar antes de pagar | 1 | Producto agregado exitosamente | En caso de que el producto esté disponible | Cuando hace clic en "Agregar al carrito" | El sistema añade el producto y actualiza el contador del carrito en la navbar |
| HU-07 | Como usuario | Agregar productos al carrito | Con la finalidad de seleccionar lo que quiero comprar antes de pagar | 2 | Modificar cantidad en carrito | En caso de que quiera más o menos unidades | Cuando cambia la cantidad de un producto | El sistema recalcula el subtotal automáticamente |
| HU-07 | Como usuario | Agregar productos al carrito | Con la finalidad de seleccionar lo que quiero comprar antes de pagar | 3 | Eliminar producto del carrito | En caso de que no quiera un item | Cuando hace clic en el icono de eliminar | El sistema remueve el producto y actualiza el total |
| HU-07 | Como usuario | Agregar productos al carrito | Con la finalidad de seleccionar lo que quiero comprar antes de pagar | 4 | Carrito vacío | En caso de que no haya agregado nada | Cuando entra a `/carrito/` sin items | El sistema muestra "Tu carrito está vacío. Explora el catálogo." |
| HU-08 | Como usuario | Realizar el proceso de compra | Con la finalidad de concretar un pedido y recibir mis productos | 1 | Checkout exitoso | En caso de que los datos de envío estén completos | Cuando confirma el pedido con todos los datos | El sistema crea la orden con estado PENDING y muestra número de pedido |
| HU-08 | Como usuario | Realizar el proceso de compra | Con la finalidad de concretar un pedido y recibir mis productos | 2 | Datos de envío incompletos | En caso de que falte la dirección u otro dato | Cuando intenta confirmar sin completar el formulario | El sistema muestra validaciones en rojo y no permite avanzar |
| HU-08 | Como usuario | Realizar el proceso de compra | Con la finalidad de concretar un pedido y recibir mis productos | 3 | Confirmación de pedido | En caso de que el pedido se procese correctamente | Cuando el pedido es creado exitosamente | El sistema muestra pantalla de confirmación con resumen y número de orden |
| HU-09 | Como usuario | Ver mi historial de pedidos | Con la finalidad de hacer seguimiento de mis compras anteriores y actuales | 1 | Historial carga correctamente | En caso de que el usuario tenga pedidos | Cuando entra a `/mis-pedidos/` | El sistema lista pedidos con número, fecha, total y estado con badge de color |
| HU-09 | Como usuario | Ver mi historial de pedidos | Con la finalidad de hacer seguimiento de mis compras anteriores y actuales | 2 | Ver detalle de pedido | En caso de que quiera ver qué compró | Cuando hace clic en un pedido | El sistema muestra productos, cantidades, subtotales y estado de tracking |
| HU-09 | Como usuario | Ver mi historial de pedidos | Con la finalidad de hacer seguimiento de mis compras anteriores y actuales | 3 | Sin pedidos previos | En caso de que el usuario sea nuevo | Cuando entra al historial sin compras | El sistema muestra "Aún no tienes pedidos. ¡Empieza a comprar!" |
| HU-10 | Como usuario | Editar mi perfil y contraseña | Con la finalidad de mantener mis datos actualizados y mi cuenta segura | 1 | Actualización de datos exitosa | En caso de que cambie nombre o avatar | Cuando guarda los cambios del perfil | El sistema actualiza el perfil y muestra confirmación visual |
| HU-10 | Como usuario | Editar mi perfil y contraseña | Con la finalidad de mantener mis datos actualizados y mi cuenta segura | 2 | Cambio de contraseña exitoso | En caso de que quiera una nueva contraseña | Cuando ingresa la actual y la nueva | El sistema actualiza la contraseña y la sesión continúa activa |
| HU-10 | Como usuario | Editar mi perfil y contraseña | Con la finalidad de mantener mis datos actualizados y mi cuenta segura | 3 | Datos inválidos en perfil | En caso de que el formato sea incorrecto | Cuando intenta guardar datos mal formateados | El sistema muestra validaciones de formulario en rojo |
| HU-11 | Como usuario | Acceder a soporte y FAQ | Con la finalidad de resolver dudas o reportar problemas con pedidos o cuenta | 1 | Consulta de FAQ con búsqueda | En caso de que tenga una pregunta frecuente | Cuando ingresa a soporte y busca un tema | El sistema muestra respuestas relevantes y enlaces a secciones relacionadas |
| HU-11 | Como usuario | Acceder a soporte y FAQ | Con la finalidad de resolver dudas o reportar problemas con pedidos o cuenta | 2 | Contactar soporte directo | En caso de que no encuentre respuesta en FAQ | Cuando hace clic en "Contactar soporte" | El sistema muestra formulario de contacto o enlace a WhatsApp |

---

## 🔴 BLOQUE 3 — ADMINISTRADOR

| Identificador (ID) de la historia | Rol | Característica / Funcionalidad | Razón / Resultado | Número (#) de escenario | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|---|---|---|---|---|---|---|---|---|
| HU-12 | Como administrador | Acceder al gateway de administración | Con la finalidad de ingresar al panel de control de forma segura | 1 | Acceso con código correcto | En caso de que el admin ingrese el código válido | Cuando escribe el código de acceso correcto | El sistema valida el código y redirige al panel de administración |
| HU-12 | Como administrador | Acceder al gateway de administración | Con la finalidad de ingresar al panel de control de forma segura | 2 | Código de acceso incorrecto | En caso de que el código sea equivocado | Cuando envía un código inválido | El sistema muestra "Código de acceso inválido. Intenta de nuevo." |
| HU-12 | Como administrador | Acceder al gateway de administración | Con la finalidad de ingresar al panel de control de forma segura | 3 | Usuario sin rol de administrador | En caso de que un usuario normal intente acceder | Cuando un usuario sin rol admin entra a la URL | El sistema redirige al dashboard de usuario sin mostrar el panel |
| HU-12 | Como administrador | Acceder al gateway de administración | Con la finalidad de ingresar al panel de control de forma segura | 4 | Acceso sin sesión activa | En caso de que nadie esté autenticado | Cuando se accede a la URL del gateway sin login | El sistema redirige a `/login/` |
| HU-13 | Como administrador | Ver el panel principal de administración | Con la finalidad de tener una visión global del negocio en tiempo real | 1 | Panel carga con métricas | En caso de que el admin esté autenticado | Cuando entra al panel principal | El sistema muestra ventas del día, pedidos activos y total de usuarios |
| HU-13 | Como administrador | Ver el panel principal de administración | Con la finalidad de tener una visión global del negocio en tiempo real | 2 | Navegación entre módulos | En caso de que quiera gestionar un área específica | Cuando hace clic en un módulo del menú | El sistema redirige al módulo seleccionado (Productos, Pedidos, Usuarios, Reportes) |
| HU-14 | Como administrador | Gestionar el catálogo de productos | Con la finalidad de mantener actualizado el inventario y la oferta de la tienda | 1 | Crear producto exitosamente | En caso de que quiera añadir un nuevo producto | Cuando llena el formulario completo y guarda | El sistema crea el producto y lo hace visible en el catálogo público |
| HU-14 | Como administrador | Gestionar el catálogo de productos | Con la finalidad de mantener actualizado el inventario y la oferta de la tienda | 2 | Editar producto existente | En caso de que cambie precio o descripción | Cuando modifica datos y guarda | El sistema actualiza los cambios y se reflejan inmediatamente en el catálogo |
| HU-14 | Como administrador | Gestionar el catálogo de productos | Con la finalidad de mantener actualizado el inventario y la oferta de la tienda | 3 | Desactivar producto | En caso de que el producto esté agotado | Cuando desactiva el toggle de visibilidad | El sistema oculta el producto del catálogo público pero lo mantiene en el panel |
| HU-14 | Como administrador | Gestionar el catálogo de productos | Con la finalidad de mantener actualizado el inventario y la oferta de la tienda | 4 | Marcar producto como destacado | En caso de que quiera promocionarlo en la landing | Cuando activa la opción "Destacado" | El sistema lo muestra en la sección Destacados del Home |
| HU-14 | Como administrador | Gestionar el catálogo de productos | Con la finalidad de mantener actualizado el inventario y la oferta de la tienda | 5 | Carga masiva con Excel | En caso de que tenga muchos productos nuevos | Cuando sube un archivo `.xlsx` válido | El sistema importa los productos y confirma cuántos se crearon exitosamente |
| HU-14 | Como administrador | Gestionar el catálogo de productos | Con la finalidad de mantener actualizado el inventario y la oferta de la tienda | 6 | Excel con formato inválido | En caso de que el archivo tenga errores | Cuando sube un Excel con filas mal formateadas | El sistema muestra qué fila tiene el error y no importa nada |
| HU-15 | Como administrador | Gestionar pedidos globales | Con la finalidad de supervisar incidencias y devoluciones de toda la plataforma | 1 | Listado global con filtros | En caso de que el admin necesite monitorear operación | Cuando consulta el módulo de pedidos | El sistema muestra pedidos con filtros por estado, fecha, usuario y proveedor |
| HU-15 | Como administrador | Gestionar pedidos globales | Con la finalidad de supervisar incidencias y devoluciones de toda la plataforma | 2 | Cambiar estado de pedido | En caso de que el pedido avance en el proceso | Cuando actualiza el estado a SHIPPED o DELIVERED | El sistema actualiza el estado y el cliente puede verlo en su historial |
| HU-15 | Como administrador | Gestionar pedidos globales | Con la finalidad de supervisar incidencias y devoluciones de toda la plataforma | 3 | Gestión de devolución | En caso de que exista una solicitud RETURN_REQUESTED | Cuando el admin procesa la devolución | El sistema registra la decisión, actualiza estados y notifica al cliente |
| HU-16 | Como administrador | Gestionar cuentas de usuarios | Con la finalidad de controlar el acceso y la seguridad de la plataforma | 1 | Ver lista de usuarios | En caso de que necesite revisar cuentas | Cuando entra al módulo de usuarios | El sistema muestra tabla con nombre, email, rol y estado de cada cuenta |
| HU-16 | Como administrador | Gestionar cuentas de usuarios | Con la finalidad de controlar el acceso y la seguridad de la plataforma | 2 | Suspender cuenta de usuario | En caso de que un usuario infrinja normas | Cuando desactiva la cuenta | El sistema bloquea el acceso y el usuario no puede iniciar sesión |
| HU-16 | Como administrador | Gestionar cuentas de usuarios | Con la finalidad de controlar el acceso y la seguridad de la plataforma | 3 | Reactivar cuenta suspendida | En caso de que se levante la suspensión | Cuando activa nuevamente la cuenta | El sistema restaura el acceso y el usuario puede iniciar sesión |
| HU-17 | Como administrador | Ver reportes globales del negocio | Con la finalidad de tomar decisiones basadas en datos y rendimiento | 1 | Ventas por período y ticket promedio | En caso de que seleccione un rango de fechas | Cuando consulta el reporte de ventas | El sistema muestra gráfico con ventas por día/mes y calcula ticket promedio |
| HU-17 | Como administrador | Ver reportes globales del negocio | Con la finalidad de tomar decisiones basadas en datos y rendimiento | 2 | Pedidos por estado y top proveedores | En caso de que quiera identificar cuellos de botella | Cuando consulta reportes operativos | El sistema muestra distribución por estados y ranking de proveedores por ingresos |
| HU-17 | Como administrador | Ver reportes globales del negocio | Con la finalidad de tomar decisiones basadas en datos y rendimiento | 3 | Exportación CSV/Excel | En caso de que necesite auditoría o análisis externo | Cuando exporta los reportes | El sistema genera archivo con datos detallados y consistentes |

---

## 🗺️ Mapa de Flujo General

```
/ (Landing)
 │
 ├── VISITANTE
 │    ├── /catalogo/  → Ver productos → Detalle
 │    │                          └── [Comprar sin login] → /login/
 │    ├── /registro/  → Crear cuenta → /dashboard/
 │    └── /login/
 │           ├── Éxito usuario   → /dashboard/
 │           ├── Éxito admin     → /admin-gateway/ → /admin/
 │           ├── Error           → Mensaje + reintentar
 │           └── /forgot-password/ → Email → Restablecer
 │
 ├── USUARIO AUTENTICADO
 │    ├── /dashboard/       → Resumen y accesos
 │    ├── /catalogo/        → Agregar al carrito
 │    ├── /carrito/         → Revisar y modificar items
 │    ├── /checkout/        → Confirmar → Orden creada (PENDING)
 │    ├── /mis-pedidos/     → Ver historial y estados
 │    ├── /perfil/          → Editar datos y contraseña
 │    └── /soporte/         → FAQ y contacto
 │
 └── ADMINISTRADOR
      ├── /admin-gateway/   → Código secreto → Panel
      ├── /admin/productos/ → CRUD + Excel masivo
      ├── /admin/pedidos/   → Estados + devoluciones
      ├── /admin/usuarios/  → Activar / Suspender
      └── /admin/reportes/  → Gráficos + Exportar CSV
```

---
*MIKITECH E-Commerce · Historias de Usuario v2.0 · Mayo 2026*
