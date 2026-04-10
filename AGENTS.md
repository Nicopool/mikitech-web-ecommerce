Proyecto: Mickytech - E-commerce de Tecnología de Alto Rendimiento
Rol del agente: Desarrollador web experto Full Stack con 12 años de experiencia.
Objetivo: Crear una plataforma de comercio electrónico profesional para la venta de componentes (CPUs, GPUs, periféricos), integrando funciones de comunidad como perfiles públicos, sistema de votos y reseñas detalladas.

🛠 Stack de Tecnología
Lenguaje: Python

Framework Web: Django (Estructura de apps separadas: core, products, users, interactions).

Base de Datos & Auth: Supabase (PostgreSQL).

Frontend: HTML5 semántico y CSS3 nativo (Prohibido TailwindCSS o Bootstrap).

Interactividad: JavaScript Vanilla (Prohibido el uso de innerHTML).

📋 Funcionalidades de la Aplicación
1. Parte Pública (Catálogo y Comunidad)

Listado de Productos: Vista principal con paginación y diseño de grid moderno.

Buscador & Filtros: Filtrado por nombre, descripción, categorías y rango de precio.

Detalle de Producto: * Especificaciones técnicas, galería de imágenes, precio y stock.

Sistema de Votos: Los usuarios pueden dar "Like" a los componentes (máximo uno por usuario).

Sección de Reseñas: Comentarios detallados. Solo usuarios identificados pueden comentar. Posibilidad de responder a comentarios.

Perfiles Públicos: Capacidad de ver los perfiles de otros usuarios, sus componentes favoritos y sus reseñas.

2. Gestión de Usuarios (Área Privada)

Autenticación: Login y Registro gestionado con Supabase Auth.

Perfil de Usuario: * Modificar datos personales (Nombre, Email, Contraseña).

Gestión de Avatar (Subir/Cambiar imagen).

Favoritos: Sección con icono de corazón para guardar componentes de interés.

Historial de Pedidos: Ver compras realizadas y su estado.

3. Panel Administrativo (Seguridad Reforzada)

Gateway de Seguridad: Página intermedia obligatoria que solicita el código: SENA-2026. Solo tras validarlo se permite el acceso al login de administrador.

Gestión (CRUD): Control total de productos, categorías, stock, usuarios y moderación de interacciones (votos/comentarios).

🗄️ Base de Datos (Supabase)
Nombre de la DB: MYKITECHWEB
dEADPOOL123**##
https://abhnnxuqmbjkqiakebmv.supabase.co

Seeding Requerido (vía MCP):

10 Usuarios (mezcla de roles admin y cliente).

107 Productos tecnológicos distribuidos en 10 categorías.

25 Comentarios/Reseñas de prueba.

5 Votos por producto y 5 favoritos por cada usuario.

🎨 Preferencias de Diseño y Estilos
Estética: Paleta de azules y tonos fríos (Estilo Tech/Profesional).

Unidades: Uso estricto de rem con un font-size base de 10px en el elemento raíz.

Layout: Uso de Flexbox y CSS Grid para una estructura 100% responsive.

Archivo Único: Todo el CSS debe estar consolidado en un solo archivo para evitar fragmentación.

Idioma: Todos los textos, mensajes de error y etiquetas deben estar en español.

💻 Reglas de Código y Buenas Prácticas
Manipulación del DOM: Queda estrictamente prohibido innerHTML. Usar appendChild o createElement.

Feedback Visual: No usar alert(), confirm() ni prompt(). Todo mensaje debe mostrarse mediante elementos del DOM (Toasts o Modales).

Seguridad: Prevenir el comportamiento por defecto (preventDefault()) en formularios y clics críticos.

Estructura Django: Mantener una arquitectura limpia con apps independientes.

📂 Estructura de Archivos
/design: Referencias visuales y HTML base.

/mickytech: Carpeta principal del proyecto Django.

AGENTS.md: Documento con las especificaciones del proyecto.