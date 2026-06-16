# 📋 Historias de Usuario — MIKITECH E-Commerce

Este documento contiene las **31 historias de usuario** que describen el comportamiento del sistema e-commerce de Mikitech, divididas por bloques de roles y numeradas secuencialmente del 01 al 31. Cada historia cuenta con sus escenarios de aceptación detallados en tablas individuales para facilitar su lectura y mantenimiento.

---

## 🔵 BLOQUE 1 — VISITANTE (Sin cuenta)

### 🔹 HU-01: Visualizar la landing page de mikitech
* **Rol:** Como visitante  
* **Característica:** visualizar la landing page de Mikitech  
* **Razón:** Con la finalidad de entender rápidamente qué vende la plataforma y cómo funciona.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Carga rápida y contenido principal visible | En caso de que el visitante ingrese por primera vez a la web | Cuando se carga la página principal | El sistema muestra el hero, CTAs y secciones clave en menos de 2 segundos percibidos. |
| **2** | Acceso claro a Explorar Kits y Explorar Tienda | En caso de que el visitante quiera empezar a navegar el catálogo | Cuando hace clic en "Explorar kits" o "Explorar tienda" | El sistema redirige a la vista correspondiente conservando la navegación. |
| **3** | Sección de categorías tecnológicas disponible | En caso de que el visitante quiera ver qué tipo de productos existen | Cuando se desplaza a la sección de categorías | El sistema muestra cards de categorías como Kits por objetivo, Periféricos, Audio y Video. |

---

### 🔹 HU-02: Ver el catálogo público de productos
* **Rol:** Como visitante  
* **Característica:** ver el catálogo público de productos  
* **Razón:** Con la finalidad de conocer la oferta de la tienda antes de registrarme.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Catálogo carga con productos visibles | En caso de que el visitante navegue al catálogo | Cuando entra a la sección de catálogo | El sistema muestra los productos con imagen, nombre y precio en un grid paginado. |
| **2** | Filtrar por categoría | En caso de que quiera ver solo una categoría | Cuando selecciona un filtro | El sistema actualiza el grid con los productos correspondientes. |
| **3** | Buscar un producto | En caso de que sepa qué producto busca | Cuando escribe en el buscador | El sistema muestra resultados relacionados en tiempo real. |
| **4** | Sin resultados de búsqueda | En caso de que no existan coincidencias | Cuando busca un término sin resultados | El sistema muestra el mensaje "No se encontraron productos para tu búsqueda." |

---

### 🔹 HU-03: Ver el detalle de un producto
* **Rol:** Como visitante  
* **Característica:** ver el detalle de un producto  
* **Razón:** Con la finalidad de conocer sus especificaciones antes de decidir comprarlo.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Detalle del producto carga correctamente | En caso de que el visitante haga clic en una card | Cuando entra al detalle | El sistema muestra imagen, nombre, precio, descripción y especificaciones técnicas. |
| **2** | Bloqueo de compra sin login | En caso de que intente agregar al carrito sin sesión activa | Cuando hace clic en "Agregar al carrito" | El sistema redirige al login con el mensaje "Inicia sesión para comprar." |
| **3** | Producto no existe | En caso de que la URL sea inválida o el producto haya sido eliminado | Cuando intenta acceder | El sistema muestra la página 404. |

---

### 🔹 HU-04: Registrarme como usuario
* **Rol:** Como visitante  
* **Característica:** registrarme como usuario  
* **Razón:** Con la finalidad de comprar productos, ver mis pedidos y acceder al dashboard.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Registro exitoso | En caso de que el visitante complete el formulario correctamente | Cuando envía nombre, email y contraseña válida | El sistema crea la cuenta y redirige al dashboard de usuario. |
| **2** | Campos incompletos | En caso de que falten campos obligatorios | Cuando intenta enviar el formulario sin completarlo | El sistema muestra validaciones en rojo y no permite avanzar. |
| **3** | Email ya registrado | En caso de que el email ya exista en la base de datos | Cuando intenta registrarse con ese email | El sistema informa la duplicidad y ofrece iniciar sesión o recuperar contraseña. |
| **4** | Contraseñas no coinciden | En caso de que los campos de contraseña sean diferentes | Cuando el visitante intenta registrarse | El sistema muestra "Las contraseñas no coinciden" y bloquea el envío. |

