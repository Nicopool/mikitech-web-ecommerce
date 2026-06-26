# Historias de Usuario — MIKITECH E-Commerce (Completo)
Aplicación: MIKITECH — Plataforma de comercio electrónico de componentes tecnológicos y kits.
Roles del sistema: Visitante · Usuario autenticado · Repartidor · Administrador
Total de historias: 29 | Total de escenarios: 76

---

## BLOQUE 1 — VISITANTE (Sin cuenta)

---

HU-01: Como visitante, necesito visualizar la landing page de Mikitech, con la finalidad de entender rápidamente qué vende la plataforma y cómo funciona.

Escenario 1 — Carga rápida y contenido principal visible:
En caso de que el visitante ingrese por primera vez a la web, cuando se carga la página principal, el sistema muestra el hero, CTAs y secciones clave en menos de 2 segundos percibidos.

Escenario 2 — Acceso claro a Explorar Kits y Explorar Tienda:
En caso de que el visitante quiera empezar a navegar el catálogo, cuando hace clic en "Explorar kits" o "Explorar tienda", el sistema redirige a la vista correspondiente conservando la navegación.

Escenario 3 — Sección de categorías tecnológicas disponible:
En caso de que el visitante quiera ver qué tipo de productos existen, cuando se desplaza a la sección de categorías, el sistema muestra cards de categorías como Kits por objetivo, Periféricos, Audio y Video.

---

HU-02: Como visitante, necesito ver el catálogo público de productos, con la finalidad de conocer la oferta de la tienda antes de registrarme.

Escenario 1 — Catálogo carga con productos visibles:
En caso de que el visitante navegue al catálogo, cuando entra a la sección de catálogo, el sistema muestra los productos con imagen, nombre y precio en un grid paginado.

Escenario 2 — Filtrar por categoría:
En caso de que quiera ver solo una categoría, cuando selecciona un filtro, el sistema actualiza el grid con los productos correspondientes.

Escenario 3 — Buscar un producto:
En caso de que sepa qué producto busca, cuando escribe en el buscador, el sistema muestra resultados relacionados en tiempo real.

Escenario 4 — Sin resultados de búsqueda:
En caso de que no existan coincidencias, cuando busca un término sin resultados, el sistema muestra el mensaje "No se encontraron productos para tu búsqueda."

---

HU-03: Como visitante, necesito ver el detalle de un producto, con la finalidad de conocer sus especificaciones antes de decidir comprarlo.

Escenario 1 — Detalle del producto carga correctamente:
En caso de que el visitante haga clic en una card, cuando entra al detalle, el sistema muestra imagen, nombre, precio, descripción y especificaciones técnicas.

Escenario 2 — Bloqueo de compra sin login:
En caso de que intente agregar al carrito sin sesión activa, cuando hace clic en "Agregar al carrito", el sistema redirige al login con el mensaje "Inicia sesión para comprar."

Escenario 3 — Producto no existe:
En caso de que la URL sea inválida o el producto haya sido eliminado, cuando intenta acceder, el sistema muestra la página 404.

---

HU-04: Como visitante, necesito registrarme como usuario, con la finalidad de comprar productos, ver mis pedidos y acceder al dashboard.

Escenario 1 — Registro exitoso:
En caso de que el visitante complete el formulario correctamente, cuando envía nombre, email y contraseña válida, el sistema crea la cuenta y redirige al dashboard de usuario.

Escenario 2 — Campos incompletos:
En caso de que falten campos obligatorios, cuando intenta enviar el formulario sin completarlo, el sistema muestra validaciones en rojo y no permite avanzar.

Escenario 3 — Email ya registrado:
En caso de que el email ya exista en la base de datos, cuando intenta registrarse con ese email, el sistema informa la duplicidad y ofrece iniciar sesión o recuperar contraseña.

Escenario 4 — Contraseñas no coinciden:
En caso de que los campos de contraseña sean diferentes, cuando el visitante intenta registrarse, el sistema muestra "Las contraseñas no coinciden" y bloquea el envío.

---

