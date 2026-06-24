# 📋 Diagrama de Procesos - E-commerce MIKITECH

Este documento detalla y explica el flujo de procesos del **Ciclo de Compra y Checkout de la aplicación MIKITECH**, el cual organiza las responsabilidades y transiciones de estados entre el Cliente, la Plataforma Backend con Supabase, y el equipo de Logística y Despacho.

El flujo completo interactivo y responsivo se encuentra disponible en formato HTML/CSS en el archivo [diagrama_procesos.html](file:///c:/Users/turca/Desktop/MIKITECH-APP/diagrama_procesos.html).

---

## 👥 Roles y Actores del Proceso

El flujo de compra se distribuye en **3 carriles (swimlanes)** que delimitan las responsabilidades operativas y lógicas:

1. **👤 Cliente (Usuario):**
   * Explora los productos de hardware en la tienda.
   * Agrega artículos a su carrito y procede a completar sus datos en el checkout.
   * Realiza el pago electrónico y espera el arribo de su paquete para realizar la verificación final.
2. **⚙️ Sistema y Supabase (Backend Django):**
   * Valida automáticamente el stock del inventario en la base de datos de Supabase.
   * Procesa las llamadas HTTP a la pasarela de pagos (ej: Stripe).
   * Genera el registro de la Orden de Compra, descuenta stock y despacha notificaciones por correo de forma automatizada.
3. **📦 Logística y Despacho (Administrador de Bodega):**
   * Recibe la alerta de la orden aprobada y pagada en el panel de control.
   * Prepara físicamente el hardware (picking & packing) y genera la etiqueta.
   * Despacha el paquete con la transportadora y registra el número de guía de seguimiento.

---

## 🔄 Descripción Detallada del Flujo de Compra

El proceso fluye de la siguiente manera:

### 1. Selección y Validación de Inventario
* El **Cliente** explora el catálogo de hardware y agrega componentes a su carrito.
* La acción de agregar al carrito activa en el **Sistema** la tarea de **Validar stock de productos**.
* **Bifurcación / Gateway de Stock**:
  * **NO (Sin Stock)**: Se notifica la falta de inventario y se regresa al Cliente al flujo de ajuste de su carrito.
  * **SÍ (Con Stock)**: Permite al Cliente avanzar y ejecutar la acción **Proceder al Checkout**.

### 2. Procesamiento de Checkout y Pago
* El **Cliente** completa sus datos de envío y hace clic en **Confirmar y Realizar Pago**.
* El **Sistema** procesa la transacción de pago.
* **Bifurcación / Gateway de Pago**:
  * **NO (Transacción Fallida)**: Se notifica el fallo en la transacción y se regresa al Cliente a la pantalla de pago para reintentar con otro medio.
  * **SÍ (Aprobado)**: Se genera la Orden de Compra definitiva en la base de datos, se descuenta el stock del inventario permanentemente y se envía un correo de confirmación.

### 3. Alistamiento y Despacho Físico (Logística)
* El equipo de **Logística** recibe la orden de compra aprobada en bodega.
* Se procede a **Empacar el hardware** y **Despachar el paquete** mediante la transportadora.
* Una vez entregado el paquete a la transportadora, el despachador ejecuta la tarea **Registrar número de guía**.

### 4. Entrega y Cierre
* El registro de la guía notifica al **Cliente**, quien pasa al estado **Esperar entrega**.
* Al recibir el paquete físico de la transportadora, el **Cliente** realiza la tarea de **Recibir pedido y verificar hardware**.
* El proceso finaliza con éxito (**Pedido Entregado**).

---

## 📊 Representación Gráfica (Mermaid BPMN Diagram)

Diagrama de carriles horizontales que representa la lógica del ciclo de compra en MIKITECH:

```mermaid
flowchart TB
    subgraph Cliente ["👤 Carril: Cliente (Usuario)"]
        start([Inicio]) --> browse[Explorar catálogo]
        browse --> cart[Agregar al carrito]
        checkout[Proceder al Checkout] --> pay[Realizar Pago]
        wait[Esperar entrega] --> receive[Recibir pedido / Verificar]
    end

    subgraph Sistema ["⚙️ Carril: Sistema & Supabase"]
        check_stock[Validar stock] --> dec_stock{¿Hay stock?}
        dec_stock -- No --> no_stock[No: Notificar falta de stock]
        dec_stock -- Sí --> checkout
        
        process_pay[Procesar Pago] --> dec_pay{¿Pago exitoso?}
        dec_pay -- No --> no_pay[No: Notificar fallo pago]
        dec_pay -- Sí --> create_order[Sí: Registrar Orden & Descontar stock]
    end

    subgraph Logistica ["📦 Carril: Logística y Despacho"]
        pack[Empacar hardware] --> ship[Despachar paquete]
        ship --> register_ship[Registrar guía de envío]
    end

    %% Transiciones entre carriles
    cart -.-> check_stock
    no_stock -.-> cart
    pay -.-> process_pay
    no_pay -.-> pay
    create_order --> pack
    register_ship -.-> wait
    
    receive --> finished([Pedido Entregado / Fin])
    
    style start fill:#22c55e,stroke:#15803d,color:#fff
    style finished fill:#ef4444,stroke:#b91c1c,color:#fff
    style dec_stock fill:#fef3c7,stroke:#d97706,color:#b45309
    style dec_pay fill:#fef3c7,stroke:#d97706,color:#b45309
    style no_stock fill:#fee2e2,stroke:#f87171,color:#991b1b
    style no_pay fill:#fee2e2,stroke:#f87171,color:#991b1b
```

---

## 🔗 Enlace al Documento de Visualización Interactiva
Para interactuar visualmente con las swimlanes a color, las cajas adaptativas y las flechas de flujo calculadas por SVG, abre el archivo local en tu navegador:
👉 **[diagrama_procesos.html](file:///c:/Users/turca/Desktop/MIKITECH-APP/diagrama_procesos.html)**

---

## 🎭 Diagrama de Casos de Uso (PlantUML)

A continuación se presenta el código fuente en formato PlantUML para el **Diagrama de Casos de Uso** del sistema MIKITECH, que modela las interacciones de los cuatro roles principales: **Visitante**, **Cliente**, **Repartidor** y **Administrador**.

```plantuml
@startuml
title Diagrama de Casos de Uso - MIKITECH E-Commerce

left to right direction
skinparam packageStyle rectangle

actor Visitante as vis
actor Cliente as cli
actor Repartidor as rep
actor Administrador as adm

cli --|> vis

rectangle "Sistema MIKITECH" {
  usecase "Visualizar Landing Page y Catalogo" as UC1
  usecase "Ver Detalle de Producto" as UC2
  usecase "Buscar Producto" as UC3
  usecase "Registrarse en Plataforma" as UC4
  usecase "Ver Perfil Publico de Usuario" as UC5
  
  usecase "Iniciar Sesion" as UC6
  usecase "Recuperar Contrasena" as UC7
  usecase "Gestionar Carrito de Compras" as UC8
  usecase "Realizar Checkout y Compra" as UC9
  usecase "Procesar Pago Electronico" as UC9_1
  usecase "Ver Pedidos y Seguimiento" as UC10
  usecase "Ver Historial y Reportes" as UC11
  usecase "Editar Perfil y Direccion" as UC12
  usecase "Agregar Resenas y Votos" as UC13
  usecase "Guardar en Favoritos" as UC14
  usecase "Acceder a Soporte y FAQ" as UC15

  usecase "Acceder a Portal Repartidor" as UC16
  usecase "Ver Entregas Asignadas" as UC17
  usecase "Marcar Pedido como Entregado" as UC18
  usecase "Registrar Novedad / Fallido" as UC19

  usecase "Acceder a Consola Admin (Codigo)" as UC20
  usecase "Gestionar Catalogo e Inventario" as UC21
  usecase "Importar Excel (Carga Masiva)" as UC22
  usecase "Asignar Repartidores y Ver Facturas" as UC23
  usecase "Moderar Resenas" as UC24
  usecase "Suspender / Reactivar Cuentas" as UC25
  usecase "Visualizar Metricas y Reportes" as UC26
}

vis --> UC1
vis --> UC2
vis --> UC3
vis --> UC4
vis --> UC5

cli --> UC6
cli --> UC7
cli --> UC8
cli --> UC9
cli --> UC10
cli --> UC11
cli --> UC12
cli --> UC13
cli --> UC14
cli --> UC15

UC9 ..> UC9_1 : <<include>>

rep --> UC16
rep --> UC17
rep --> UC18
UC18 <.. UC19 : <<extend>>

adm --> UC20
adm --> UC21
adm --> UC23
adm --> UC24
adm --> UC25
adm --> UC26

UC21 <.. UC22 : <<extend>>

@enduml
```

---

## 📐 Diagrama de Clases (PlantUML)

Este diagrama representa la estructura de clases del backend de **MIKITECH** basado en Django Models. Define las propiedades, tipos de datos, métodos de negocio y las relaciones estructurales entre los modelos principales de **Usuarios**, **Productos** e **Interacciones/Ventas**.

```plantuml
@startuml
title Diagrama de Clases (Vista Logica) - MIKITECH E-Commerce

skinparam classAttributeIconSize 0
skinparam linetype ortho
left to right direction

package "Modulo de Usuarios (users)" {
  class Perfil {
    + UUID id
    + String nombre_completo
    + String nombre_usuario
    + String biografia
    + String url_avatar
    + String telefono
    + String direccion
    + String ciudad
    + String pais
    + String rol
    + Boolean esta_activo
    + DateTime creado_el
    + DateTime actualizado_el
    + es_administrador() : Boolean
    + nombre_mostrado() : String
    + email() : String
  }

  class Notificacion {
    + UUID id
    + String mensaje
    + Boolean esta_leida
    + DateTime creado_el
  }
}

package "Modulo de Productos (products)" {
  class Categoria {
    + UUID id
    + String nombre
    + String enlace
    + String descripcion
    + String icono
    + String url_imagen
    + DateTime creado_el
    + DateTime actualizado_el
  }

  class Producto {
    + UUID id
    + String nombre
    + String enlace
    + String descripcion
    + String descripcion_corta
    + Decimal precio
    + Integer existencias
    + String marca
    + String modelo
    + String codigo_sku
    + JSON especificaciones
    + String url_imagen_principal
    + Integer descuento_porcentaje
    + DateTime descuento_expira_el
    + Boolean esta_activo
    + Boolean es_destacado
    + Integer conteo_vistas
    + DateTime creado_el
    + DateTime actualizado_el
    + conteo_votos() : Integer
    + conteo_resenas() : Integer
    + calificacion_promedio() : Decimal
    + descuento_activo() : Boolean
    + precio_con_descuento() : Decimal
    + en_stock() : Boolean
  }

  class ImagenProducto {
    + UUID id
    + String url_imagen
    + String texto_alt
    + Integer orden
    + DateTime creado_el
  }
}

package "Modulo de Interacciones y Pedidos (interactions)" {
  class Voto {
    + UUID id
    + DateTime creado_el
  }

  class Resena {
    + UUID id
    + Integer calificacion
    + String comentario
    + Boolean esta_aprobada
    + DateTime creado_el
  }

  class Respuesta {
    + UUID id
    + String contenido
    + DateTime creado_el
  }

  class Favorito {
    + UUID id
    + DateTime creado_el
  }

  class Pedido {
    + UUID id
    + String estado
    + Decimal monto_total
    + String direccion_envio
    + String cedula
    + String telefono
    + String notas
    + DateTime entregado_el
    + String notas_repartidor
    + DateTime creado_el
    + DateTime actualizado_el
  }

  class DetallePedido {
    + UUID id
    + Integer cantidad
    + Decimal precio_unitario
    + DateTime creado_el
  }
}

' Relaciones entre clases
Perfil "1" *-- "0..*" Notificacion : recibe
Categoria "1" *-- "0..*" Producto : contiene
Producto "1" *-- "0..*" ImagenProducto : tiene

Perfil "1" -- "0..*" Voto : realiza
Producto "1" -- "0..*" Voto : recibe

Perfil "1" -- "0..*" Resena : escribe
Producto "1" -- "0..*" Resena : califica
Resena "1" *-- "0..*" Respuesta : tiene
Perfil "1" -- "0..*" Respuesta : responde

Perfil "1" -- "0..*" Favorito : agrega
Producto "1" -- "0..*" Favorito : es_marcado

Perfil "1" -- "0..*" Pedido : realiza
Perfil "0..1" -- "0..*" Pedido : despacha
Pedido "1" *-- "1..*" DetallePedido : contiene
Producto "1" -- "0..*" DetallePedido : es_vendido

@enduml
```

---

## 🏆 Diagrama de Clases Avanzado con Patrones de Diseño (PlantUML)

Este diagrama representa la propuesta de diseño de arquitectura de software para la evolución de **MIKITECH**, aplicando patrones de diseño del GOF (Gang of Four) para solucionar problemas de escalabilidad, acoplamiento y mantenimiento del sistema.

### Patrones Aplicados:
1. **Repository Pattern (Acceso a Datos):** Desacopla la lógica de negocio de la base de datos física en Supabase.
2. **Factory Pattern (Creación de Productos):** Encapsula y simplifica la creación de productos estándar y combos/kits de hardware.
3. **Observer Pattern (Notificaciones):** Automatiza las alertas y notificaciones a usuarios en múltiples canales (Email y Notificaciones Web) al actualizar pedidos.
4. **State Pattern (Gestión de Pedidos):** Controla de forma limpia las transiciones y estados del ciclo de entrega de los pedidos.
5. **Strategy Pattern (Métodos de Pago):** Facilita la adición e intercambio de pasarelas de pago independientes (Stripe, PSE local, Contraentrega).

```plantuml
@startuml
title Diagrama de Clases Avanzado con Patrones de Diseño - MIKITECH

skinparam classAttributeIconSize 0
left to right direction
skinparam packageStyle rectangle

' --- REPOSITORY PATTERN ---
package "Repository Pattern" {
  interface IProductRepository {
    + getById(id: UUID) : Producto
    + getAll() : List<Producto>
    + save(p: Producto)
    + delete(id: UUID)
  }
  class SupabaseProductRepository {
    - client: SupabaseClient
    + getById(id: UUID) : Producto
    + getAll() : List<Producto>
    + save(p: Producto)
    + delete(id: UUID)
  }
  IProductRepository <|.. SupabaseProductRepository
  note bottom of SupabaseProductRepository : **Repository Pattern**\nAbstrae el acceso a Supabase\ny aísla la lógica del backend.
}

' --- FACTORY PATTERN ---
package "Factory Pattern" {
  class ProductFactory {
    + {static} createProduct(tipo: String, datos: JSON) : Producto
  }
  class Producto {
    + UUID id
    + String nombre
    + Decimal precio
  }
  class KitHardware {
    + List<Producto> componentes
  }
  Producto <|-- KitHardware
  ProductFactory ..> Producto : crea >
  note top of ProductFactory : **Factory Pattern**\nFabrica encargada de crear productos\nsimples o combos/kits de hardware.
}

' --- OBSERVER PATTERN ---
package "Observer Pattern" {
  interface ISubject {
    + attach(o: IObserver)
    + detach(o: IObserver)
    + notifyObservers()
  }
  class OrderNotificationService {
    - observers: List<IObserver>
    - orderStatus: String
    + attach(o: IObserver)
    + detach(o: IObserver)
    + notifyObservers()
    + setStatus(status: String)
  }
  interface IObserver {
    + update(message: String)
  }
  class EmailNotifier {
    + update(message: String)
  }
  class InAppNotifier {
    + update(message: String)
  }
  
  ISubject <|.. OrderNotificationService
  IObserver <|.. EmailNotifier
  IObserver <|.. InAppNotifier
  OrderNotificationService o-- IObserver : notifica >
  note top of IObserver : **Observer Pattern**\nObservadores que reaccionan ante\ncambios de estado del pedido.
}

' --- STATE PATTERN ---
package "State Pattern" {
  class PedidoContext {
    - state: OrderState
    + setState(s: OrderState)
    + nextState()
    + cancel()
  }
  abstract class OrderState {
    + {abstract} handleNext(context: PedidoContext)
    + {abstract} handleCancel(context: PedidoContext)
    + {abstract} getStatus() : String
  }
  class PendingState {
    + handleNext(context: PedidoContext)
    + handleCancel(context: PedidoContext)
    + getStatus() : String
  }
  class ShippedState {
    + handleNext(context: PedidoContext)
    + handleCancel(context: PedidoContext)
    + getStatus() : String
  }
  class DeliveredState {
    + handleNext(context: PedidoContext)
    + handleCancel(context: PedidoContext)
    + getStatus() : String
  }
  
  PedidoContext *-- OrderState
  OrderState <|-- PendingState
  OrderState <|-- ShippedState
  OrderState <|-- DeliveredState
  note right of OrderState : **State Pattern**\nGestiona el ciclo de vida del pedido:\nPendiente -> Enviado -> Entregado.
}

' --- STRATEGY PATTERN ---
package "Strategy Pattern" {
  class CheckoutService {
    - paymentStrategy: IPaymentStrategy
    + setPaymentStrategy(s: IPaymentStrategy)
    + checkout(amount: Decimal)
  }
  interface IPaymentStrategy {
    + processPayment(amount: Decimal) : Boolean
  }
  class StripePaymentStrategy {
    - cardToken: String
    + processPayment(amount: Decimal) : Boolean
  }
  class PSEPaymentStrategy {
    - bankId: String
    + processPayment(amount: Decimal) : Boolean
  }
  class CashOnDeliveryStrategy {
    + processPayment(amount: Decimal) : Boolean
  }
  
  CheckoutService *-- IPaymentStrategy
  IPaymentStrategy <|.. StripePaymentStrategy
  IPaymentStrategy <|.. PSEPaymentStrategy
  IPaymentStrategy <|.. CashOnDeliveryStrategy
  note top of IPaymentStrategy : **Strategy Pattern**\nPermite intercambiar pasarelas\nde pago (Stripe, PSE, Contraentrega).
}

' Relaciones de orquestación
PedidoContext ..> ISubject : actualiza estado >
CheckoutService ..> PedidoContext : crea en éxito >

@enduml
```

---

## 📐 Diagrama de Clases Básico (Estructura Simplificada)

Este diagrama representa la estructura de clases fundamental de un sistema de e-commerce como MIKITECH, mostrando las entidades básicas de negocio (Usuario, Categoria, Producto, Pedido, DetallePedido y Pago) junto con sus multiplicidades y relaciones típicas.

```plantuml
@startuml
title Diagrama de Clases Basico - MIKITECH E-Commerce

left to right direction
skinparam packageStyle rectangle
skinparam classAttributeIconSize 0

class Usuario {
  + id: int
  + nombre: String
  + email: String
  + rol: String
}

class Categoria {
  + id: int
  + nombre: String
  + descripcion: String
}

class Producto {
  + id: int
  + nombre: String
  + precio: Decimal
  + stock: int
}

class Pedido {
  + id: int
  + fecha: DateTime
  + estado: String
  + total: Decimal
}

class DetallePedido {
  + id: int
  + cantidad: int
  + precio_unitario: Decimal
}

class Pago {
  + id: int
  + metodo: String
  + monto: Decimal
  + transaccion_id: String
  + fecha: DateTime
}

' Relaciones tipicas con multiplicidad
Usuario "1" -- "0..*" Pedido : realiza >
Pedido "1" *-- "1..*" DetallePedido : contiene >
Producto "1" -- "0..*" DetallePedido : se incluye en >
Categoria "1" -- "0..*" Producto : clasifica >
Pedido "1" -- "1" Pago : procesa >

@enduml
```

---

## 🔄 Diagrama de Procesos en Carriles (PlantUML Activity Diagram)

Este diagrama representa el ciclo de compra y checkout mapeado a un diagrama de actividades con carriles (*swimlanes*) en PlantUML, delimitando los roles del Cliente, el Sistema y el equipo de Logística.

```plantuml
@startuml
title Diagrama de Procesos (Checkout y Compra) - MIKITECH

|Cliente|
start
:Explorar catalogo;
:Agregar al carrito;

|Sistema|
:Validar stock de productos;
if (Existe stock?) then (Si)
  |Cliente|
  :Proceder al Checkout;
  :Realizar Pago;
  
  |Sistema|
  :Procesar Pago Electronico;
  if (Pago exitoso?) then (Si)
    :Registrar Orden & Descontar stock;
    
    |Logistica|
    :Empacar hardware;
    :Despachar paquete;
    :Registrar guia de envio;
    
    |Cliente|
    :Esperar entrega;
    :Recibir pedido y verificar hardware;
    stop
  else (No)
    |Sistema|
    :Notificar fallo en el pago;
    |Cliente|
    :Reintentar con otro metodo de pago;
    stop
  endif
else (No)
  |Sistema|
  :Notificar falta de stock;
  |Cliente|
  :Ajustar cantidad en el carrito;
  stop
endif

@enduml
```

---

## 🏗️ Diagrama de Vista de Implementación y Despliegue (PlantUML Premium Styling)

Este diagrama representa la **Vista de Implementación (Componentes y Despliegue)** completa del sistema MIKITECH, detallando los archivos físicos, el entorno virtual, las herramientas de pruebas y la infraestructura en la nube, con una paleta de colores personalizada en modo oscuro.

```plantuml
@startuml
title Vista de Implementacion y Despliegue Completo - MIKITECH

left to right direction
skinparam packageStyle rectangle
skinparam componentStyle uml2

' --- PREMIUM COLOR THEME (DARK MODE) ---
skinparam BackgroundColor #0f172a
skinparam TitleFontColor #3b82f6
skinparam TitleFontSize 20
skinparam TitleFontName "Outfit"

skinparam node {
  BackgroundColor #1e293b
  BorderColor #3b82f6
  FontColor #f8fafc
  FontName "Outfit"
}

skinparam package {
  BackgroundColor #1e1b4b
  BorderColor #818cf8
  FontColor #e0e7ff
  FontName "Outfit"
}

skinparam component {
  BackgroundColor #312e81
  BorderColor #a5b4fc
  FontColor #f8fafc
  FontName "Outfit"
}

skinparam database {
  BackgroundColor #064e3b
  BorderColor #34d399
  FontColor #f8fafc
  FontName "Outfit"
}

skinparam artifact {
  BackgroundColor #0f172a
  BorderColor #64748b
  FontColor #cbd5e1
  FontName "Outfit"
}

skinparam arrow {
  Color #3b82f6
  FontColor #94a3b8
  FontName "Outfit"
}

' --- DIAGRAM ELEMENTS ---

node "Computador Cliente" as ClientNode {
  package "Navegador Web (Frontend)" {
    component [interfaz-cliente/\n(vistas de usuario HTML/CSS/JS)] as ClientHTML
    component [consola_pruebas.html\n(Panel Interactivo de QA)] as QAPanel
    component [diagrama_procesos.html\n(Visualizador de Swimlanes)] as SwimlaneHTML
  }
}

node "Servidor Local de Desarrollo (Waitress WSGI / Django)" as ServerNode {
  
  package "Entorno Virtual (.venv/)" {
    component [Interprete Python & Django Core] as PythonEnv
  }

  package "servidor-y-logica/ (Codigo Fuente Backend)" as BackendPkg {
    
    package "mickytech (Configuracion Central)" {
      artifact "settings.py" as SetFile
      artifact "urls.py" as UrlsFile
      artifact "wsgi.py" as WsgiFile
    }

    package "users (Gestion de Usuarios)" {
      artifact "users/models.py" as UserModel
      artifact "users/views.py" as UserView
      artifact "users/photo_manager.py" as UserPhoto
    }

    package "products (Catalogo de Tienda)" {
      artifact "products/models.py" as ProdModel
      artifact "products/views.py" as ProdView
    }

    package "interactions (Ventas y Logistica)" {
      artifact "interactions/models.py" as IntModel
      artifact "interactions/views.py" as IntView
    }
  }
}

node "Nube de Supabase (Backend as a Service)" as CloudNode {
  database "PostgreSQL Database\n(Tablas: profiles, products, orders...)" as SupaDB
  component [Supabase Auth API\n(Gestion de Sesiones & JWT)] as SupaAuth
  component [Supabase Storage Bucket\n(avatars/ & products/)] as SupaStorage
}

node "Entorno de Pruebas y QA" as QANode {
  component [Motor de k6\n(load_test_basic.js, k6_mitigation.js)] as k6Engine
  component [Locust Swarm\n(locustfile.py)] as LocustEngine
}

' Relaciones de Despliegue y Dependencias
ClientHTML --> WsgiFile : Peticiones HTTP/HTTPS
QAPanel --> PythonEnv : Ejecuta comandos unittest
k6Engine --> WsgiFile : Simula trafico concurrente
LocustEngine --> WsgiFile : Simula swarms de usuarios

PythonEnv ..> BackendPkg : Ejecuta logica de

UrlsFile ..> UserView : Enruta a
UrlsFile ..> ProdView : Enruta a
UrlsFile ..> IntView : Enruta a

UserView ..> UserModel : Lee/Escribe
ProdView ..> ProdModel : Lee/Escribe
IntView ..> IntModel : Lee/Escribe

UserModel --> SupaDB : Mapea en tabla 'profiles'
ProdModel --> SupaDB : Mapea en tabla 'products'
IntModel --> SupaDB : Mapea en tablas 'orders' y 'reviews'

UserPhoto --> SupaStorage : Sube fotos de perfil
UserView --> SupaAuth : Valida tokens de acceso

@enduml
```