---

### 🔹 HU-05: Usar el buscador global
* **Rol:** Como visitante  
* **Característica:** usar el buscador global  
* **Razón:** Con la finalidad de encontrar productos específicos sin navegar por todo el catálogo.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Búsqueda con resultados | En caso de que existan productos relacionados al término | Cuando escribe en el buscador y presiona buscar | El sistema muestra los resultados en la vista de búsqueda con imagen y precio. |
| **2** | Búsqueda sin resultados | En caso de que no haya coincidencias | Cuando busca un término inexistente | El sistema muestra "No se encontraron productos" y sugiere explorar el catálogo. |

---

### 🔹 HU-06: Ver el perfil público de un usuario
* **Rol:** Como visitante  
* **Característica:** ver el perfil público de un usuario  
* **Razón:** Con la finalidad de conocer su actividad y reseñas en la plataforma.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Perfil público carga correctamente | En caso de que el visitante acceda al perfil de un usuario activo | Cuando navega a la URL del perfil público | El sistema muestra nombre, avatar y reseñas públicas del usuario. |
| **2** | Usuario no existe | En caso de que el nombre de usuario no exista | Cuando accede a esa URL | El sistema muestra página 404. |

---

## 🟢 BLOQUE 2 — USUARIO AUTENTICADO

### 🔹 HU-07: Iniciar sesión en mikitech
* **Rol:** Como usuario  
* **Característica:** iniciar sesión en Mikitech  
* **Razón:** Con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades del sistema.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Inicio de sesión exitoso | En caso de que el usuario ingrese credenciales correctas | Cuando envía email y contraseña válidos | El sistema autentica, asigna rol y redirige al dashboard correspondiente. |
| **2** | Contraseña incorrecta | En caso de que la contraseña no coincida | Cuando envía contraseña errónea | El sistema niega el acceso y muestra "Credenciales inválidas. Intenta de nuevo." |
| **3** | Email no registrado | En caso de que el email no exista en la BD | Cuando envía un email inexistente | El sistema muestra "No encontramos una cuenta con ese email." |
| **4** | Cuenta suspendida | En caso de que la cuenta esté desactivada por administración | Cuando el usuario intenta iniciar sesión | El sistema bloquea el ingreso y muestra el canal de soporte. |
| **5** | Formulario vacío | En caso de que no llene ningún campo | Cuando intenta enviar sin datos | El sistema aplica validación requerida y no permite avanzar. |

---

### 🔹 HU-08: Recuperar mi contraseña
* **Rol:** Como usuario  
* **Característica:** recuperar mi contraseña  
* **Razón:** Con la finalidad de recuperar el acceso a mi cuenta si olvidé mis credenciales.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Solicitud de recuperación exitosa | En caso de que el email pertenezca a una cuenta existente | Cuando solicita "Olvidé mi contraseña" | El sistema envía un enlace de recuperación y confirma la acción en pantalla. |
| **2** | Email no registrado | En caso de que el email no exista | Cuando envía el email inexistente | El sistema responde con un mensaje genérico: "Si el email existe, recibirás un correo." |
| **3** | Restablecimiento exitoso | En caso de que el usuario acceda al enlace del correo | Cuando ingresa y confirma la nueva contraseña | El sistema la actualiza y redirige al login con mensaje de éxito. |

---

### 🔹 HU-09: Ver mi dashboard personal
* **Rol:** Como usuario  
* **Característica:** ver mi dashboard personal  
* **Razón:** Con la finalidad de tener un resumen de mi actividad y accesos rápidos al sistema.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Dashboard carga correctamente | En caso de que el usuario esté autenticado | Cuando entra al dashboard | El sistema muestra saludo personalizado, resumen de pedidos activos y accesos rápidos. |
| **2** | Notificaciones disponibles | En caso de que haya notificaciones nuevas | Cuando entra al dashboard | El sistema muestra el indicador de notificaciones con el contador activo. |
| **3** | Marcar notificaciones como leídas | En caso de que quiera limpiar las notificaciones | Cuando hace clic en "Marcar como leídas" | El sistema limpia el indicador y actualiza el estado. |

---