HU-05: Como visitante, necesito usar el buscador global, con la finalidad de encontrar productos específicos sin navegar por todo el catálogo.

Escenario 1 — Búsqueda con resultados:
En caso de que existan productos relacionados al término, cuando escribe en el buscador y presiona buscar, el sistema muestra los resultados en la vista de búsqueda con imagen y precio.

Escenario 2 — Búsqueda sin resultados:
En caso de que no haya coincidencias, cuando busca un término inexistente, el sistema muestra "No se encontraron productos" y sugiere explorar el catálogo.

---

HU-06: Como visitante, necesito ver el perfil público de un usuario, con la finalidad de conocer su actividad y reseñas en la plataforma.

Escenario 1 — Perfil público carga correctamente:
En caso de que el visitante acceda al perfil de un usuario activo, cuando navega a la URL del perfil público, el sistema muestra nombre, avatar y reseñas públicas del usuario.

Escenario 2 — Usuario no existe:
En caso de que el nombre de usuario no exista, cuando accede a esa URL, el sistema muestra página 404.

---

## BLOQUE 2 — USUARIO AUTENTICADO

---

HU-07: Como usuario, necesito iniciar sesión en Mikitech, con la finalidad de acceder a mi cuenta, carrito, pedidos y funcionalidades del sistema.

Escenario 1 — Inicio de sesión exitoso:
En caso de que el usuario ingrese credenciales correctas, cuando envía email y contraseña válidos, el sistema autentica, asigna rol y redirige al dashboard correspondiente.

Escenario 2 — Contraseña incorrecta:
En caso de que la contraseña no coincida, cuando envía contraseña errónea, el sistema niega el acceso y muestra "Credenciales inválidas. Intenta de nuevo."

Escenario 3 — Email no registrado:
En caso de que el email no exista en la BD, cuando envía un email inexistente, el sistema muestra "No encontramos una cuenta con ese email."

Escenario 4 — Cuenta suspendida:
En caso de que la cuenta esté desactivada por administración, cuando el usuario intenta iniciar sesión, el sistema bloquea el ingreso y muestra el canal de soporte.

Escenario 5 — Formulario vacío:
En caso de que no llene ningún campo, cuando intenta enviar sin datos, el sistema aplica validación requerida y no permite avanzar.

---

HU-08: Como usuario, necesito recuperar mi contraseña, con la finalidad de recuperar el acceso a mi cuenta si olvidé mis credenciales.

Escenario 1 — Solicitud de recuperación exitosa:
En caso de que el email pertenezca a una cuenta existente, cuando solicita "Olvidé mi contraseña", el sistema envía un enlace de recuperación y confirma la acción en pantalla.

Escenario 2 — Email no registrado:
En caso de que el email no exista, cuando envía el email inexistente, el sistema responde con un mensaje genérico: "Si el email existe, recibirás un correo."

Escenario 3 — Restablecimiento exitoso:
En caso de que el usuario acceda al enlace del correo, cuando ingresa y confirma la nueva contraseña, el sistema la actualiza y redirige al login con mensaje de éxito.

---

HU-09: Como usuario, necesito ver mi dashboard personal, con la finalidad de tener un resumen de mi actividad y accesos rápidos al sistema.

Escenario 1 — Dashboard carga correctamente:
En caso de que el usuario esté autenticado, cuando entra al dashboard, el sistema muestra saludo personalizado, resumen de pedidos activos y accesos rápidos.

Escenario 2 — Notificaciones disponibles:
En caso de que haya notificaciones nuevas, cuando entra al dashboard, el sistema muestra el indicador de notificaciones con el contador activo.

Escenario 3 — Marcar notificaciones como leídas:
En caso de que quiera limpiar las notificaciones, cuando hace clic en "Marcar como leídas", el sistema limpia el indicador y actualiza el estado.

---

HU-10: Como usuario, necesito agregar productos al carrito, con la finalidad de seleccionar lo que quiero comprar antes de pagar.

Escenario 1 — Producto agregado exitosamente:
En caso de que el producto esté disponible, cuando hace clic en "Agregar al carrito", el sistema añade el producto y actualiza el contador en la navbar.

