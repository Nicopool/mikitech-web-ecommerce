# Proyecto: Mickytech - E-commerce de Tecnología de Alto Rendimiento

Este documento es la **Especificación Maestra** de la plataforma MIKITECH. Sirve como referencia técnica definitiva para el desarrollo, diseño y reglas de negocio del sistema.

---

## 🛠 Stack de Tecnología y APIs

### 1. Core Engine
- **Lenguaje**: Python 3.11.9
- **Framework Web**: Django 4.x (Arquitectura: `core`, `products`, `users`, `interactions`).
- **Base de Datos**: PostgreSQL alojada en **Supabase** (Tablas con `managed=False` en Django).
- **Autenticación**: Supabase Auth REST API integrada con sesiones de Django.

### 2. Ecosistema de Terceros (APIs)
- **Supabase JS/REST**: Gestión de identidades, perfiles y almacenamiento de avatares.
- **Leaflet.js + Nominatim (OSM)**: 
    - Geocodificación inversa para autocompletado de direcciones en Checkout.
    - Mapas interactivos con marcadores arrastrables para precisión de entrega.
- **Chart.js**: Visualización de métricas de consumo en tiempo real para el Panel de Usuario y Reportes Administrativos.
- **SweetAlert2**: Estandarización de toda la UX de alertas, confirmaciones (logout, eliminación) y notificaciones (*Toasts*).
- **Bootstrap 5**: Uso exclusivo de utilidades de diseño (*grid*, *spacing*) para complementar el CSS nativo.

---

## 📋 Funcionalidades Maestras e Inteligencia de Negocio

### 1. Motor de E-commerce (Logística de Venta)
- **Precisión Financiera**: Uso estricto de la clase `Decimal` de Python para todos los cálculos. Prohibido el uso de `float` en precios.
- **Matriz de Impuestos**: IVA del 19% incluido en todos los precios marcados. Cálculo interno: `iva = total - (total / 1.19)`.
- **Gestión de Stock**: El sistema descuenta existencias automáticamente al confirmar el pago en el Checkout.
- **Carrito AJAX**: Persistencia en sesión con *Mini-Cart Drawer* lateral y sincronización en tiempo real vía API interna.

### 2. Panel de Usuario (Dashboard Pro)
- **Interfaz Sidebar**: Navegación lateral persistente con estados activos.
- **Secciones Específicas**:
    - **Mi Perfil**: Gestión de avatar con previsualización dinámica.
    - **Mis Pedidos**: Seguimiento de estados (`pending`, `processing`, `shipped`, `delivered`).
    - **Reportes Interactivos**: Gráficos de líneas (`Chart.js`) que muestran el historial de gastos del usuario.
    - **Favoritos**: Sistema de persistencia para componentes de interés.

### 3. Logística y Administración (Accesos Secretos)
- **Portal de Repartidores (MOTO-2026)**:
    - **Pasarela**: `/repartidor/pasarela/`. Código secreto: **`MOTO-2026`**.
    - **Validación de Entrega**: El repartidor debe ingresar la **Cédula del Cliente** al momento del despacho; el sistema valida que coincida con la registrada en el pedido antes de marcar como `delivered`.
- **Panel Administrativo Maestro (SENA-2026)**:
    - **Pasarela de Seguridad**: `/admin-panel/pasarela/`. Código secreto: **`SENA-2026`**.
    - **Integración Social**: Moderación de reseñas con sistema de aprobación y gestión de votos técnicos.

---

## 🎨 Especificaciones de Diseño (Identidad Visual)

### 1. Sistema de Diseño (Design Tokens)
- **Estética**: High-Tech / Premium (Inspirado en ecosistemas de alto rendimiento).
- **Paleta de Colores (Cold Tech)**:
    - **Primario**: Azul Eléctrico (`#1D4ED8`)
    - **Secundario**: Navy Dark (`#0F172A`)
    - **Acento**: Slate Grey (`#64748B`)
    - **Fondo**: Off-White / Blueish Grey (`#F8FAFC`)
- **Tipografía**:
    - **Titulares**: *Oswald* (Google Fonts) - Peso 700 para fuerza visual.
    - **Cuerpo**: *Jost* (Google Fonts) - Peso 400/500/600 para legibilidad técnica.
    - **UI / Labels**: *Inter* - Alta densidad de información.

### 2. Reglas de Layout
- **Unidades**: Uso estricto de `rem` (font-size raíz de `10px`). Un `1rem` equivale siempre a `10px`.
- **Estructura**: 100% responsiva mediante CSS Grid y Flexbox. Prohibido el uso de `tables` para maquetación.

---

## 💻 Reglas de Código y Seguridad Inviables
- **DOM**: Prohibido el uso de `innerHTML`. Únicamente `createElement`, `appendChild` y `textContent`.
- **Sesiones**: Cierres de sesión protegidos con `session.flush()` y confirmación previa obligatoria vía SweetAlert2.
- **Seguridad**: Prevención de comportamiento por defecto (`preventDefault()`) en todos los formularios y clics críticos.
- **Idioma**: La interfaz completa, logs de error, validaciones y documentación deben estar 100% en **Español (Colombia)**.

---

## 📂 Estructura de Arquitectura
- `/mickytech`: Configuración del servidor Django.
- `/core`: Apps de tienda, carrito, checkout y gateways de seguridad.
- `/products`: Modelos de hardware y lógica de precios dinámicos.
- `/users`: Perfiles, autenticación Supabase y dashboards personales.
- `/interactions`: Sistema de reseñas, votos y notificaciones.
- `/static`: CSS consolidado, JS modular y activos de marca.
- `/templates`: Estructura HTML segmentada por aplicación y componentes.