### 🔹 HU-10: Agregar productos al carrito
* **Rol:** Como usuario  
* **Característica:** agregar productos al carrito  
* **Razón:** Con la finalidad de seleccionar lo que quiero comprar antes de pagar.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Producto agregado exitosamente | En caso de que el producto esté disponible | Cuando hace clic en "Agregar al carrito" | El sistema añade el producto y actualiza el contador en la navbar. |
| **2** | Modificar cantidad en el carrito | En caso de que quiera más o menos unidades | Cuando cambia la cantidad | El sistema recalcula el subtotal automáticamente. |
| **3** | Eliminar producto del carrito | En caso de que no quiera un item | Cuando hace clic en eliminar | El sistema remueve el producto y actualiza el total. |
| **4** | Carrito vacío | En caso de que no haya agregado nada | Cuando entra al carrito | El sistema muestra "Tu carrito está vacío. Explora el catálogo." |

---

### 🔹 HU-11: Realizar el proceso de checkout
* **Rol:** Como usuario  
* **Característica:** realizar el proceso de checkout  
* **Razón:** Con la finalidad de concretar mi pedido y recibirlo en mi dirección.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Checkout exitoso | En caso de que los datos de envío estén completos | Cuando confirma el pedido con todos los datos | El sistema crea la orden con estado PENDING y muestra el número de pedido. |
| **2** | Datos de envío incompletos | En caso de que falte dirección, cédula o teléfono | Cuando intenta confirmar sin completar el formulario | El sistema muestra validaciones en rojo y no permite avanzar. |
| **3** | Confirmación del pedido | En caso de que el pedido se procese correctamente | Cuando la orden es creada | El sistema muestra pantalla de confirmación con resumen y número de orden. |

---

### 🔹 HU-12: Ver mis pedidos activos
* **Rol:** Como usuario  
* **Característica:** ver mis pedidos activos  
* **Razón:** Con la finalidad de hacer seguimiento de mis compras en curso.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Lista de pedidos activos | En caso de que el usuario tenga pedidos en curso | Cuando entra a la sección de pedidos | El sistema muestra los pedidos con estado, fecha y total con badge de color. |
| **2** | Ver detalle de un pedido | En caso de que quiera ver qué compró | Cuando hace clic en un pedido | El sistema muestra los productos, cantidades, subtotales y estado de tracking. |
| **3** | Sin pedidos activos | En caso de que no tenga compras en curso | Cuando entra a la sección | El sistema muestra "No tienes pedidos activos. ¡Empieza a comprar!" |

---

### 🔹 HU-13: Ver mi historial de compras
* **Rol:** Como usuario  
* **Característica:** ver mi historial de compras  
* **Razón:** Con la finalidad de consultar todas mis transacciones anteriores.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Historial completo carga | En caso de que el usuario tenga compras pasadas | Cuando entra al historial | El sistema lista todos los pedidos con número, fecha, total y estado final. |
| **2** | Sin historial | En caso de que sea un usuario nuevo sin compras | Cuando entra al historial | El sistema muestra "Aún no tienes compras registradas." |

---

### 🔹 HU-14: Ver mis reportes personales de compra
* **Rol:** Como usuario  
* **Característica:** ver mis reportes personales de compra  
* **Razón:** Con la finalidad de analizar mis gastos y productos más comprados.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Reportes personales cargan | En caso de que el usuario tenga compras registradas | Cuando entra a la sección de reportes | El sistema muestra gráficos de gasto por período y productos más comprados. |
| **2** | Sin datos suficientes | En caso de que el usuario no tenga compras | Cuando entra a reportes | El sistema muestra "Aún no hay datos para mostrar. Realiza tu primera compra." |

---

### 🔹 HU-15: Editar mi perfil
* **Rol:** Como usuario  
* **Característica:** editar mi perfil  
* **Razón:** Con la finalidad de mantener mis datos personales actualizados.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Actualización de datos exitosa | En caso de que el usuario quiera cambiar nombre o avatar | Cuando guarda los cambios | El sistema actualiza el perfil y muestra confirmación visual. |
| **2** | Cambio de contraseña exitoso | En caso de que quiera nueva contraseña | Cuando ingresa la actual y la nueva | El sistema la actualiza y la sesión continúa activa. |
| **3** | Datos inválidos | En caso de que el formato sea incorrecto | Cuando intenta guardar datos mal formateados | El sistema muestra validaciones en rojo. |