Escenario 2 — Modificar cantidad en el carrito:
En caso de que quiera más o menos unidades, cuando cambia la cantidad, el sistema recalcula el subtotal automáticamente.

Escenario 3 — Eliminar producto del carrito:
En caso de que no quiera un item, cuando hace clic en eliminar, el sistema remueve el producto y actualiza el total.

Escenario 4 — Carrito vacío:
En caso de que no haya agregado nada, cuando entra al carrito, el sistema muestra "Tu carrito está vacío. Explora el catálogo."

---

HU-11: Como usuario, necesito realizar el proceso de checkout, con la finalidad de concretar mi pedido y recibirlo en mi dirección.

Escenario 1 — Checkout exitoso:
En caso de que los datos de envío estén completos, cuando confirma el pedido con todos los datos, el sistema crea la orden con estado PENDING y muestra el número de pedido.

Escenario 2 — Datos de envío incompletos:
En caso de que falte dirección, cédula o teléfono, cuando intenta confirmar sin completar el formulario, el sistema muestra validaciones en rojo y no permite avanzar.

Escenario 3 — Confirmación del pedido:
En caso de que el pedido se procese correctamente, cuando la orden es creada, el sistema muestra pantalla de confirmación con resumen y número de orden.

---

HU-12: Como usuario, necesito ver mis pedidos activos, con la finalidad de hacer seguimiento de mis compras en curso.

Escenario 1 — Lista de pedidos activos:
En caso de que el usuario tenga pedidos en curso, cuando entra a la sección de pedidos, el sistema muestra los pedidos con estado, fecha y total con badge de color.

Escenario 2 — Ver detalle de un pedido:
En caso de que quiera ver qué compró, cuando hace clic en un pedido, el sistema muestra los productos, cantidades, subtotales y estado de tracking.

Escenario 3 — Sin pedidos activos:
En caso de que no tenga compras en curso, cuando entra a la sección, el sistema muestra "No tienes pedidos activos. ¡Empieza a comprar!"

---

HU-13: Como usuario, necesito ver mi historial de compras, con la finalidad de consultar todas mis transacciones anteriores.

Escenario 1 — Historial completo carga:
En caso de que el usuario tenga compras pasadas, cuando entra al historial, el sistema lista todos los pedidos con número, fecha, total y estado final.

Escenario 2 — Sin historial:
En caso de que sea un usuario nuevo sin compras, cuando entra al historial, el sistema muestra "Aún no tienes compras registradas."

---

HU-14: Como usuario, necesito ver mis reportes personales de compra, con la finalidad de analizar mis gastos y productos más comprados.

Escenario 1 — Reportes personales cargan:
En caso de que el usuario tenga compras registradas, cuando entra a la sección de reportes, el sistema muestra gráficos de gasto por período y productos más comprados.

Escenario 2 — Sin datos suficientes:
En caso de que el usuario no tenga compras, cuando entra a reportes, el sistema muestra "Aún no hay datos para mostrar. Realiza tu primera compra."

---

HU-15: Como usuario, necesito editar mi perfil, con la finalidad de mantener mis datos personales actualizados.

Escenario 1 — Actualización de datos exitosa:
En caso de que el usuario quiera cambiar nombre o avatar, cuando guarda los cambios, el sistema actualiza el perfil y muestra confirmación visual.

Escenario 2 — Cambio de contraseña exitoso:
En caso de que quiera nueva contraseña, cuando ingresa la actual y la nueva, el sistema la actualiza y la sesión continúa activa.

Escenario 3 — Datos inválidos:
En caso de que el formato sea incorrecto, cuando intenta guardar datos mal formateados, el sistema muestra validaciones en rojo.

---

HU-16: Como usuario, necesito agregar reseñas a productos, con la finalidad de compartir mi experiencia con otros compradores.

Escenario 1 — Reseña enviada exitosamente:
En caso de que el usuario haya comprado el producto, cuando escribe y envía una reseña con calificación, el sistema la registra y la muestra en el detalle del producto.

