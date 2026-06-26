markdown

# PROMPT PARA ANTIGRAVITY - MEJORA DE UX MÓVIL Y DISEÑO INTUITIVO PARA ECOMMERCE

## CONTEXTO ACTUAL

Mi aplicación es un **ecommerce** que actualmente tiene problemas de usabilidad en dispositivos móviles:

### Problemas identificados

1. **Letra demasiado pequeña** en móviles (texto ilegible sin hacer zoom)
2. **Diseño no responsive** (elementos se desbordan o se superponen)
3. **Navegación confusa** (usuarios no encuentran lo que buscan)
4. **Botones muy pequeños** (difíciles de tocar en pantallas táctiles)
5. **Checkout complejo** (abandono de carrito alto en móviles)
6. **Tiempos de carga lentos** en redes móviles
7. **Falta de jerarquía visual** (todo parece igual de importante)
8. **Formularios difíciles** de completar en móvil

### Datos actuales

- **Tasa de conversión móvil:** [X]% (vs [Y]% en desktop)
- **Tasa de abandono de carrito:** [X]%
- **Usuarios móviles:** [X]% del total
- **Tiempo promedio de carga:** [X] segundos en móvil

### Tecnologías

- Frontend: [React/Vue/Angular + CSS framework]
- UI Library: [Material-UI/Tailwind/Bootstrap/etc.]
- Estado: [Redux/Zustand/Context/etc.]
- Responsive actual: [Media queries / CSS Grid / Flexbox]

## OBJETIVO PRINCIPAL

Necesito **rediseñar la experiencia móvil** de mi ecommerce para que sea:

1. **Legible** (texto claro y de tamaño adecuado)
2. **Intuitiva** (navegación obvia y fluida)
3. **Rápida** (optimizada para redes móviles)
4. **Accesible** (para todos los usuarios)
5. **Conversora** (que aumente las ventas)

## REQUERIMIENTOS ESPECÍFICOS

### 1. TIPOGRAFÍA Y LEGIBILIDAD

#### Tamaños de fuente recomendados

- **Títulos principales (h1):** 24-28px en móvil (vs 32-36px en desktop)
- **Subtítulos (h2):** 20-22px en móvil
- **Texto de cuerpo:** 16-18px en móvil (mínimo 16px para legibilidad)
- **Textos pequeños (etiquetas, precios):** 14-15px
- **Botones:** 16-18px (texto visible)

#### Consejos de implementación