---

### 🔹 HU-16: Agregar reseñas a productos
* **Rol:** Como usuario  
* **Característica:** agregar reseñas a productos  
* **Razón:** Con la finalidad de compartir mi experiencia con otros compradores.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Reseña enviada exitosamente | En caso de que el usuario haya comprado el producto | Cuando escribe y envía una reseña con calificación | El sistema la registra y la muestra en el detalle del producto. |
| **2** | Responder a una reseña | En caso de que quiera comentar en una reseña existente | Cuando escribe una respuesta | El sistema la registra y la muestra anidada bajo la reseña original. |
| **3** | Calificación incompleta | En caso de que no seleccione estrellas | Cuando intenta enviar sin calificación | El sistema muestra "Selecciona una calificación para continuar." |

---

### 🔹 HU-17: Votar por productos
* **Rol:** Como usuario  
* **Característica:** votar por productos  
* **Razón:** Con la finalidad de indicar que me gustan y ayudar a otros usuarios a descubrir los mejores.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Voto registrado | En caso de que el usuario esté autenticado | Cuando hace clic en el botón de voto | El sistema registra el voto y actualiza el contador de votos del producto. |
| **2** | Voto ya registrado (toggle) | En caso de que ya haya votado por ese producto | Cuando hace clic nuevamente | El sistema elimina el voto y actualiza el contador. |

---

### 🔹 HU-18: Guardar productos en favoritos
* **Rol:** Como usuario  
* **Característica:** guardar productos en favoritos  
* **Razón:** Con la finalidad de tener una lista de productos que me interesan para comprarlos después.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Producto agregado a favoritos | En caso de que el usuario quiera guardar un producto | Cuando hace clic en el icono de favorito | El sistema lo agrega a su lista y confirma con ícono activo. |
| **2** | Producto eliminado de favoritos | En caso de que ya esté en favoritos | Cuando hace clic nuevamente | El sistema lo elimina de la lista (toggle). |
| **3** | Ver lista de favoritos | En caso de que quiera ver sus guardados | Cuando entra a la sección de favoritos | El sistema muestra todos los productos guardados con acceso directo al detalle. |
| **4** | Lista de favoritos vacía | En caso de que no haya guardado nada | Cuando entra a favoritos | El sistema muestra "Aún no tienes productos guardados." |

---

### 🔹 HU-19: Acceder a soporte y faq
* **Rol:** Como usuario  
* **Característica:** acceder a soporte y FAQ  
* **Razón:** Con la finalidad de resolver dudas o reportar problemas con mis pedidos o cuenta.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Consulta de FAQ con búsqueda | En caso de que tenga una pregunta frecuente | Cuando busca un tema en la sección de soporte | El sistema muestra respuestas relevantes y enlaces relacionados. |
| **2** | Contactar soporte directo | En caso de que no encuentre respuesta en FAQ | Cuando hace clic en "Contactar soporte" | El sistema muestra formulario de contacto o enlace a WhatsApp. |

---

### 🔹 HU-20: Ver el blog de mikitech
* **Rol:** Como usuario  
* **Característica:** ver el blog de Mikitech  
* **Razón:** Con la finalidad de acceder a contenido sobre tecnología y novedades de la plataforma.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Blog carga correctamente | En caso de que el usuario entre a la sección de blog | Cuando navega a la URL del blog | El sistema muestra las publicaciones disponibles. |

---

## 🟡 BLOQUE 3 — REPARTIDOR

### 🔹 HU-21: Registrarme y acceder al sistema
* **Rol:** Como repartidor  
* **Característica:** registrarme y acceder al sistema  
* **Razón:** Con la finalidad de gestionar mis entregas asignadas.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Registro de repartidor exitoso | En caso de que complete el formulario de registro del portal repartidor | Cuando envía los datos válidos | El sistema crea la cuenta de repartidor y redirige al panel. |
| **2** | Login de repartidor exitoso | En caso de que tenga credenciales correctas | Cuando accede al portal de repartidor | El sistema autentica y redirige al panel de entregas. |
| **3** | Acceso sin código de gateway | En caso de que intente acceder directamente sin pasar por la pasarela | Cuando navega al panel | El sistema redirige a la pasarela de repartidor. |

---