Escenario 2 — Responder a una reseña:
En caso de que quiera comentar en una reseña existente, cuando escribe una respuesta, el sistema la registra y la muestra anidada bajo la reseña original.

Escenario 3 — Calificación incompleta:
En caso de que no seleccione estrellas, cuando intenta enviar sin calificación, el sistema muestra "Selecciona una calificación para continuar."

---

HU-17: Como usuario, necesito votar por productos, con la finalidad de indicar que me gustan y ayudar a otros usuarios a descubrir los mejores.

Escenario 1 — Voto registrado:
En caso de que el usuario esté autenticado, cuando hace clic en el botón de voto, el sistema registra el voto y actualiza el contador de votos del producto.

Escenario 2 — Voto ya registrado (toggle):
En caso de que ya haya votado por ese producto, cuando hace clic nuevamente, el sistema elimina el voto y actualiza el contador.

---

HU-18: Como usuario, necesito guardar productos en favoritos, con la finalidad de tener una lista de productos que me interesan para comprarlos después.

Escenario 1 — Producto agregado a favoritos:
En caso de que el usuario quiera guardar un producto, cuando hace clic en el icono de favorito, el sistema lo agrega a su lista y confirma con ícono activo.

Escenario 2 — Producto eliminado de favoritos:
En caso de que ya esté en favoritos, cuando hace clic nuevamente, el sistema lo elimina de la lista (toggle).

Escenario 3 — Ver lista de favoritos:
En caso de que quiera ver sus guardados, cuando entra a la sección de favoritos, el sistema muestra todos los productos guardados con acceso directo al detalle.

Escenario 4 — Lista de favoritos vacía:
En caso de que no haya guardado nada, cuando entra a favoritos, el sistema muestra "Aún no tienes productos guardados."

---

HU-19: Como usuario, necesito acceder a soporte y FAQ, con la finalidad de resolver dudas o reportar problemas con mis pedidos o cuenta.

Escenario 1 — Consulta de FAQ con búsqueda:
En caso de que tenga una pregunta frecuente, cuando busca un tema en la sección de soporte, el sistema muestra respuestas relevantes y enlaces relacionados.

Escenario 2 — Contactar soporte directo:
En caso de que no encuentre respuesta en FAQ, cuando hace clic en "Contactar soporte", el sistema muestra formulario de contacto o enlace a WhatsApp.

---

HU-20: Como usuario, necesito ver el blog de Mikitech, con la finalidad de acceder a contenido sobre tecnología y novedades de la plataforma.

Escenario 1 — Blog carga correctamente:
En caso de que el usuario entre a la sección de blog, cuando navega a la URL del blog, el sistema muestra las publicaciones disponibles.

---

## BLOQUE 3 — REPARTIDOR

---

HU-21: Como repartidor, necesito registrarme y acceder al sistema, con la finalidad de gestionar mis entregas asignadas.

Escenario 1 — Registro de repartidor exitoso:
En caso de que complete el formulario de registro del portal repartidor, cuando envía los datos válidos, el sistema crea la cuenta de repartidor y redirige al panel.

Escenario 2 — Login de repartidor exitoso:
En caso de que tenga credenciales correctas, cuando accede al portal de repartidor, el sistema autentica y redirige al panel de entregas.

Escenario 3 — Acceso sin código de gateway:
En caso de que intente acceder directamente sin pasar por la pasarela, cuando navega al panel, el sistema redirige a la pasarela de repartidor.

---

HU-22: Como repartidor, necesito ver mis pedidos asignados, con la finalidad de saber qué entregas debo realizar.

Escenario 1 — Panel de entregas carga:
En caso de que el repartidor esté autenticado, cuando entra al panel, el sistema muestra los pedidos asignados con dirección, cliente y estado.

Escenario 2 — Sin pedidos asignados:
En caso de que no tenga entregas asignadas, cuando entra al panel, el sistema muestra "No tienes pedidos asignados en este momento."

---

HU-23: Como repartidor, necesito marcar un pedido como entregado, con la finalidad de actualizar el estado de la entrega en el sistema.

