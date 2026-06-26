# DIAGRAMAS DE ARQUITECTURA Y DISEÑO — MIKITECH E-COMMERCE

Este documento contiene los diagramas formales de arquitectura de procesos y del modelo lógico de datos (Entidad-Relación) de la plataforma MIKITECH E-Commerce. Estos diagramas sirven de base para el equipo de desarrollo y aseguramiento de calidad (QA).

> [!NOTE]
> Todos los diagramas de este archivo están desarrollados bajo la sintaxis **Mermaid.js**. Si visualizas este documento en un IDE compatible o plataforma como GitHub, se renderizarán de forma gráfica e interactiva.

> [!TIP]
> **Para usar en Mermaid Live Editor (https://mermaid.live):**
> Copia únicamente el contenido de texto que está entre las marcas de `<!-- INICIO ... -->` y `<!-- FIN ... -->` (excluyendo las comillas triples ```).

---

## 1. DIAGRAMAS DE PROCESOS (Flujos de Negocio)

A continuación se detallan los tres flujos operacionales principales del e-commerce correspondientes a los diferentes actores del sistema.

### A. Ciclo de Compra y Checkout (Cliente)
Este diagrama de flujo describe el camino de un usuario desde que ingresa como visitante al catálogo hasta que completa una transacción y se realiza el despacho de su pedido.

<!-- INICIO DIAGRAMA COMPRA CLIENTE (Copiar desde aquí) -->
```mermaid
flowchart TD
    Start([Inicio: Cliente en el Home]) --> publicCatalog[Navegar Catálogo Público HU-02]
    publicCatalog --> selectProduct[Ver Detalle del Producto HU-03]
    selectProduct --> addCart[Agregar al Carrito HU-10]
    addCart --> askCart{¿Seguir Comprando?}
    askCart -- Sí --> publicCatalog
    askCart -- No --> checkAuth{¿Usuario Autenticado?}
    
    checkAuth -- No --> loginPage[Ir a Registro / Login HU-04/HU-07]
    loginPage --> registerSuccess{¿Ingreso Exitoso?}
    registerSuccess -- No --> loginPage
    registerSuccess -- Sí --> checkoutPage[Ir al Checkout HU-11]
    
    checkAuth -- Sí --> checkoutPage
    
    checkoutPage --> fillShipping[Ingresar Dirección y Teléfono]
    fillShipping --> paymentGate[Procesar Pago con Tarjeta]
    paymentGate --> paymentSuccess{¿Transacción Aprobada?}
    
    paymentSuccess -- No --> paymentError[Mostrar Error y Reintentar]
    paymentError --> paymentGate
    
    paymentSuccess -- Sí --> createOrder[Registrar Pedido como PENDING]
    createOrder --> updateStock[Descontar Stock en Bodega]
    updateStock --> sendEmail[Enviar Correo de Confirmación HU-11]
    sendEmail --> clearCart[Vaciar Carrito de Compras]
    clearCart --> End([Fin: Pedido Registrado])
```
<!-- FIN DIAGRAMA COMPRA CLIENTE (Hasta aquí) -->

---

### B. Ciclo de Despacho y Entrega (Repartidor)
Describe el proceso que realiza un repartidor (domiciliario) registrado para entregar un pedido en camino.

<!-- INICIO DIAGRAMA ENTREGA REPARTIDOR (Copiar desde aquí) -->
```mermaid
flowchart TD
    StartRep([Inicio: Login de Repartidor HU-21]) --> checkAssigned[Consultar Pedidos Asignados HU-22]
    checkAssigned --> selectOrder[Seleccionar Pedido en Ruta]
    selectOrder --> checkRoute[Consultar Dirección de Entrega]
    checkRoute --> deliverOrder[Transportar y Entregar Pedido]
    deliverOrder --> confirmDelivery{¿Entrega Exitosa?}
    
    confirmDelivery -- Sí --> markDelivered[Marcar como ENTREGADO HU-23]
    markDelivered --> notifyClient[Notificar y Guardar Hora Exacta]
    notifyClient --> EndRep([Fin: Entrega Completada])
    
    confirmDelivery -- No --> markReturned[Marcar como NO_ENTREGADO / Novedad]
    markReturned --> returnWarehouse[Retornar Producto a Bodega]
    returnWarehouse --> EndRep
```
<!-- FIN DIAGRAMA ENTREGA REPARTIDOR (Hasta aquí) -->

---

### C. Ciclo de Gestión y Auditoría (Administrador)
Describe la pasarela de seguridad y las operaciones del administrador en el Panel de Control.

<!-- INICIO DIAGRAMA AUDITORÍA ADMIN (Copiar desde aquí) -->
```mermaid
flowchart TD
    StartAdmin([Inicio: Acceso a Consola Admin]) --> adminGateway[Pasarela de Código de Seguridad HU-24]
    adminGateway --> checkCode{¿Código SENA-2026?}
    checkCode -- Incorrecto --> denyAccess[Acceso Denegado / Bloqueo]
    denyAccess --> adminGateway
    
    checkCode -- Correcto --> adminLogin[Ingresar Credenciales Administrativas]
    adminLogin --> checkCreds{¿Usuario Admin Activo?}
    checkCreds -- No --> denyAccess
    
    checkCreds -- Sí --> adminDashboard[Acceder a Dashboard Admin HU-25]
    adminDashboard --> selectModule{Seleccionar Módulo}
    
    selectModule -- Catálogo --> crudProducts[Crear/Modificar Productos HU-26]
    selectModule -- Carga Masiva --> excelImport[Carga Masiva vía Excel HU-26]
    selectModule -- Logística --> assignRider[Asignar Repartidores a Pedidos HU-28]
    selectModule -- Usuarios --> manageAccounts[Activar / Suspender Cuentas HU-30]
    selectModule -- Reportes --> viewReports[Visualizar Métricas y Exportar CSV HU-31]
    
    crudProducts --> finishAdmin([Fin de Operaciones])
    excelImport --> finishAdmin
    assignRider --> finishAdmin
    manageAccounts --> finishAdmin
    viewReports --> finishAdmin
```
<!-- FIN DIAGRAMA AUDITORÍA ADMIN (Hasta aquí) -->

---

## 2. DIAGRAMA DE ENTIDAD-RELACIÓN (ERD)

Este diagrama representa el modelo lógico de la base de datos de **MIKITECH** implementada en **Supabase (PostgreSQL)** e integrada con los modelos de **Django**. Mapea las tablas de negocio, seguridad y estadísticas con sus atributos y llaves foráneas.

<!-- INICIO DIAGRAMA ENTIDAD-RELACIÓN ERD (Copiar desde aquí) -->
```mermaid
erDiagram
    AUTH_USERS ||--|| PERFIL : "vincula a"
    PERFIL ||--o{ PEDIDO : "realiza"
    PERFIL ||--o{ PEDIDO : "despacha (rol repartidor)"
    PERFIL ||--o{ RESENA : "escribe"
    PERFIL ||--o{ FAVORITO : "guarda"
    
    CATEGORIA ||--o{ PRODUCTO : "clasifica"
    PRODUCTO ||--o{ DETALLE_PEDIDO : "se incluye en"
    PEDIDO ||--o{ DETALLE_PEDIDO : "contiene"
    PRODUCTO ||--o{ RESENA : "recibe"
    PRODUCTO ||--o{ FAVORITO : "marcado en"

    AUTH_USERS {
        uuid id PK
        string email "Único"
        datetime created_at
    }

    PERFIL {
        uuid id PK
        uuid user_id FK "Relación 1:1 con auth.users"
        string username "Único"
        string nombre_completo
        string telefono
        string direccion_envio
        string rol "Cliente, Administrador, Repartidor"
        string estado "Activo, Suspendido"
        string avatar_url "Almacenado en Supabase Storage"
    }

    CATEGORIA {
        integer id PK
        string nombre "Único"
        string descripcion
        string slug "Indexado"
    }

    PRODUCTO {
        integer id PK
        integer categoria_id FK
        string nombre
        string descripcion
        decimal precio
        integer stock
        string imagen_url
        boolean es_kit "Define si es combo"
        boolean activo "Visibilidad en catálogo"
    }

    PEDIDO {
        integer id PK
        uuid cliente_id FK "Relación con Perfil (Cliente)"
        uuid repartidor_id FK "Relación con Perfil (Repartidor), Nulo por defecto"
        datetime fecha_pedido
        string estado "PENDIENTE, PREPARACION, DESPACHADO, ENTREGADO, CANCELADO"
        decimal total
        string direccion_entrega
        string telefono_contacto
    }

    DETALLE_PEDIDO {
        integer id PK
        integer pedido_id FK
        integer producto_id FK
        integer cantidad
        decimal precio_unitario
        decimal subtotal
    }

    RESENA {
        integer id PK
        integer producto_id FK
        uuid cliente_id FK
        integer puntuacion "Rango 1 a 5 estrellas"
        string comentario
        datetime fecha_publicacion
        boolean aprobado "Visibilidad pública"
    }

    FAVORITO {
        integer id PK
        uuid cliente_id FK
        integer producto_id FK
    }
```
<!-- FIN DIAGRAMA ENTIDAD-RELACIÓN ERD (Hasta aquí) -->