### 🔹 HU-22: Ver mis pedidos asignados
* **Rol:** Como repartidor  
* **Característica:** ver mis pedidos asignados  
* **Razón:** Con la finalidad de saber qué entregas debo realizar.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Panel de entregas carga | En caso de que el repartidor esté autenticado | Cuando entra al panel | El sistema muestra los pedidos asignados con dirección, cliente y estado. |
| **2** | Sin pedidos asignados | En caso de que no tenga entregas asignadas | Cuando entra al panel | El sistema muestra "No tienes pedidos asignados en este momento." |

---

### 🔹 HU-23: Marcar un pedido como entregado
* **Rol:** Como repartidor  
* **Característica:** marcar un pedido como entregado  
* **Razón:** Con la finalidad de actualizar el estado de la entrega en el sistema.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Entrega confirmada exitosamente | En caso de que haya completado la entrega | Cuando marca el pedido como entregado | El sistema cambia el estado a DELIVERED y registra la fecha y hora de entrega. |
| **2** | Nota de entrega fallida | En caso de que no haya podido entregar | Cuando agrega una nota al pedido | El sistema registra la incidencia y notifica al administrador. |

---

## 🔴 BLOQUE 4 — ADMINISTRADOR

### 🔹 HU-24: Acceder al gateway de administración
* **Rol:** Como administrador  
* **Característica:** acceder al gateway de administración  
* **Razón:** Con la finalidad de ingresar al panel de control de forma segura.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Acceso con código correcto | En caso de que el admin ingrese el código válido | Cuando escribe el código de acceso | El sistema lo valida y redirige al panel de administración. |
| **2** | Código de acceso incorrecto | En caso de que el código sea equivocado | Cuando envía un código inválido | El sistema muestra "Código de acceso inválido. Intenta de nuevo." |
| **3** | Usuario sin rol de administrador | En caso de que un usuario normal intente acceder | Cuando navega a la URL del gateway | El sistema lo redirige al dashboard de usuario. |
| **4** | Acceso sin sesión activa | En caso de que nadie esté autenticado | Cuando se accede al gateway sin login | El sistema redirige al login. |

---

### 🔹 HU-25: Ver el panel principal (dashboard)
* **Rol:** Como administrador  
* **Característica:** ver el panel principal (dashboard)  
* **Razón:** Con la finalidad de tener visión global del negocio en tiempo real.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Panel carga con métricas | En caso de que el admin esté autenticado | Cuando entra al panel principal | El sistema muestra ventas del día, pedidos activos, total de usuarios y productos destacados. |
| **2** | Navegación entre módulos | En caso de que quiera gestionar un área | Cuando hace clic en un módulo del menú | El sistema redirige al módulo seleccionado. |

---

### 🔹 HU-26: Gestionar el catálogo de productos
* **Rol:** Como administrador  
* **Característica:** gestionar el catálogo de productos  
* **Razón:** Con la finalidad de mantener actualizado el inventario y la oferta de la tienda.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Crear producto exitosamente | En caso de que quiera añadir un nuevo producto | Cuando llena el formulario completo y guarda | El sistema crea el producto y lo hace visible en el catálogo público. |
| **2** | Editar producto existente | En caso de que el precio o descripción hayan cambiado | Cuando modifica y guarda | El sistema actualiza los cambios inmediatamente en el catálogo. |
| **3** | Eliminar producto | En caso de que el producto deba ser eliminado | Cuando confirma la eliminación | El sistema borra el producto y lo remueve del catálogo. |
| **4** | Desactivar/Activar producto | En caso de que esté agotado temporalmente | Cuando desactiva el toggle de visibilidad | El sistema oculta el producto del catálogo público pero lo mantiene en el panel admin. |
| **5** | Marcar producto como destacado | En caso de que quiera promocionarlo en la landing | Cuando activa "Destacado" | El sistema lo muestra en la sección Destacados del Home. |
| **6** | Carga masiva con Excel | En caso de que tenga muchos productos nuevos | Cuando sube un archivo .xlsx válido | El sistema importa los productos y confirma cuántos se crearon exitosamente. |
| **7** | Excel con formato inválido | En caso de que el archivo tenga errores de estructura | Cuando sube un Excel inválido | El sistema muestra qué fila tiene el error y no importa ningún dato. |

---