Escenario 1 — Entrega confirmada exitosamente:
En caso de que haya completado la entrega, cuando marca el pedido como entregado, el sistema cambia el estado a DELIVERED y registra la fecha y hora de entrega.

Escenario 2 — Nota de entrega fallida:
En caso de que no haya podido entregar, cuando agrega una nota al pedido, el sistema registra la incidencia y notifica al administrador.

---

## BLOQUE 4 — ADMINISTRADOR

---

HU-24: Como administrador, necesito acceder al gateway de administración, con la finalidad de ingresar al panel de control de forma segura.

Escenario 1 — Acceso con código correcto:
En caso de que el admin ingrese el código válido, cuando escribe el código de acceso, el sistema lo valida y redirige al panel de administración.

Escenario 2 — Código de acceso incorrecto:
En caso de que el código sea equivocado, cuando envía un código inválido, el sistema muestra "Código de acceso inválido. Intenta de nuevo."

Escenario 3 — Usuario sin rol de administrador:
En caso de que un usuario normal intente acceder, cuando navega a la URL del gateway, el sistema lo redirige al dashboard de usuario.

Escenario 4 — Acceso sin sesión activa:
En caso de que nadie esté autenticado, cuando se accede al gateway sin login, el sistema redirige al login.

---

HU-25: Como administrador, necesito ver el panel principal (dashboard), con la finalidad de tener visión global del negocio en tiempo real.

Escenario 1 — Panel carga con métricas:
En caso de que el admin esté autenticado, cuando entra al panel principal, el sistema muestra ventas del día, pedidos activos, total de usuarios y productos destacados.

Escenario 2 — Navegación entre módulos:
En caso de que quiera gestionar un área, cuando hace clic en un módulo del menú, el sistema redirige al módulo seleccionado.

---

HU-26: Como administrador, necesito gestionar el catálogo de productos, con la finalidad de mantener actualizado el inventario y la oferta de la tienda.

Escenario 1 — Crear producto exitosamente:
En caso de que quiera añadir un nuevo producto, cuando llena el formulario completo y guarda, el sistema crea el producto y lo hace visible en el catálogo público.

Escenario 2 — Editar producto existente:
En caso de que el precio o descripción hayan cambiado, cuando modifica y guarda, el sistema actualiza los cambios inmediatamente en el catálogo.

Escenario 3 — Eliminar producto:
En caso de que el producto deba ser eliminado, cuando confirma la eliminación, el sistema borra el producto y lo remueve del catálogo.

Escenario 4 — Desactivar/Activar producto:
En caso de que esté agotado temporalmente, cuando desactiva el toggle de visibilidad, el sistema oculta el producto del catálogo público pero lo mantiene en el panel admin.

Escenario 5 — Marcar producto como destacado:
En caso de que quiera promocionarlo en la landing, cuando activa "Destacado", el sistema lo muestra en la sección Destacados del Home.

Escenario 6 — Carga masiva con Excel:
En caso de que tenga muchos productos nuevos, cuando sube un archivo .xlsx válido, el sistema importa los productos y confirma cuántos se crearon exitosamente.

Escenario 7 — Excel con formato inválido:
En caso de que el archivo tenga errores de estructura, cuando sube un Excel inválido, el sistema muestra qué fila tiene el error y no importa ningún dato.

---

HU-27: Como administrador, necesito gestionar categorías de productos, con la finalidad de mantener organizado el catálogo.

Escenario 1 — Crear categoría:
En caso de que necesite una nueva categoría, cuando la crea con nombre e icono, el sistema la registra y la hace disponible en el catálogo y filtros.

Escenario 2 — Editar categoría:
En caso de que cambie el nombre o icono, cuando guarda los cambios, el sistema actualiza la categoría en todo el catálogo.

Escenario 3 — Eliminar categoría:
En caso de que una categoría ya no sea necesaria, cuando la elimina, el sistema la borra y reasigna o notifica sobre los productos afectados.

---

HU-28: Como administrador, necesito gestionar la logística y despachos, con la finalidad de supervisar las entregas y asignar repartidores.

