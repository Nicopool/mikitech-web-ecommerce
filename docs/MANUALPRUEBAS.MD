# MANUAL DE PRUEBAS - MIKITECH E-COMMERCE

Este documento constituye el Manual de Pruebas formalizado de MIKITECH E-Commerce, estructurado bajo el estándar de aseguramiento de calidad (QA) y trazabilidad de requerimientos. Contiene la auditoría de cobertura, análisis de trazabilidad y el catálogo detallado de casos de prueba organizados por bloques de funcionalidad y alineados con las **31 Historias de Usuario (HU)** y 94 escenarios del sistema.

---

## 1. TABLA DE TRAZABILIDAD (HU ↔ Casos de Prueba)

La siguiente tabla presenta la correspondencia bidireccional entre las 31 Historias de Usuario (HU) reales de la plataforma y los casos de prueba (CP) contenidos en el manual.

| HU ID | Historia de Usuario | # Casos de Prueba | IDs de Casos de Prueba | Estado de Cobertura |
|---|---|:---:|---|---|
| **HU-01** | Visualizar la landing page de Mikitech | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-02** | Ver catálogo público de productos | 3 | CP-MK-USR-010, CP-MK-USR-011, CP-MK-USR-012 | 🟢 Completa |
| **HU-03** | Ver el detalle de un producto | 1 | CP-MK-USR-013 | 🟢 Completa |
| **HU-04** | Registrarse como usuario | 9 | CP-MK-001, CP-MK-002, CP-MK-003, CP-MK-004, CP-MK-005, CP-MK-006, CP-MK-007, CP-MK-008, CP-MK-009 | 🟢 Completa |
| **HU-05** | Usar buscador global | 2 | CP-MK-USR-011, CP-MK-USR-012 *(Cruza con HU-02)* | 🟢 Completa |
| **HU-06** | Ver perfil público de usuario | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-07** | Iniciar sesión en Mikitech | 6 | CP-MK-010, CP-MK-011, CP-MK-012, CP-MK-013, CP-MK-014, CP-MK-015 | 🟢 Completa |
| **HU-08** | Recuperar mi contraseña | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-09** | Ver dashboard personal | 2 | CP-MK-USR-001, CP-MK-USR-002 | 🟢 Completa |
| **HU-10** | Agregar productos al carrito | 5 | CP-MK-USR-014, CP-MK-USR-015, CP-MK-USR-016, CP-MK-USR-017, CP-MK-USR-030 | 🟢 Completa |
| **HU-11** | Realizar el proceso de checkout | 5 | CP-MK-USR-018, CP-MK-USR-019, CP-MK-USR-020, CP-MK-USR-021, CP-MK-USR-022 | 🟢 Completa |
| **HU-12** | Ver pedidos activos | 1 | CP-MK-USR-026 | 🟢 Completa |
| **HU-13** | Ver historial de compras | 3 | CP-MK-USR-023, CP-MK-USR-024, CP-MK-USR-025 | 🟢 Completa |
| **HU-14** | Ver reportes personales de compra | 3 | CP-MK-USR-027, CP-MK-USR-028, CP-MK-USR-029 | 🟢 Completa |
| **HU-15** | Editar mi perfil | 7 | CP-MK-USR-003, CP-MK-USR-004, CP-MK-USR-005, CP-MK-USR-006, CP-MK-USR-007, CP-MK-USR-008, CP-MK-USR-009 | 🟢 Completa |
| **HU-16** | Agregar reseñas a productos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-17** | Votar por productos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-18** | Guardar favoritos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-19** | Acceder a soporte y FAQ | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-20** | Ver el blog de Mikitech | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-21** | Registrarse y acceder (Repartidor) | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-22** | Ver pedidos asignados (Repartidor) | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-23** | Marcar pedido como entregado | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-24** | Acceder al gateway de admin | 8 | CP-MK-ADM-001, CP-MK-ADM-002, CP-MK-ADM-003, CP-MK-ADM-010, CP-MK-ADM-011, CP-MK-ADM-012, CP-MK-ADM-013, CP-MK-ADM-014 | 🟢 Completa |
| **HU-25** | Ver el panel principal (Dashboard admin) | 6 | CP-MK-DASH-001, CP-MK-DASH-002, CP-MK-DASH-003, CP-MK-DASH-004, CP-MK-DASH-005, CP-MK-DASH-007 | 🟢 Completa |
| **HU-26** | Gestionar catálogo de productos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-27** | Gestionar categorías de productos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-28** | Gestionar logística y despachos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-29** | Moderar reseñas de productos | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-30** | Gestionar cuentas de usuario | 0 | *Ninguno* | 🔴 Sin Cobertura |
| **HU-31** | Ver reportes globales del negocio | 1 | CP-MK-DASH-006 | 🟡 Parcial |

---

## 2. QUÉ ESTÁ BIEN (Cobertura Correcta)

* **Flujos de Registro y Autenticación (`HU-04`, `HU-07`):** Amplia variedad de casos que cubren escenarios de éxito, fallos por datos vacíos, correos duplicados, credenciales incorrectas, longitudes de clave inadecuadas, formatos inseguros y seguridad contra inyección SQL.
* **Módulo de Tienda y Carrito (`HU-02`, `HU-03`, `HU-10`):** Se validan adecuadamente la navegación, búsqueda por palabras clave, detalle de productos, adición al carrito con control de stock disponible, modificaciones e item drop.
* **Proceso de Compra e Historial (`HU-11`, `HU-12`, `HU-13`, `HU-14`):** Cobertura robusta de checkout (validaciones de envío, datos de pago erróneos y compra exitosa) y visualización del historial de pedidos del cliente.
* **Panel de Usuario (`HU-09`, `HU-15`):** Excelente validación del menú de navegación, edición de campos de perfil, cambio de clave y ciclo de logout seguro.
* **Gateway y Dashboard Admin (`HU-24`, `HU-25`):** Pruebas rigurosas sobre la pasarela con código secreto `SENA-2026`, validaciones del login administrativo y renderizado de gráficos/métricas del Dashboard.

---

## 3. QUÉ ESTÁ MAL O FALTA (Huecos de Trazabilidad)

Como Ingeniero de QA Senior, detallo los siguientes hallazgos y brechas críticas en el manual de pruebas original al mapear las 31 Historias de Usuario reales:

### A. Historias de Usuario sin Casos de Pruebas (Holes)
1. **Visitante:** `HU-01` (Landing page) y `HU-06` (Perfil público) no poseen pruebas.
2. **Usuario Autenticado:** `HU-08` (Recuperar contraseña), `HU-16` (Reseñas), `HU-17` (Votos), `HU-18` (Favoritos), `HU-19` (Soporte/FAQs) y `HU-20` (Blog) carecen de pruebas documentadas.
3. **Repartidor:** `HU-21` (Registro/Acceso), `HU-22` (Ver asignaciones) y `HU-23` (Marcar entregas) no tienen ninguna cobertura en este manual.
4. **Administrador:** `HU-26` (Gestionar productos), `HU-27` (Categorías), `HU-28` (Logística), `HU-29` (Moderar reseñas) y `HU-30` (Gestionar cuentas) no tienen casos de prueba (solo el Dashboard y los reportes están cubiertos).