### 🔹 HU-27: Gestionar categorías de productos
* **Rol:** Como administrador  
* **Característica:** gestionar categorías de productos  
* **Razón:** Con la finalidad de mantener organizado el catálogo.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Crear categoría | En caso de que necesite una nueva categoría | Cuando la crea con nombre e icono | El sistema la registra y la hace disponible en el catálogo y filtros. |
| **2** | Editar categoría | En caso de que cambie el nombre o icono | Cuando guarda los cambios | El sistema actualiza la categoría en todo el catálogo. |
| **3** | Eliminar categoría | En caso de que una categoría ya no sea necesaria | Cuando la elimina | El sistema la borra y reasigna o notifica sobre los productos afectados. |

---

### 🔹 HU-28: Gestionar la logística y despachos
* **Rol:** Como administrador  
* **Característica:** gestionar la logística y despachos  
* **Razón:** Con la finalidad de supervisar las entregas y asignar repartidores.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Ver pedidos en logística | En caso de que el admin necesite gestionar entregas | Cuando consulta el módulo de logística | El sistema muestra pedidos pendientes de asignación con filtros por estado. |
| **2** | Asignar repartidor a pedido | En caso de que un pedido esté listo para despacho | Cuando asigna un repartidor | El sistema actualiza el pedido y notifica al repartidor. |
| **3** | Cambiar estado de pedido | En caso de que el pedido avance en el proceso | Cuando actualiza el estado | El sistema lo refleja en el historial del cliente y en el panel del repartidor. |
| **4** | Ver factura de pedido | En caso de que necesite revisar o imprimir una factura | Cuando accede a la factura de un pedido | El sistema muestra el documento con todos los detalles del pedido. |

---

### 🔹 HU-29: Moderar reseñas de productos
* **Rol:** Como administrador  
* **Característica:** moderar reseñas de productos  
* **Razón:** Con la finalidad de garantizar la calidad del contenido en la plataforma.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Ver todas las reseñas | En caso de que el admin necesite moderar el contenido | Cuando entra al módulo de reseñas | El sistema muestra todas las reseñas con usuario, producto, calificación y estado. |
| **2** | Eliminar reseña inapropiada | En caso de que una reseña viole las normas | Cuando el admin la elimina | El sistema la borra y confirma la acción. |
| **3** | Notificar al usuario sobre su reseña | En caso de que quiera informar al usuario | Cuando envía una notificación desde el módulo de reseñas | El sistema registra y envía la notificación al usuario correspondiente. |

---

### 🔹 HU-30: Gestionar cuentas de usuarios
* **Rol:** Como administrador  
* **Característica:** gestionar cuentas de usuarios  
* **Razón:** Con la finalidad de controlar el acceso y la seguridad de la plataforma.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Ver lista de usuarios | En caso de que necesite revisar cuentas registradas | Cuando entra al módulo de usuarios | El sistema muestra tabla con nombre, email, rol y estado de cada cuenta. |
| **2** | Suspender cuenta de usuario | En caso de que un usuario infrinja normas | Cuando el admin desactiva la cuenta | El sistema bloquea el acceso y el usuario no puede iniciar sesión. |
| **3** | Reactivar cuenta suspendida | En caso de que se levante la suspensión | Cuando activa la cuenta nuevamente | El sistema restaura el acceso y el usuario puede iniciar sesión. |

---

### 🔹 HU-31: Ver los reportes globales del negocio
* **Rol:** Como administrador  
* **Característica:** ver los reportes globales del negocio  
* **Razón:** Con la finalidad de tomar decisiones basadas en datos y rendimiento.

| N° | Criterio de aceptación (Título) | Contexto | Evento | Resultado / Comportamiento esperado |
|:---:|---|---|---|---|
| **1** | Ventas por período y ticket promedio | En caso de que seleccione un rango de fechas | Cuando consulta el reporte de ventas | El sistema muestra gráfico con ventas por día o mes y ticket promedio. |
| **2** | Pedidos por estado y top proveedores | En caso de que quiera identificar cuellos de botella | Cuando consulta reportes operativos | El sistema muestra distribución por estados y ranking de ingresos. |
| **3** | Exportación CSV/Excel | En caso de que necesite auditoría o análisis externo | Cuando exporta los reportes | El sistema genera un archivo descargable con datos detallados. |

---