Escenario 1 — Ver pedidos en logística:
En caso de que el admin necesite gestionar entregas, cuando consulta el módulo de logística, el sistema muestra pedidos pendientes de asignación con filtros por estado.

Escenario 2 — Asignar repartidor a pedido:
En caso de que un pedido esté listo para despacho, cuando asigna un repartidor, el sistema actualiza el pedido y notifica al repartidor.

Escenario 3 — Cambiar estado de pedido:
En caso de que el pedido avance en el proceso, cuando actualiza el estado, el sistema lo refleja en el historial del cliente y en el panel del repartidor.

Escenario 4 — Ver factura de pedido:
En caso de que necesite revisar o imprimir una factura, cuando accede a la factura de un pedido, el sistema muestra el documento con todos los detalles del pedido.

---

HU-29: Como administrador, necesito moderar reseñas de productos, con la finalidad de garantizar la calidad del contenido en la plataforma.

Escenario 1 — Ver todas las reseñas:
En caso de que el admin necesite moderar el contenido, cuando entra al módulo de reseñas, el sistema muestra todas las reseñas con usuario, producto, calificación y estado.

Escenario 2 — Eliminar reseña inapropiada:
En caso de que una reseña viole las normas, cuando el admin la elimina, el sistema la borra y confirma la acción.

Escenario 3 — Notificar al usuario sobre su reseña:
En caso de que quiera informar al usuario, cuando envía una notificación desde el módulo de reseñas, el sistema registra y envía la notificación al usuario correspondiente.

---

HU-30: Como administrador, necesito gestionar cuentas de usuarios, con la finalidad de controlar el acceso y la seguridad de la plataforma.

Escenario 1 — Ver lista de usuarios:
En caso de que necesite revisar cuentas registradas, cuando entra al módulo de usuarios, el sistema muestra tabla con nombre, email, rol y estado de cada cuenta.

Escenario 2 — Suspender cuenta de usuario:
En caso de que un usuario infrinja normas, cuando el admin desactiva la cuenta, el sistema bloquea el acceso y el usuario no puede iniciar sesión.

Escenario 3 — Reactivar cuenta suspendida:
En caso de que se levante la suspensión, cuando activa la cuenta nuevamente, el sistema restaura el acceso y el usuario puede iniciar sesión.

---

HU-31: Como administrador, necesito ver los reportes globales del negocio, con la finalidad de tomar decisiones basadas en datos y rendimiento.

Escenario 1 — Ventas por período y ticket promedio:
En caso de que seleccione un rango de fechas, cuando consulta el reporte de ventas, el sistema muestra gráfico con ventas por día o mes y ticket promedio.

Escenario 2 — Pedidos por estado y top proveedores:
En caso de que quiera identificar cuellos de botella, cuando consulta reportes operativos, el sistema muestra distribución por estados y ranking de ingresos.

Escenario 3 — Exportación CSV/Excel:
En caso de que necesite auditoría o análisis externo, cuando exporta los reportes, el sistema genera un archivo descargable con datos detallados.

---

Resumen final:
- Total de historias de usuario: 31
- Total de escenarios documentados: 83
- Roles cubiertos:
  · Visitante       → HU-01 a HU-06 (6 historias, 17 escenarios)
  · Usuario         → HU-07 a HU-20 (14 historias, 38 escenarios)
  · Repartidor      → HU-21 a HU-23 (3 historias, 7 escenarios)
  · Administrador   → HU-24 a HU-31 (8 historias, 21 escenarios)
- Plataforma: MIKITECH E-Commerce | Django 5 + Supabase + Python 3.11
- Apps del sistema: core · products · users · interactions
- URLs principales mapeadas: /, /buscar/, /carrito/, /checkout/,
  /usuario/ingreso/, /usuario/perfil/, /usuario/favoritos/,
  /usuario/pedidos/, /usuario/historial/, /usuario/reportes/,
  /usuario/recuperar/, /repartidor/, /admin/pasarela/, /admin/,
  /admin/productos/, /admin/categorias/, /admin/logistica/,
  /admin/resenas/, /admin/usuarios/, /admin/reportes/