```css
/* Ejemplo de tipografía responsive */
html {
  font-size: 16px; /* Base */
}

@media (max-width: 768px) {
  html {
    font-size: 14px; /* Reducir base en móvil */
  }
  
  h1 { font-size: 1.75rem; } /* 28px */
  h2 { font-size: 1.375rem; } /* 22px */
  p { font-size: 1rem; } /* 16px */
  small { font-size: 0.875rem; } /* 14px */
}
Requerimientos:

Usar unidades relativas (rem, em) en lugar de px

Contraste mínimo 4.5:1 para texto normal

Contraste mínimo 3:1 para textos grandes

Espaciado entre líneas (line-height): 1.5-1.6 para texto

Ancho de línea máximo: 60-75 caracteres por línea

2. DISEÑO RESPONSIVE Y LAYOUT
Estructura de grilla:
text
[Móvil - 1 columna]  → [Tablet - 2 columnas] → [Desktop - 3-4 columnas]
Puntos de quiebre (breakpoints):
Móvil pequeño: < 375px

Móvil: 376px - 768px

Tablet: 769px - 1024px

Desktop: > 1024px

Componentes clave a rediseñar:
Header/Navbar:

Logo a la izquierda

Buscador expandible (icono de lupa)

Carrito con contador visible

Menú hamburguesa para navegación

Lista de productos:

Cards con imagen destacada

Precio grande y visible

Botón "Agregar al carrito" prominente

Vista en grid (2 columnas en móvil)

Detalle de producto:

Carrusel de imágenes táctil

Descripción colapsable

Selector de cantidad con +/- grande

Botón "Comprar ahora" fijo en la parte inferior

Carrito de compras:

Resumen siempre visible (sticky)

Botones grandes para cantidad

Opción "Seguir comprando" fácil

Total claro y grande

Checkout:

Progreso de pasos visible

Formularios optimizados (autocompletar, validación en tiempo real)

Botón de pago prominente

Opciones de pago con íconos grandes

3. NAVEGACIÓN INTUITIVA
Arquitectura de navegación:
text
[Home]
  ├── [Categorías]
  │   ├── [Subcategoría 1]
  │   ├── [Subcategoría 2]
  │   └── [Subcategoría 3]
  ├── [Búsqueda]
  ├── [Ofertas]
  ├── [Mi Cuenta]
  └── [Carrito]
Elementos de navegación:
Breadcrumbs (migas de pan) en móvil (simplificados)

Filtros en slide lateral o acordeón

Ordenamiento con selector desplegable

Botón "Volver arriba" (flotante)

Navegación inferior (bottom navigation) con 4-5 íconos

Bottom Navigation (Mobile First):
text
[🏠 Home] [🔍 Buscar] [❤️ Favoritos] [🛒 Carrito] [👤 Cuenta]
4. INTERACCIÓN Y FEEDBACK
Micro-interacciones:
Botones: Efecto de presión (scale-down al tocar)

Carga: Skeletons o spinners sutiles

Éxito: Animación de "añadido al carrito" (checkmark)

Error: Mensajes claros y con color distintivo

Desplazamiento: Scroll suave y snap scrolling para secciones

Feedback visual:
css
/* Ejemplo de feedback en botones */
.button:active {
  transform: scale(0.95);
  transition: transform 0.1s;
}

.button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
5. OPTIMIZACIÓN DE RENDIMIENTO MÓVIL
Técnicas recomendadas:
Lazy loading de imágenes (cargar solo visibles)

Imágenes WebP con fallback a JPEG/PNG

Caching de recursos estáticos

Code splitting (cargar solo lo necesario)

Precarga de recursos críticos

Minimizar CSS/JS

Usar CDN para assets

Reducir número de peticiones HTTP

Métricas objetivo:
First Contentful Paint (FCP): < 1.8s

Largest Contentful Paint (LCP): < 2.5s

Time to Interactive (TTI): < 3.8s

Total Blocking Time (TBT): < 200ms

Cumulative Layout Shift (CLS): < 0.1

6. ACCESIBILIDAD MÓVIL
Checklist de accesibilidad:
Contraste de color suficiente (4.5:1)

Tamaño de toque mínimo: 44x44px (Apple HIG) o 48x48px (Material Design)

Espaciado entre elementos táctiles: mínimo 8px

Texto redimensionable (sin zoom bloqueado)

Etiquetas ARIA en elementos interactivos

Navegación por teclado (para usuarios con discapacidad)

Descripciones alternativas en imágenes

Formularios con labels asociados

7. CHECKOUT Y CONVERSIÓN
Optimizaciones para checkout móvil:
Checkout en 1-2 pasos (máximo 3)

Autocompletar direcciones (Google Maps API)

Guardar datos de pago seguros

Pago con huella digital (Face ID / Touch ID)

Botón de pago prominente y en color contrastante

Indicador de progreso (paso 1 de 3)

Resumen del pedido siempre visible

Opciones de pago con íconos grandes

Reducción de fricción:
Eliminar campos innecesarios

Usar inputs con tipo específico (type="email", type="tel")

Validación en tiempo real (no al enviar)

Recordar información del usuario (si está autenticado)

Ofrecer "Pago como invitado"

8. USABILIDAD Y PRUEBAS
Pruebas sugeridas:
Test A/B de diferentes layouts

Heatmaps para ver dónde hacen clic

Grabaciones de sesiones para ver problemas reales

Pruebas de usuario con 5-10 personas

Análisis de funnel (dónde abandonan)

Métricas a mejorar:
Tasa de conversión móvil (actual: X%, objetivo: +20%)

Tasa de abandono de carrito (actual: X%, objetivo: -15%)

Tiempo en página (actual: X min, objetivo: +30%)

Tasa de rebote (actual: X%, objetivo: -10%)

PREGUNTAS ESPECÍFICAS QUE QUIERO RESPONDIDAS
¿Cuál es el tamaño de fuente óptimo para mi tipo de ecommerce?

¿Debo usar un diseño de 1 o 2 columnas en móvil para productos?

¿Qué elementos deberían estar fijos (sticky) en móvil?

¿Cómo simplificar el checkout sin perder información necesaria?

¿Qué micro-interacciones mejoran más la experiencia de compra?

¿Cómo manejar la navegación por categorías en móvil?

¿Qué hacer cuando el usuario tiene mala conexión?

¿Cómo implementar un bottom navigation efectivo?

¿Cuál es la mejor posición para el botón "Agregar al carrito"?

¿Cómo reducir el abandono de carrito en móvil?

ENTREGABLES ESPERADOS
Quiero que me entregues:

1. Guía de Estilos Móvil
Paleta de colores optimizada para móvil

Tamaños de fuente (h1, h2, h3, body, small)

Espaciados y márgenes (padding, margin)

Tamaños de botones y elementos táctiles

Estilos para estados (hover, active, disabled, focus)

2. Wireframes / Mockups (en texto o ASCII)
Layout de Home en móvil

Layout de lista de productos

Layout de detalle de producto

Layout de carrito

Layout de checkout (paso a paso)

3. Código de Implementación
CSS/SCSS para tipografía responsive

Componentes responsivos (cards, botones, formularios)

Sistema de grilla (grid/flexbox)

Animaciones y transiciones

Componente de bottom navigation

4. Estrategia de Testing
Cómo probar en diferentes dispositivos

Herramientas recomendadas (BrowserStack, LambdaTest)

Checklist de QA móvil

5. Plan de Implementación
Orden de implementación (qué cambiar primero)

Estimación de tiempo

Recursos necesarios

Riesgos y mitigaciones

EJEMPLOS DE MEJORES PRÁCTICAS
Ejemplo 1: Card de Producto (Móvil)
html
<!-- Mobile Product Card -->
<div class="product-card">
  <div class="product-image">
    <img src="producto.jpg" alt="Nombre producto" loading="lazy">
    <span class="product-badge">Oferta</span>
  </div>
  <div class="product-info">
    <h3 class="product-name">Nombre del Producto</h3>
    <div class="product-rating">⭐⭐⭐⭐ (120)</div>
    <div class="product-price">
      <span class="price-current">$99.99</span>
      <span class="price-original">$129.99</span>
    </div>
    <button class="btn-add-to-cart">Agregar al Carrito</button>
  </div>
</div>
Ejemplo 2: Bottom Navigation
html
<!-- Bottom Navigation -->
<nav class="bottom-nav">
  <a href="/" class="nav-item active">
    <svg><!-- Home icon --></svg>
    <span>Inicio</span>
  </a>
  <a href="/search" class="nav-item">
    <svg><!-- Search icon --></svg>
    <span>Buscar</span>
  </a>
  <a href="/cart" class="nav-item cart-nav">
    <svg><!-- Cart icon --></svg>
    <span>Carrito</span>
    <span class="cart-badge">3</span>
  </a>
  <a href="/account" class="nav-item">
    <svg><!-- Profile icon --></svg>
    <span>Cuenta</span>
  </a>
</nav>
Ejemplo 3: Formulario de Checkout Optimizado
html
<!-- Mobile Checkout -->
<form class="checkout-form">
  <div class="form-step active">
    <h2>Datos de Envío</h2>
    <input type="text" placeholder="Nombre completo" required>
    <input type="email" placeholder="Correo electrónico" required>
    <input type="tel" placeholder="Teléfono" required>
    <button type="button" class="btn-next">Siguiente →</button>
  </div>
  
  <div class="form-step">
    <h2>Método de Pago</h2>
    <!-- Opciones de pago -->
    <button type="submit" class="btn-pay">Pagar $99.99</button>
  </div>
</form>
NOTAS ADICIONALES
Presupuesto: [bajo/medio/alto]

Tiempo disponible: [X] semanas para implementar

Equipo: [X] diseñadores, [X] desarrolladores frontend

Restricciones: [mantener compatibilidad con navegadores antiguos, etc.]

Inspiración: [Apps/ecommerces que te gustan: Amazon, MercadoLibre, etc.]

RECURSOS ÚTILES
Herramientas recomendadas:
Prototipado: Figma, Adobe XD

Testing móvil: BrowserStack, LambdaTest, Chrome DevTools

Analytics: Hotjar, CrazyEgg (heatmaps), Google Analytics

Performance: Lighthouse, PageSpeed Insights, WebPageTest

Referencias de diseño:
Material Design (Google)

Human Interface Guidelines (Apple)

NNG Group (estudios de usabilidad)

Baymard Institute (best practices ecommerce)