### B. Inconsistencias de Negocio y Residuos de Copiado
- **Casos Obsoletos:** `CP-SE-001` menciona el sistema "ServeEasy TJ", el cual pertenece a otra aplicación y representa un residuo de plantilla.
- **Inconsistencia de Arquitectura:** En la sección *Estrategia y Niveles de Prueba* e *Infraestructura* se duplican textos que hacen referencia a "GlassFish", "MySQL (XAMPP)", "dispositivos Android para domiciliarios" y "modo offline de Google Maps". Esto no aplica para la arquitectura real de MIKITECH, que es una aplicación web responsiva en Django y Supabase.
- **Caso Omitido:** El caso de registro con correo duplicado `CP-MK-003` fue omitido físicamente de la numeración del manual de origen.
- **Falta de linealidad:** El módulo Perfil (`CP-MK-USR-001` a `009`) se encuentra desordenado numéricamente tras el módulo de Tienda (`CP-MK-USR-010` a `030`).

---

## 4. PROPUESTA DE CASOS DE PRUEBA FALTANTES

Para cubrir las brechas detectadas en las historias sin cobertura, se proponen los siguientes casos de prueba mínimos:

### Módulo Visitante y Cuenta
* **CP-MK-031 — Visualizar Landing Page (`HU-01`):** Validar la carga de la página raíz (`/`) en menos de 2s mostrando hero, secciones destacadas y categorías.
* **CP-MK-032 — Solicitud de Recuperación de Clave (`HU-08`):** Validar que al solicitar recuperar clave con email registrado se envíe el correo y se reestablezca exitosamente en Supabase Auth.

### Módulo de Interacciones (Cliente)
* **CP-MK-USR-031 — Guardar Favoritos (`HU-18`):** Hacer clic en favorito, verificar que cambie el icono a activo y que el producto aparezca en la pestaña `/usuario/favoritos/`.
* **CP-MK-USR-032 — Publicar Reseña y Puntuación (`HU-16`):** Escribir comentario, seleccionar estrellas y verificar persistencia en el detalle del producto.

### Módulo de Repartidores
* **CP-MK-REP-001 — Acceso a portal Repartidor (`HU-21`):** Validar registro, login de repartidor y bloqueo de acceso al panel privado sin token activo.
* **CP-MK-REP-002 — Actualizar pedido a Entregado (`HU-23`):** Repartidor marca pedido como `DELIVERED`, guardando la hora exacta y notificando al cliente.

### Módulo de Administración (Logística y CRUD)
* **CP-MK-ADM-020 — CRUD de Catálogo de Productos (`HU-26`):** Crear un producto, guardarlo, editar su precio y desactivar su visibilidad desde el panel de administrador.
* **CP-MK-ADM-021 — Carga masiva de catálogo vía Excel (`HU-26`):** Cargar un archivo `.xlsx` estructurado y verificar que los productos se inserten masivamente en base de datos.
* **CP-MK-ADM-022 — Asignación de Repartidores (`HU-28`):** Seleccionar un pedido en preparación, asignarlo a un repartidor activo y cambiar estado a despachado.

---

## 5. MANUAL DE PRUEBAS ORGANIZADO (por Bloques y HUs)

A continuación, se listan los casos de prueba originales estructurados bajo la plantilla ISO 29119, organizados secuencialmente y asociados a su Historia de Usuario (HU).

---

### 🔵 BLOQUE 1: VISITANTE (Sin cuenta)

#### HU-02: Ver catálogo público de productos

1. **ID: CP-MK-USR-010**  
   **Nombre:** Tienda - Carga del catálogo de productos  
   **HU Relacionada:** HU-02  
   **Precondición:** El usuario navega a la sección "Tienda".  
   **Pasos:**  
   1. Hacer clic en el botón de la Tienda.  
   2. Observar la cuadrícula o lista de productos.  
   **Resultado Esperado:** Se cargan las imágenes, nombres, descripciones cortas y precios de los productos disponibles sin errores visuales.  
   **Resultado Real:** Pendiente (Entré a la tienda y todo el catálogo cargó bien).  
   **Estado:** ⏳ Pendiente  

2. **ID: CP-MK-USR-011**  
   **Nombre:** Tienda - Búsqueda de producto específico  
   **HU Relacionada:** HU-02 / HU-05  
   **Precondición:** El usuario está en la tienda.  
   **Pasos:**  
   1. En la barra de búsqueda, ingresar el nombre de un producto que sí existe.  
   2. Presionar Buscar.  
   **Resultado Esperado:** El sistema filtra el catálogo y muestra únicamente el producto o productos que coinciden con la palabra escrita.  
   **Resultado Real:** Pendiente (Busqué "Laptop" y me salieron los resultados correctos).  
   **Estado:** ⏳ Pendiente  

3. **ID: CP-MK-USR-012**  
   **Nombre:** Tienda - Búsqueda sin resultados  
   **HU Relacionada:** HU-02 / HU-05  
   **Precondición:** El usuario está en la tienda.  
   **Pasos:**  
   1. Escribir en el buscador un nombre inventado (ej. "xyz123").  
   2. Presionar Buscar.  
   **Resultado Esperado:** El sistema no se rompe y muestra un mensaje amigable: "No se encontraron productos con esa búsqueda".  
   **Resultado Real:** Pendiente (Busqué un producto raro y el sistema manejó bien el error).  
   **Estado:** ⏳ Pendiente  

#### HU-03: Ver el detalle de un producto

4. **ID: CP-MK-USR-013**  
   **Nombre:** Tienda - Detalles del producto  
   **HU Relacionada:** HU-03  
   **Precondición:** El usuario está viendo el catálogo.  
   **Pasos:**  
   1. Hacer clic en la foto o nombre de un producto.  
   2. Observar la página de detalles.  
   **Resultado Esperado:** Carga la página individual del producto mostrando su precio completo, descripción detallada y stock disponible.  
   **Resultado Real:** Pendiente (Entré a ver los detalles de un producto en específico).  
   **Estado:** ⏳ Pendiente  

#### HU-04: Registrarse como usuario

5. **ID: CP-MK-001**  
   **Nombre:** Registro Exitoso - Datos Válidos  
   **HU Relacionada:** HU-04  
   **Precondición:** El usuario está en la pantalla de registro y no tiene cuenta en Mikitech.  
   **Pasos:**  
   1. Llenar todos los campos obligatorios con datos correctos.  
   2. Clic en el botón "Registrarse".  
   **Resultado Esperado:** El sistema crea la cuenta exitosamente, muestra un mensaje de confirmación y redirige al inicio de sesión o panel principal.  
   **Resultado Real:** ¡Cuenta creada con éxito! Se ingresaron datos válidos y la cuenta se creó sin problemas.  
   **Estado:** ⏳ Pendiente  

