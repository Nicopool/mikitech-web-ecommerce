# Plan de Pruebas e Implementación — MIKITECH
**Proyecto:** MIKITECH E-Commerce
**Estándar:** Basado en ISO 29119

---

## 1. Registro

**ID:** TC-REG-01
**Nombre:** Registro exitoso de usuario
**Precondición:** El visitante no tiene sesión activa y se encuentra en la página de registro.
**Pasos:**
1. Navegar a la página de registro.
2. Completar nombre, email válido y contraseña.
3. Confirmar la contraseña asegurando que coincida.
4. Hacer clic en "Registrarse".
**Resultado Esperado:** El sistema crea la cuenta exitosamente y redirige al dashboard de usuario.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-REG-02
**Nombre:** Registro con datos incompletos
**Precondición:** El visitante se encuentra en la página de registro.
**Pasos:**
1. Dejar campos obligatorios vacíos o usar formatos inválidos.
2. Intentar enviar el formulario.
**Resultado Esperado:** El sistema muestra validaciones claras y solicita completar la información correctamente.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-REG-03
**Nombre:** Email ya registrado
**Precondición:** El visitante se encuentra en la página de registro.
**Pasos:**
1. Ingresar un email que ya existe en la base de datos.
2. Completar los demás campos y enviar el formulario.
**Resultado Esperado:** El sistema informa la duplicidad del email y ofrece opciones para iniciar sesión o recuperar contraseña.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-REG-04
**Nombre:** Contraseñas no coinciden
**Precondición:** El visitante se encuentra en la página de registro.
**Pasos:**
1. Ingresar una contraseña.
2. Ingresar una confirmación distinta a la contraseña original.
3. Intentar enviar el formulario.
**Resultado Esperado:** El sistema muestra el error "Las contraseñas no coinciden" y bloquea el envío.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 2. Login

**ID:** TC-LOG-01
**Nombre:** Inicio de sesión exitoso
**Precondición:** El usuario tiene una cuenta activa registrada.
**Pasos:**
1. Navegar a la página de login.
2. Ingresar email y contraseña válidos.
3. Hacer clic en "Iniciar Sesión".
**Resultado Esperado:** El sistema autentica al usuario y lo redirige a su dashboard personal correspondiente.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-LOG-02
**Nombre:** Contraseña incorrecta
**Precondición:** El usuario se encuentra en la página de login.
**Pasos:**
1. Ingresar email válido pero contraseña incorrecta.
2. Hacer clic en "Iniciar Sesión".
**Resultado Esperado:** El sistema niega el acceso y muestra el mensaje "Credenciales inválidas. Intenta de nuevo."
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-LOG-03
**Nombre:** Recuperación de contraseña (Solicitud)
**Precondición:** El usuario olvidó su contraseña.
**Pasos:**
1. Navegar a "Olvidé mi contraseña".
2. Ingresar un email válido asociado a una cuenta.
3. Enviar solicitud.
**Resultado Esperado:** El sistema envía un enlace de recuperación al email proporcionado y muestra confirmación.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 3. Dashboard

**ID:** TC-DASH-01
**Nombre:** Dashboard carga correctamente
**Precondición:** El usuario ha iniciado sesión exitosamente.
**Pasos:**
1. Navegar a la ruta `/dashboard/`.
**Resultado Esperado:** El sistema muestra saludo personalizado, resumen de pedidos activos y accesos rápidos.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 4. Tienda

**ID:** TC-TIE-01
**Nombre:** Carga rápida y visualización de Landing
**Precondición:** El usuario entra por primera vez a la web.
**Pasos:**
1. Cargar la ruta principal `/`.
**Resultado Esperado:** El sistema muestra el hero, CTAs y secciones clave en menos de 2 segundos.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-TIE-02
**Nombre:** Catálogo carga correctamente
**Precondición:** El catálogo tiene productos registrados.
**Pasos:**
1. Navegar a `/catalogo/`.
**Resultado Esperado:** El sistema muestra los productos con imagen, nombre y precio en un grid paginado.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-TIE-03
**Nombre:** Ver detalle de producto
**Precondición:** El catálogo está visible.
**Pasos:**
1. Hacer clic en la card de un producto.
**Resultado Esperado:** El sistema muestra imagen, descripción, precio y especificaciones técnicas detalladas del producto.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-TIE-04
**Nombre:** Bloqueo de compra sin login
**Precondición:** El visitante no tiene sesión iniciada.
**Pasos:**
1. Navegar al detalle de un producto.
2. Hacer clic en "Agregar al carrito".
**Resultado Esperado:** El sistema redirige a `/login/` con el mensaje "Inicia sesión para comprar".
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 5. Carrito

**ID:** TC-CAR-01
**Nombre:** Agregar producto exitosamente
**Precondición:** El usuario tiene sesión iniciada y el producto tiene stock.
**Pasos:**
1. Navegar al detalle de un producto.
2. Hacer clic en "Agregar al carrito".
**Resultado Esperado:** El sistema añade el producto y actualiza el contador del carrito en la barra de navegación.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-CAR-02
**Nombre:** Modificar cantidad y eliminar en carrito
**Precondición:** El carrito contiene al menos un producto.
**Pasos:**
1. Navegar al carrito.
2. Cambiar la cantidad de un producto.
3. Hacer clic en el ícono de eliminar.
**Resultado Esperado:** El sistema recalcula el subtotal al cambiar la cantidad, y al eliminar, remueve el ítem actualizando el total general.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 6. Checkout