6. **ID: CP-MK-002**  
   **Nombre:** Registro Fallido - Campos Vacíos  
   **HU Relacionada:** HU-04  
   **Precondición:** El usuario se encuentra en la pantalla de registro.  
   **Pasos:**  
   1. Dejar todos los campos obligatorios vacíos.  
   2. Hacer clic en el botón "Registrarse".  
   **Resultado Esperado:** El sistema no permite el envío, resalta en rojo los campos obligatorios y muestra un mensaje de error indicando que los campos son requeridos.  
   **Resultado Real:** Se intentó guardar con el formulario vacío y se bloquearon las acciones mostrando los requeridos.  
   **Estado:** ⏳ Pendiente  

7. **ID: CP-MK-003**  
   **Nombre:** Registro Fallido - Correo Duplicado  
   **HU Relacionada:** HU-04  
   **Precondición:** El usuario se encuentra en la pantalla de registro y el correo electrónico a registrar ya existe en el sistema.  
   **Pasos:**  
   1. Llenar los campos obligatorios con datos válidos pero ingresando un correo que ya esté registrado.  
   2. Hacer clic en el botón "Registrarse".  
   **Resultado Esperado:** El sistema bloquea el registro e informa que el correo electrónico ingresado ya está en uso.  
   **Resultado Real:** Se utilizó un correo repetido y el sistema bloqueó el registro mostrando alerta.  
   **Estado:** ⏳ Pendiente  

8. **ID: CP-MK-004**  
   **Nombre:** Registro Fallido - Correo Inválido  
   **HU Relacionada:** HU-04  
   **Precondición:** El usuario se encuentra en la pantalla de registro.  
   **Pasos:**  
   1. Ingresar un correo en formato incorrecto (ej. "usuario@", "usuario.com").  
   2. Llenar los demás campos correctamente.  
   3. Hacer clic en el botón "Registrarse".  
   **Resultado Esperado:** El sistema valida el formato del correo y muestra el mensaje: "Formato de correo electrónico no válido", impidiendo el registro.  
   **Resultado Real:** Pendiente (POR REVISAR: NO ESTÁ VERIFICANDO EMAIL INVÁLIDO).  
   **Estado:** ⏳ Pendiente  

9. **ID: CP-MK-005**  
   **Nombre:** Registro Fallido - Contraseña muy corta  
   **HU Relacionada:** HU-04  
   **Precondición:** El usuario se encuentra en la pantalla de registro.  
   **Pasos:**  
   1. Llenar datos válidos.  
   2. Ingresar una contraseña con longitud menor a la requerida (ej. "12345").  
   3. Hacer clic en el botón "Registrarse".  
   **Resultado Esperado:** El sistema valida la contraseña y muestra un mensaje indicando que es muy corta (ej. "La contraseña debe tener al menos 8 caracteres").  
   **Resultado Real:** Pendiente (Se usó una clave de 5 caracteres y bloqueó).  
   **Estado:** ⏳ Pendiente  

10. **ID: CP-MK-006**  
    **Nombre:** Registro Fallido - Contraseñas no coinciden  
    **HU Relacionada:** HU-04  
    **Precondición:** El usuario se encuentra en la pantalla de registro.  
    **Pasos:**  
    1. Ingresar una contraseña en el campo de clave.  
    2. Ingresar una contraseña diferente en el campo de "Confirmar contraseña".  
    3. Hacer clic en el botón "Registrarse".  
    **Resultado Esperado:** El sistema detecta que no son iguales y muestra el mensaje: "Las contraseñas no coinciden", impidiendo el registro.  
    **Resultado Real:** Pendiente (Se escribió mal la confirmación de la contraseña).  
    **Estado:** ⏳ Pendiente  

11. **ID: CP-MK-007**  
    **Nombre:** Registro Fallido - Contraseña sin formato seguro  
    **HU Relacionada:** HU-04  
    **Precondición:** El usuario se encuentra en la pantalla de registro.  
    **Pasos:**  
    1. Llenar datos válidos.  
    2. Ingresar una contraseña solo con letras minúsculas (sin mayúsculas ni números).  
    3. Hacer clic en el botón "Registrarse".  
    **Resultado Esperado:** El sistema rechaza la clave y pide un formato más seguro (ej. "Debe incluir mayúsculas, números y/o caracteres especiales").  
    **Resultado Real:** Pendiente (Se puso una clave débil y se exigió mayor seguridad).  
    **Estado:** ⏳ Pendiente  

12. **ID: CP-MK-008**  
    **Nombre:** Registro Fallido - Términos no aceptados  
    **HU Relacionada:** HU-04  
    **Precondición:** El usuario se encuentra en la pantalla de registro.  
    **Pasos:**  
    1. Llenar todos los campos obligatorios correctamente.  
    2. Dejar sin marcar la casilla de "Acepto los términos y condiciones".  
    3. Hacer clic en el botón "Registrarse".  
    **Resultado Esperado:** El sistema impide el registro y muestra un error indicando que es obligatorio aceptar los términos para continuar.  
    **Resultado Real:** Pendiente (PENDIENTE POR REALIZAR LOS TÉRMINOS Y CONDICIONES DE LA APP).  
    **Estado:** ⏳ Pendiente  

13. **ID: CP-MK-009**  
    **Nombre:** Registro Fallido - Inyección SQL (Seguridad)  
    **HU Relacionada:** HU-04  
    **Precondición:** El usuario se encuentra en la pantalla de registro.  
    **Pasos:**  
    1. Ingresar en el campo de nombre código SQL como: `' OR 1=1 --`.  
    2. Llenar el resto de campos correctamente.  
    3. Hacer clic en el botón "Registrarse".  
    **Resultado Esperado:** El sistema limpia el texto o muestra error de caracteres inválidos, sin permitir la inyección de código ni comprometer la base de datos.  
    **Resultado Real:** Pendiente (ME DEJA VALIDAR CON CARACTERES ESPECIALES EL NOMBRE).  
    **Estado:** ⏳ Pendiente  

---

### 🟢 BLOQUE 2: USUARIO AUTENTICADO

#### HU-07: Iniciar sesión en Mikitech

14. **ID: CP-MK-010**  
    **Nombre:** Login Exitoso - Credenciales Válidas  
    **HU Relacionada:** HU-07  
    **Precondición:** El usuario tiene una cuenta registrada y activa en Mikitech.  
    **Pasos:**  
    1. Ingresar a la página de inicio de sesión.  
    2. Ingresar el correo electrónico válido.  
    3. Ingresar la contraseña correcta.  
    4. Hacer clic en el botón "Iniciar Sesión".  
    **Resultado Esperado:** El sistema autentica correctamente al usuario y lo redirige a la pantalla principal o Dashboard.  
    **Resultado Real:** Pendiente (Ingreso exitoso con cuenta existente).  
    **Estado:** ⏳ Pendiente  