**ID:** TC-CHK-01
**Nombre:** Checkout exitoso
**Precondición:** El carrito tiene productos y el usuario tiene sesión.
**Pasos:**
1. Ir al proceso de pago (Checkout).
2. Completar todos los datos requeridos de envío y pago.
3. Confirmar pedido.
**Resultado Esperado:** El sistema procesa la orden, la establece en estado PENDING y muestra la pantalla de confirmación con el número de pedido.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-CHK-02
**Nombre:** Datos de envío incompletos
**Precondición:** El usuario está en el Checkout.
**Pasos:**
1. Dejar la dirección de envío en blanco.
2. Intentar confirmar pedido.
**Resultado Esperado:** El sistema muestra errores de validación en rojo y bloquea la confirmación.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 7. Pedidos

**ID:** TC-PED-01
**Nombre:** Historial de pedidos carga correctamente
**Precondición:** El usuario tiene pedidos previos realizados.
**Pasos:**
1. Navegar a la sección `/mis-pedidos/`.
**Resultado Esperado:** El sistema lista los pedidos con número, fecha, total y estado con sus respectivos badges de color.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-PED-02
**Nombre:** Ver detalle de un pedido
**Precondición:** El usuario está en el historial de pedidos.
**Pasos:**
1. Hacer clic en uno de los pedidos de la lista.
**Resultado Esperado:** El sistema muestra los productos, cantidades, subtotales y estado de seguimiento actualizado.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 8. Perfil

**ID:** TC-PER-01
**Nombre:** Actualización de datos de perfil
**Precondición:** El usuario tiene sesión iniciada.
**Pasos:**
1. Navegar a la configuración de perfil.
2. Modificar el nombre u otros datos.
3. Guardar cambios.
**Resultado Esperado:** El sistema actualiza la información y muestra una notificación visual de éxito.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## 9. Admin

**ID:** TC-ADM-01
**Nombre:** Acceso al panel de administración
**Precondición:** El usuario es administrador y conoce el código de pasarela.
**Pasos:**
1. Navegar al gateway de administración.
2. Ingresar código válido y credenciales.
**Resultado Esperado:** El sistema redirige al panel principal con métricas cargadas.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-ADM-02
**Nombre:** Gestión del catálogo (Creación masiva)
**Precondición:** El administrador está en el módulo de productos.
**Pasos:**
1. Navegar a carga masiva.
2. Subir un archivo `.xlsx` válido con nuevos productos.
**Resultado Esperado:** El sistema importa los productos y muestra confirmación indicando la cantidad de registros procesados.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-ADM-03
**Nombre:** Gestión de pedidos globales
**Precondición:** Existen pedidos en diferentes estados.
**Pasos:**
1. Navegar al módulo de pedidos como administrador.
2. Cambiar el estado de un pedido de PENDING a SHIPPED.
**Resultado Esperado:** El sistema actualiza el estado y este cambio es visible inmediatamente para el cliente.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

**ID:** TC-ADM-04
**Nombre:** Suspensión de cuenta de usuario
**Precondición:** El usuario objetivo existe en el sistema.
**Pasos:**
1. Navegar al módulo de usuarios.
2. Seleccionar un usuario y marcar como 'Suspendido'.
**Resultado Esperado:** El acceso del usuario queda bloqueado y no puede iniciar sesión.
**Resultado Real:** 
**Estado:** ⏳ Pendiente
**Evidencia:** 📸 

---

## Plan de Implantación

### Fase Alpha
* **Objetivo:** Verificación interna (QA en entorno local y staging controlado).
* **Actividades:** 
  * Ejecución del 100% de los casos de prueba de este documento.
  * Reporte de bugs críticos (Blockers).
  * Validación de la arquitectura (Django Backend + Vite/React Frontend).
* **Criterios de éxito:** 0 Bugs Blockers, y todos los módulos (Login, Checkout, Admin) funcionando de extremo a extremo.

### Fase Beta
* **Objetivo:** Prueba de aceptación por usuarios de negocio (UAT).
* **Actividades:** 
  * Despliegue en entorno pre-productivo (Staging).
  * Pruebas de estrés menores y cargas masivas de datos (Catálogo).
  * Verificación de la experiencia de usuario final.
* **Criterios de éxito:** Feedback positivo de los usuarios de prueba y flujos de compra sin interrupciones.

### Lanzamiento (Producción)
* **Objetivo:** Salida a Producción (Go-Live).
* **Actividades:** 
  * Despliegue de la versión final.
  * Monitorización en tiempo real de logs y base de datos (Supabase).
  * Soporte técnico reactivo y proactivo (Hiper-cuidado).
* **Criterios de éxito:** Primeras transacciones completadas exitosamente por usuarios reales. Sin caídas del servidor (Uptime 99.9%).

---

## Cierre y Lecciones Aprendidas

1. **Gestión de Casos:** La trazabilidad desde Historias de Usuario hasta Casos de Prueba asegura cobertura completa (ISO 29119).
2. **Automatización:** Se sugiere en futuras versiones automatizar el "TC-CHK-01" (Checkout Exitoso) ya que representa el Core Business.
3. **Manejo de Errores:** Las precondiciones establecidas ahorraron tiempo valioso identificando dependencias antes de testear los flujos.
4. **Validación de Evidencia:** Incluir el espacio de Evidencia (📸) para cada paso crítico garantizará auditorías claras y precisas.

---
*Documento de Pruebas generado por el Ingeniero de QA Senior*