15. **ID: CP-MK-011**  
    **Nombre:** Login Fallido - Campos Vacíos  
    **HU Relacionada:** HU-07  
    **Precondición:** El usuario se encuentra en la pantalla de inicio de sesión.  
    **Pasos:**  
    1. Dejar los campos de correo y contraseña en blanco.  
    2. Hacer clic en el botón "Iniciar Sesión".  
    **Resultado Esperado:** El sistema no envía el formulario, resalta los campos vacíos y solicita completarlos obligatoriamente.  
    **Resultado Real:** Pendiente  
    **Estado:** ⏳ Pendiente  

16. **ID: CP-MK-012**  
    **Nombre:** Login Fallido - Contraseña Incorrecta  
    **HU Relacionada:** HU-07  
    **Precondición:** El usuario tiene cuenta activa y está en la pantalla de login.  
    **Pasos:**  
    1. Ingresar el correo electrónico válido.  
    2. Ingresar una contraseña incorrecta.  
    3. Hacer clic en el botón "Iniciar Sesión".  
    **Resultado Esperado:** El sistema valida las credenciales y muestra el mensaje: "Credenciales incorrectas" sin permitir el acceso.  
    **Resultado Real:** Pendiente  
    **Estado:** ⏳ Pendiente  

17. **ID: CP-MK-013**  
    **Nombre:** Login Fallido - Correo No Registrado  
    **HU Relacionada:** HU-07  
    **Precondición:** El usuario no está registrado en el sistema.  
    **Pasos:**  
    1. Ingresar un correo electrónico que no existe en la base de datos.  
    2. Ingresar cualquier contraseña.  
    3. Hacer clic en el botón "Iniciar Sesión".  
    **Resultado Esperado:** El sistema muestra un mensaje de error genérico (ej. "Credenciales incorrectas") sin revelar que el correo no existe, por seguridad.  
    **Resultado Real:** Pendiente (Se intentó entrar con cuenta inexistente).  
    **Estado:** ⏳ Pendiente  

18. **ID: CP-MK-014**  
    **Nombre:** Login Fallido - Demasiados Intentos  
    **HU Relacionada:** HU-07  
    **Precondición:** El usuario tiene cuenta activa en Mikitech.  
    **Pasos:**  
    1. Ingresar correo válido.  
    2. Ingresar una contraseña incorrecta 5 veces consecutivas.  
    3. Hacer clic en "Iniciar Sesión".  
    **Resultado Esperado:** El sistema detecta los múltiples intentos fallidos y bloquea temporalmente la cuenta mostrando el mensaje correspondiente.  
    **Resultado Real:** Pendiente (Se bloqueó la cuenta por fallar clave 5 veces).  
    **Estado:** ⏳ Pendiente  

19. **ID: CP-MK-015**  
    **Nombre:** Funcionalidad "Recordarme"  
    **HU Relacionada:** HU-07  
    **Precondición:** El usuario tiene cuenta activa y existe el check de "Recordarme" en el login.  
    **Pasos:**  
    1. Ingresar correo y contraseña válidos.  
    2. Marcar la casilla "Recordarme".  
    3. Hacer clic en "Iniciar Sesión".  
    4. Cerrar el navegador y volver a ingresar a la web.  
    **Resultado Esperado:** El usuario ingresa directamente a su cuenta sin necesidad de volver a autenticarse, debido a que la sesión quedó guardada.  
    **Resultado Real:** Pendiente  
    **Estado:** ⏳ Pendiente  

---

#### HU-09: Ver dashboard personal

20. **ID: CP-MK-USR-001**  
    **Nombre:** Panel Principal - Carga correcta de la interfaz  
    **HU Relacionada:** HU-09  
    **Precondición:** El usuario acaba de iniciar sesión exitosamente.  
    **Pasos:**  
    1. Observar la pantalla de inicio del panel.  
    2. Verificar que la información corresponda al usuario logueado.  
    **Resultado Esperado:** La interfaz carga completamente sin errores visuales, mostrando los menús habilitados y saludando al usuario por su nombre.  
    **Resultado Real:** Pendiente (Revisé que el panel se viera bien y me saludara con mi nombre).  
    **Estado:** ⏳ Pendiente  

21. **ID: CP-MK-USR-002**  
    **Nombre:** Navegación - Funcionamiento de los menús  
    **HU Relacionada:** HU-09  
    **Precondición:** El usuario está dentro del Panel.  
    **Pasos:**  
    1. Hacer clic en cada uno de los enlaces del menú lateral o superior.  
    **Resultado Esperado:** Todos los botones redirigen a la sección correcta sin arrojar páginas en blanco o errores.  
    **Resultado Real:** Pendiente (Hice clic en el menú y todos los botones funcionan).  
    **Estado:** ⏳ Pendiente  

---

#### HU-10: Agregar productos al carrito

22. **ID: CP-MK-USR-014**  
    **Nombre:** Carrito - Agregar producto disponible  
    **HU Relacionada:** HU-10  
    **Precondición:** El usuario está en los detalles de un producto con stock.  
    **Pasos:**  
    1. Seleccionar cantidad "1".  
    2. Hacer clic en "Agregar al Carrito".  
    **Resultado Esperado:** El sistema muestra una notificación de éxito ("Producto agregado") y el icono del carrito arriba cambia de 0 a 1.  
    **Resultado Real:** Pendiente (Agregué exitosamente un ítem a la bolsa de compras).  
    **Estado:** ⏳ Pendiente  

23. **ID: CP-MK-USR-015**  
    **Nombre:** Carrito - Agregar cantidad mayor al Stock  
    **HU Relacionada:** HU-10  
    **Precondición:** Un producto tiene solo 5 unidades disponibles.  
    **Pasos:**  
    1. En el selector de cantidad, escribir "10".  
    2. Clic en "Agregar al Carrito".  
    **Resultado Esperado:** El sistema bloquea la acción y muestra un error: "Cantidad supera el stock disponible".  
    **Resultado Real:** Pendiente (Intenté comprar más de lo que había en bodega y no me dejó).  
    **Estado:** ⏳ Pendiente  

24. **ID: CP-MK-USR-016**  
    **Nombre:** Carrito - Modificar cantidades dentro del carrito  
    **HU Relacionada:** HU-10  
    **Precondición:** El usuario está viendo su carrito con productos.  
    **Pasos:**  
    1. Presionar el botón de "+" para subir la cantidad de un ítem de 1 a 2.  
    2. Observar el precio total.  
    **Resultado Esperado:** La cantidad se actualiza y el precio total (subtotal) se recalcula matemáticamente de manera automática.  
    **Resultado Real:** Pendiente (Subí la cantidad a 2 y el precio subió al doble correctamente).  
    **Estado:** ⏳ Pendiente  

25. **ID: CP-MK-USR-017**  
    **Nombre:** Carrito - Eliminar producto  
    **HU Relacionada:** HU-10  
    **Precondición:** El usuario tiene productos en el carrito.  
    **Pasos:**  
    1. Hacer clic en el icono de la basura ("Eliminar") al lado de un producto en el carrito.  
    **Resultado Esperado:** El producto desaparece de la lista, el precio se descuenta del total y si queda vacío, muestra "Tu carrito está vacío".  
    **Resultado Real:** Pendiente (Borré un ítem de mi lista de compras).  
    **Estado:** ⏳ Pendiente  

26. **ID: CP-MK-USR-030**  
    **Nombre:** Seguridad del Carrito / Compra expirada  
    **HU Relacionada:** HU-10  
    **Precondición:** El usuario agregó productos al carrito y se fue a hacer otra cosa.  
    **Pasos:**  
    1. Dejar productos en el carrito.  
    2. Cerrar sesión o dejar pasar varias horas/días.  
    3. Volver a iniciar sesión.  
    **Resultado Esperado:** El sistema debe mantener guardado su carrito de compras (persistencia) o, si el stock ya se acabó, informarle que el producto ya no está disponible.  
    **Resultado Real:** Pendiente  
    **Estado:** ⏳ Pendiente  

---

#### HU-11: Realizar el proceso de compra

27. **ID: CP-MK-USR-018**  
    **Nombre:** Checkout - Campos de dirección vacíos  
    **HU Relacionada:** HU-11  
    **Precondición:** El usuario presiona "Ir a Pagar" en el carrito.  
    **Pasos:**  
    1. Dejar la "Dirección de envío" en blanco.  
    2. Hacer clic en "Continuar al Pago".  
    **Resultado Esperado:** El sistema no deja avanzar a la sección de tarjeta, resalta la dirección y exige que se llene.  
    **Resultado Real:** Pendiente (Intenté pagar sin decir a dónde debían enviar el pedido).  
    **Estado:** ⏳ Pendiente  

28. **ID: CP-MK-USR-019**  
    **Nombre:** Checkout - Tarjeta con datos incompletos  
    **HU Relacionada:** HU-11  
    **Precondición:** El usuario está en la pasarela de pago de tarjeta.  
    **Pasos:**  
    1. Ingresar el número de tarjeta pero dejar vacío el "Código de seguridad (CVV)" o "Fecha de expiración".  
    2. Clic en "Confirmar Compra".  
    **Resultado Esperado:** El formulario marca en rojo el CVV o fecha y avisa que los datos de la tarjeta están incompletos.  
    **Resultado Real:** Pendiente (Probé intentar meter la tarjeta sin fecha de vencimiento).  
    **Estado:** ⏳ Pendiente  

29. **ID: CP-MK-USR-020**  
    **Nombre:** Checkout - Tarjeta rechazada / Sin fondos  
    **HU Relacionada:** HU-11  
    **Precondición:** El usuario está en la pasarela de pago.  
    **Pasos:**  
    1. Usar una tarjeta válida pero sin saldo o una tarjeta de "Prueba" diseñada para declinar.  
    2. Clic en "Pagar".  
    **Resultado Esperado:** El sistema rechaza el pago, el pedido no se crea y muestra: "Pago rechazado, intente con otra tarjeta".  
    **Resultado Real:** Pendiente (El banco rechazó la tarjeta y el sistema me avisó sin romperse).  
    **Estado:** ⏳ Pendiente  

30. **ID: CP-MK-USR-021**  
    **Nombre:** Checkout - Compra completamente Exitosa  
    **HU Relacionada:** HU-11  
    **Precondición:** El usuario está en la pasarela de pago y los datos de envío están completos.  
    **Pasos:**  
    1. Ingresar una tarjeta de crédito/débito válida y con fondos.  
    2. Clic en "Confirmar y Pagar".  
    **Resultado Esperado:** El pago pasa con éxito. Se muestra la pantalla de confirmación: "¡Gracias por tu compra!" y se genera un número único de pedido (Ej. #MK-999).  
    **Resultado Real:** Pendiente (Pagué exitosamente y me dio mi número de orden).  
    **Estado:** ⏳ Pendiente  

31. **ID: CP-MK-USR-022**  
    **Nombre:** Notificaciones - Correo de compra exitosa  
    **HU Relacionada:** HU-11  
    **Precondición:** Acaba de ejecutarse el caso 021 (Compra exitosa).  
    **Pasos:**  
    1. Abrir la bandeja de entrada del correo con el que se registró el usuario.  
    **Resultado Esperado:** El usuario debe haber recibido un correo de confirmación de Mikitech con el resumen de la compra y el número de pedido.  
    **Resultado Real:** Pendiente (Revisé mi Gmail y me llegó el recibo de compra automático).  
    **Estado:** ⏳ Pendiente  

---

#### HU-12: Ver pedidos activos

32. **ID: CP-MK-USR-026**  
    **Nombre:** Pedidos - Ver detalle de seguimiento (Status)  
    **HU Relacionada:** HU-12  
    **Precondición:** El usuario está en el historial de un pedido reciente.  
    **Pasos:**  
    1. Hacer clic en "Ver Detalle" o "Rastrear" en un pedido.  
    2. Revisar el estado de entrega.  
    **Resultado Esperado:** El sistema muestra los productos comprados, la dirección de entrega y el estatus actual (Ej. "Procesando", "Enviado", "Entregado").  
    **Resultado Real:** Pendiente (Abrí mi compra y vi que estaba en estado "Procesando").  
    **Estado:** ⏳ Pendiente  

---

#### HU-13: Ver historial de compras

33. **ID: CP-MK-USR-023**  
    **Nombre:** Pedidos - Ver historial de compras  
    **HU Relacionada:** HU-13  
    **Precondición:** El usuario ha realizado compras previamente.  
    **Pasos:**  
    1. Ir a la sección "Mis Pedidos" o "Historial" en el Panel.  
    2. Revisar la tabla.  
    **Resultado Esperado:** Carga la lista cronológica de los pedidos, mostrando la fecha, el total pagado y el Estado de cada uno.  
    **Resultado Real:** Pendiente (Abrí mi historial y estaban todas mis compras).  
    **Estado:** ⏳ Pendiente  

34. **ID: CP-MK-USR-024**  
    **Nombre:** Pedidos - Búsqueda de pedido por ID válido  
    **HU Relacionada:** HU-13  
    **Precondición:** El usuario está en "Mis Pedidos".  
    **Pasos:**  
    1. Usar el buscador para meter el número exacto del pedido (ej. #MK-999).  
    2. Presionar Buscar.  
    **Resultado Esperado:** El historial se filtra y muestra únicamente ese pedido específico.  
    **Resultado Real:** Pendiente (Busqué el pedido que acababa de hacer usando el número).  
    **Estado:** ⏳ Pendiente  

35. **ID: CP-MK-USR-025**  
    **Nombre:** Pedidos - Búsqueda de pedido inexistente  
    **HU Relacionada:** HU-13  
    **Precondición:** El usuario está en "Mis Pedidos".  
    **Pasos:**  
    1. Escribir un ID falso en el buscador.  
    2. Presionar Buscar.  
    **Resultado Esperado:** Aparece un mensaje indicando que no se encontró ningún pedido con ese número.  
    **Resultado Real:** Pendiente (Traté de buscar la orden de otra persona y no me salió nada).  
    **Estado:** ⏳ Pendiente  

---

#### HU-14: Ver reportes personales de compra

36. **ID: CP-MK-USR-027**  
    **Nombre:** Reportes - Filtrado por fecha  
    **HU Relacionada:** HU-14  
    **Precondición:** El usuario está en la sección de "Mis Pedidos" o "Reportes".  
    **Pasos:**  
    1. Seleccionar en el filtro "Mes Pasado" o poner fechas manuales (Ej. Del 1 al 30 del mes).  
    2. Aplicar filtro.  
    **Resultado Esperado:** La tabla solo muestra las compras o reportes que caen exactamente en ese rango de días.  
    **Resultado Real:** Pendiente (Filtré mis gastos para ver solo los de abril).  
    **Estado:** ⏳ Pendiente  

37. **ID: CP-MK-USR-028**  
    **Nombre:** Reportes - Rango de fechas ilógico  
    **HU Relacionada:** HU-14  
    **Precondición:** El usuario intenta filtrar.  
    **Pasos:**  
    1. Poner una Fecha de Inicio MAYOR a la Fecha de Fin (Ej. Inicio: 30 Dic / Fin: 1 Dic).  
    2. Aplicar filtro.  
    **Resultado Esperado:** El sistema bloquea el filtro y marca error ("La fecha de inicio no puede ser posterior a la de fin").  
    **Resultado Real:** Pendiente (Puse mal las fechas a propósito y me exigió ponerlas bien).  
    **Estado:** ⏳ Pendiente  

38. **ID: CP-MK-USR-029**  
    **Nombre:** Reportes - Descarga de Recibo/Factura  
    **HU Relacionada:** HU-14  
    **Precondición:** El usuario ve el detalle de un pedido completado.  
    **Pasos:**  
    1. Buscar el botón "Descargar Recibo", "Ver Factura" o "PDF".  
    2. Hacer clic sobre él.  
    **Resultado Esperado:** El sistema genera y descarga un archivo PDF (o lo muestra en pantalla) con los datos del cobro, impuestos y el nombre de la empresa Mikitech.  
    **Resultado Real:** Pendiente (Descargué el PDF de mi compra para guardarlo).  
    **Estado:** ⏳ Pendiente  

---

#### HU-15: Editar mi perfil

39. **ID: CP-MK-USR-003**  
    **Nombre:** Mi Perfil - Visualización de datos  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario navega a la sección de "Mi Perfil".  
    **Pasos:**  
    1. Hacer clic en la opción del Perfil.  
    2. Revisar los datos cargados en el formulario.  
    **Resultado Esperado:** El sistema muestra los datos con los que el usuario se registró correctamente en los campos correspondientes.  
    **Resultado Real:** Pendiente (Entré a Mi Perfil y mis datos de registro estaban ahí).  
    **Estado:** ⏳ Pendiente  

40. **ID: CP-MK-USR-004**  
    **Nombre:** Editar Perfil - Actualización Exitosa  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario se encuentra en "Editar Perfil".  
    **Pasos:**  
    1. Cambiar algún dato permitido (ej. agregar un apellido).  
    2. Hacer clic en "Guardar Cambios".  
    **Resultado Esperado:** El sistema guarda la información, muestra un mensaje de éxito ("Perfil actualizado") y los datos nuevos se ven reflejados.  
    **Resultado Real:** Pendiente (Agregué mi apellido y se guardó correctamente).  
    **Estado:** ⏳ Pendiente  

41. **ID: CP-MK-USR-005**  
    **Nombre:** Editar Perfil - Dejar campo obligatorio vacío  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario está editando su perfil.  
    **Pasos:**  
    1. Borrar por completo el contenido del campo "Nombre".  
    2. Hacer clic en "Guardar Cambios".  
    **Resultado Esperado:** El sistema no permite guardar, resalta el campo en rojo y exige que no quede en blanco.  
    **Resultado Real:** Pendiente (Borré mi nombre para probar y el sistema no me dejó guardar).  
    **Estado:** ⏳ Pendiente  

42. **ID: CP-MK-USR-006**  
    **Nombre:** Cambiar Contraseña - Actualización Exitosa  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario está en la sección de seguridad.  
    **Pasos:**  
    1. Ingresar la contraseña actual válida.  
    2. Ingresar una clave nueva y confirmarla.  
    3. Clic en "Cambiar Contraseña".  
    **Resultado Esperado:** El sistema actualiza la clave y muestra mensaje de confirmación.  
    **Resultado Real:** Pendiente (Puse una clave nueva y se actualizó sin problema).  
    **Estado:** ⏳ Pendiente  

43. **ID: CP-MK-USR-007**  
    **Nombre:** Cambiar Contraseña - Contraseña actual errónea  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario intenta cambiar su clave.  
    **Pasos:**  
    1. Escribir una clave actual equivocada.  
    2. Poner la clave nueva y confirmar.  
    3. Clic en "Cambiar Contraseña".  
    **Resultado Esperado:** El sistema deniega el cambio y muestra: "La contraseña actual es incorrecta".  
    **Resultado Real:** Pendiente (Fallé a propósito mi clave vieja y el sistema me bloqueó).  
    **Estado:** ⏳ Pendiente  

44. **ID: CP-MK-USR-008**  
    **Nombre:** Cierre de Sesión (Logout)  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario ha terminado sus tareas.  
    **Pasos:**  
    1. Hacer clic en el botón de "Cerrar sesión" o "Salir".  
    **Resultado Esperado:** La sesión finaliza y el sistema lo redirige de vuelta a la página principal o de Login.  
    **Resultado Real:** Pendiente (Le di salir y me devolvió al login).  
    **Estado:** ⏳ Pendiente  

45. **ID: CP-MK-USR-009**  
    **Nombre:** Seguridad - Regresar después del Logout  
    **HU Relacionada:** HU-15  
    **Precondición:** El usuario acaba de cerrar sesión exitosamente.  
    **Pasos:**  
    1. Presionar el botón de "Atrás" en el navegador web e intentar recargar.  
    **Resultado Esperado:** El sistema detecta que ya no hay sesión activa y bloquea el paso, obligando a loguearse de nuevo.  
    **Resultado Real:** Pendiente (Me intenté devolver con la flecha del navegador y no me dejó entrar).  
    **Estado:** ⏳ Pendiente  

---

### 🔴 BLOQUE 3: ADMINISTRADOR

#### HU-24: Acceder al gateway de administración

46. **ID: CP-MK-ADM-001**  
    **Nombre:** Código de Acceso - Código Válido  
    **HU Relacionada:** HU-24  
    **Precondición:** El usuario ingresa a la página de seguridad/código de acceso.  
    **Pasos:**  
    1. Ingresar el código de acceso secreto correcto en el campo.  
    2. Hacer clic en "Validar" o "Continuar".  
    **Resultado Esperado:** El sistema valida que el código es correcto y redirige al usuario a la pantalla de Login del Administrador.  
    **Resultado Real:** Pendiente (Puse el código de acceso correcto y me dejó pasar al formulario de LOGIN).  
    **Estado:** ⏳ Pendiente  

47. **ID: CP-MK-ADM-002**  
    **Nombre:** Código de Acceso - Campo Vacío  
    **HU Relacionada:** HU-24  
    **Precondición:** El usuario está en la página del código de acceso.  
    **Pasos:**  
    1. Dejar el campo del código de acceso totalmente en blanco.  
    2. Hacer clic en "Validar".  
    **Resultado Esperado:** El sistema no avanza y muestra un mensaje de error obligatorio (ej. "Por favor ingrese el código de acceso").  
    **Resultado Real:** Pendiente (Intenté darle al botón de continuar sin escribir ningún código).  
    **Estado:** ⏳ Pendiente  

48. **ID: CP-MK-ADM-003**  
    **Nombre:** Código de Acceso - Código Incorrecto  
    **HU Relacionada:** HU-24  
    **Precondición:** El usuario está en la página del código de acceso.  
    **Pasos:**  
    1. Ingresar un código inventado o erróneo (ej. 12345).  
    2. Hacer clic en "Validar".  
    **Resultado Esperado:** El sistema rechaza el intento y muestra el error: "Código de acceso incorrecto" o "Acceso denegado".  
    **Resultado Real:** Pendiente (Escribí un código falso para ver si el sistema me bloqueaba).  
    **Estado:** ⏳ Pendiente  

49. **ID: CP-MK-ADM-010**  
    **Nombre:** Login Admin - Campo Correo vacío  
    **HU Relacionada:** HU-24  
    **Precondición:** El administrador recién registrado entra al Login.  
    **Pasos:**  
    1. Dejar el campo Correo en blanco.  
    2. Escribir la contraseña.  
    3. Clic en "Iniciar sesión".  
    **Resultado Esperado:** El login no avanza y muestra el error: "El correo es obligatorio para iniciar sesión".  
    **Resultado Real:** Pendiente (Quise loguearme solo con la contraseña y me pidió el correo).  
    **Estado:** ⏳ Pendiente  

50. **ID: CP-MK-ADM-011**  
    **Nombre:** Login Admin - Campo Contraseña vacío  
    **HU Relacionada:** HU-24  
    **Precondición:** El administrador está en el Login.  
    **Pasos:**  
    1. Escribir el correo válido.  
    2. Dejar la contraseña en blanco.  
    3. Clic en "Iniciar sesión".  
    **Resultado Esperado:** El login no avanza y muestra el error: "La contraseña es obligatoria".  
    **Resultado Real:** Pendiente (Puse el correo pero dejé la clave vacía).  
    **Estado:** ⏳ Pendiente  

51. **ID: CP-MK-ADM-012**  
    **Nombre:** Login Admin - Correo No Registrado  
    **HU Relacionada:** HU-24  
    **Precondición:** El administrador está en el Login.  
    **Pasos:**  
    1. Escribir un correo que no existe en la base de datos.  
    2. Poner cualquier clave y dar clic en iniciar.  
    **Resultado Esperado:** El sistema rechaza el acceso y muestra error: "Credenciales incorrectas" (No debe revelar que el correo no existe).  
    **Resultado Real:** Pendiente (Probé entrar con un correo falso).  
    **Estado:** ⏳ Pendiente  

52. **ID: CP-MK-ADM-013**  
    **Nombre:** Login Admin - Contraseña Incorrecta  
    **HU Relacionada:** HU-24  
    **Precondición:** El administrador está en el Login.  
    **Pasos:**  
    1. Poner el correo de Admin correcto.  
    2. Escribir una contraseña mala.  
    3. Clic en "Iniciar Sesión".  
    **Resultado Esperado:** El sistema deniega el acceso y muestra el error: "Credenciales incorrectas".  
    **Resultado Real:** Pendiente (Puse mi correo bien pero me equivoqué de clave).  
    **Estado:** ⏳ Pendiente  

53. **ID: CP-MK-ADM-014**  
    **Nombre:** Login Admin - Ingreso Exitoso  
    **HU Relacionada:** HU-24  
    **Precondición:** El administrador está en el Login.  
    **Pasos:**  
    1. Poner correo y contraseña de Admin correctos.  
    2. Clic en "Iniciar sesión".  
    **Resultado Esperado:** El sistema valida las credenciales y da acceso total al Panel de Administrador de Mikitech.  
    **Resultado Real:** Pendiente (Ingresé bien mis datos y entré al panel).  
    **Estado:** ⏳ Pendiente  

---

#### HU-25: Ver el panel principal (Dashboard admin)

54. **ID: CP-MK-DASH-001**  
    **Nombre:** Dashboard - Carga de métricas y tarjetas de resumen  
    **HU Relacionada:** HU-25  
    **Precondición:** El administrador inicia sesión y es dirigido al Dashboard.  
    **Pasos:**  
    1. Observar la pantalla principal (Dashboard).  
    2. Revisar las tarjetas de resumen numéricas (Ej. "Ventas de hoy", "Nuevos Usuarios", "Pedidos pendientes").  
    **Resultado Esperado:** Todas las tarjetas cargan correctamente, sin mostrar "NaN" o "Errores", y la suma de datos coincide lógicamente con la base de datos real.  
    **Resultado Real:** Pendiente (Entré al Dashboard y verifiqué que los números totales cargaran bien).  
    **Estado:** ⏳ Pendiente  

55. **ID: CP-MK-DASH-002**  
    **Nombre:** Dashboard - Redirección desde las tarjetas  
    **HU Relacionada:** HU-25  
    **Precondición:** El administrador está viendo las tarjetas de resumen.  
    **Pasos:**  
    1. Hacer clic en una de las tarjetas (Por ejemplo, hacer clic en "Ver los 10 pedidos pendientes").  
    **Resultado Esperado:** El sistema debe funcionar como un acceso rápido y redirigir automáticamente a la sección completa de Pedidos o Usuarios.  
    **Resultado Real:** Pendiente (Le di clic a la tarjeta de ventas y me llevó a la tabla de ventas).  
    **Estado:** ⏳ Pendiente  

56. **ID: CP-MK-DASH-003**  
    **Nombre:** Dashboard - Visualización de Gráficos  
    **HU Relacionada:** HU-25  
    **Precondición:** El administrador está en la vista del Dashboard.  
    **Pasos:**  
    1. Bajar la pantalla para ver los gráficos (Ej. "Ventas por mes" o "Usuarios registrados").  
    2. Pasar el puntero del mouse sobre las barras o líneas del gráfico.  
    **Resultado Esperado:** Los gráficos se dibujan sin errores y, al pasar el mouse por encima (hover), aparece una etiqueta mostrando el detalle exacto del número o la fecha.  
    **Resultado Real:** Pendiente (Probé que la gráfica de barras fuera interactiva).  
    **Estado:** ⏳ Pendiente  

57. **ID: CP-MK-DASH-004**  
    **Nombre:** Dashboard - Filtro de tiempo (Semana, Mes, Año)  
    **HU Relacionada:** HU-25  
    **Precondición:** El Dashboard tiene un filtro de fecha arriba.  
    **Pasos:**  
    1. Cambiar el selector de fecha (Por ejemplo, cambiar de "Hoy" a "Último Mes").  
    2. Hacer clic en "Aplicar" o esperar a que recargue.  
    **Resultado Esperado:** Tanto las gráficas como las tarjetas de números se actualizan instantáneamente mostrando únicamente la información de ese rango de fechas.  
    **Resultado Real:** Pendiente (Filtré las ventas para ver solo las de esta semana).  
    **Estado:** ⏳ Pendiente  

58. **ID: CP-MK-DASH-005**  
    **Nombre:** Dashboard - Tabla de Actividad Reciente  
    **HU Relacionada:** HU-25  
    **Precondición:** Hay compras o registros de usuarios hechos recientemente.  
    **Pasos:**  
    1. Buscar en el Dashboard la sección de "Últimos pedidos" o "Actividad reciente".  
    2. Hacer un pedido nuevo con un usuario de prueba en otra pestaña.  
    3. Recargar el Dashboard.  
    **Resultado Esperado:** La tabla muestra los eventos más recientes de forma cronológica (el pedido nuevo aparece inmediatamente de primero en la lista).  
    **Resultado Real:** Pendiente (Hice una compra de prueba y vi cómo apareció rápido en la actividad reciente).  
    **Estado:** ⏳ Pendiente  

59. **ID: CP-MK-DASH-007**  
    **Nombre:** Dashboard - Alertas y Notificaciones del sistema  
    **HU Relacionada:** HU-25  
    **Precondición:** Hay alguna notificación pendiente (ej. Un usuario solicitó un reembolso, poco stock).  
    **Pasos:**  
    1. Buscar el icono de "Campanita" o el panel de "Alertas" en el Dashboard.  
    2. Hacer clic sobre él.  
    **Resultado Esperado:** Se despliega la lista de alertas pendientes. Al hacer clic en una, marca la alerta como "leída" y redirige al administrador a la pantalla para solucionarla.  
    **Resultado Real:** Pendiente  
    **Estado:** ⏳ Pendiente  

---

#### HU-31: Ver reportes globales del negocio

60. **ID: CP-MK-DASH-006**  
    **Nombre:** Dashboard - Exportar Reporte General  
    **HU Relacionada:** HU-31  
    **Precondición:** El administrador está viendo los gráficos y resúmenes.  
    **Pasos:**  
    1. Ubicar el botón de "Descargar Reporte", "Exportar CSV" o "Imprimir".  
    **Resultado Esperado:** Se descarga un archivo (Excel, CSV o PDF) con un resumen limpio y legible de las métricas que se ven en la pantalla.  
    **Resultado Real:** Pendiente (Exporté los datos a Excel para asegurarme de que no fallara).  
    **Estado:** ⏳ Pendiente  

---

## 6. RESUMEN EJECUTIVO

- **Total de Historias de Usuario (HUs):** 31
- **Total Casos de Prueba existentes:** 60 *(Excluyendo el caso obsoleto CP-SE-001 e incorporando el omitido CP-MK-003)*
- **Cobertura actual:** **45.2%** (14 HUs cubiertas de 31)
- **HUs 100% cubiertas (14 HUs):**
  - `HU-02` (Ver catálogo público)
  - `HU-03` (Ver detalle producto)
  - `HU-04` (Registrarse)
  - `HU-05` (Buscador global)
  - `HU-07` (Iniciar sesión)
  - `HU-09` (Dashboard personal)
  - `HU-10` (Carrito)
  - `HU-11` (Checkout)
  - `HU-12` (Pedidos activos)
  - `HU-13` (Historial de compras)
  - `HU-14` (Reportes personales)
  - `HU-15` (Editar perfil)
  - `HU-24` (Gateway admin)
  - `HU-25` (Dashboard admin)
- **HUs parcialmente cubiertas (1 HU):**
  - `HU-31` (Reportes globales) - Cubre exportación de Dashboard.
- **HUs sin cobertura (16 HUs):**
  - `HU-01` (Landing page visitor)
  - `HU-06` (Perfil público visitor)
  - `HU-08` (Recuperar contraseña)
  - `HU-16` (Reseñas)
  - `HU-17` (Votos)
  - `HU-18` (Favoritos)
  - `HU-19` (Soporte y FAQ)
  - `HU-20` (Blog)
  - `HU-21` (Registro/Acceso repartidor)
  - `HU-22` (Pedidos asignados repartidor)
  - `HU-23` (Entregas repartidor)
  - `HU-26` (Catálogo admin)
  - `HU-27` (Categorías admin)
  - `HU-28` (Logística admin)
  - `HU-29` (Reseñas admin)
  - `HU-30` (Usuarios admin)

---

## 7. RECOMENDACIONES

Como Líder de Aseguramiento de Calidad, recomiendo las siguientes acciones para optimizar la trazabilidad y la madurez de las pruebas en MIKITECH:

1. **Implementar Casos de Prueba para Historias Críticas Huérfanas:** Es crucial diseñar pruebas para el módulo de repartidores (`HU-21` a `HU-23`) y para el catálogo administrativo y logística (`HU-26` a `HU-30`), ya que son las áreas operativas clave sin cobertura.
2. **Corrección de Datos en el Entorno:** Retirar del manual toda información asociada a proyectos ajenos (ej. "ServeEasy TJ", GlassFish o aplicaciones móviles con sincronización offline) y reflejar la pila tecnológica real (Django + Supabase en entorno Web responsivo).
3. **Validación del Módulo de Registro y Seguridad:** Solucionar los hallazgos en la verificación de email inválido (`CP-MK-004`) y la inyección SQL en campo de nombre (`CP-MK-009`) para evitar incidentes en producción.
4. **Automatización del Carrito y Pagos:** Implementar pruebas automáticas (E2E) para la persistencia del carrito en la sesión del usuario (`CP-MK-USR-030`) y el flujo completo de pago con tarjeta (`CP-MK-USR-021`).
