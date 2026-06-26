🔍 ANÁLISIS DE LA VISTA ACTUAL
Problemas identificados:
❌ Falta de jerarquía visual - Todo parece igual, no hay distinción clara entre elementos

❌ Texto pequeño en móvil - Los precios y descripciones son difíciles de leer

❌ Espaciado insuficiente - Los productos están muy juntos, se siente apretado

❌ Botones pequeños - "DETALLES" y "AGREGAR" son difíciles de tocar en móvil

❌ Sin filtros visibles - No hay forma de ordenar o filtrar productos

❌ Categorías poco claras - "Tarjetas Gráficas" se repite sin diferenciación

❌ Falta de imágenes - Solo texto, ningún producto tiene foto

❌ Sin precio original tachado - No se ve el descuento claramente en todos

❌ Navegación superior confusa - "Inicio Tienda Contacto" es muy básico

❌ Sin carrito visible - No se ve el contador del carrito

🎨 RECOMENDACIONES DE MEJORA

1. JERARQUÍA VISUAL Y TIPOGRAFÍA
Tamaños de fuente recomendados:
css
/*Mobile First - MIKI TECH */
:root {
  --font-xs: 12px;    /* Etiquetas pequeñas */
  --font-sm: 14px;    /* Detalles, fechas */
  --font-base: 16px;  /* Texto normal (mínimo para móvil) */
  --font-lg: 20px;    /* Subtítulos */
  --font-xl: 24px;    /* Precios importantes */
  --font-2xl: 28px;   /* Títulos de sección */
  --font-3xl: 32px;   /* Título principal*/
}

/*EJEMPLO DE MEJORA */
.product-name {
  font-size: var(--font-base); /* 16px - legible*/
  font-weight: 600;
  margin-bottom: 4px;
}

.product-price {
  font-size: var(--font-xl); /*24px - visible*/
  font-weight: 700;
  color: #2D3748;
}

.product-price-old {
  font-size: var(--font-sm); /*14px*/
  color: #A0AEC0;
  text-decoration: line-through;
  margin-left: 8px;
}
Estructura jerárquica sugerida:
text
[Logo] MIKI TECH (más grande y visible)
  ↓
[Barra de búsqueda] (con lupa, expansible)
  ↓
[Categorías] (scroll horizontal con chips)
  ↓
[Título de sección] "Tarjetas Gráficas" (tamaño grande)
  ↓
[Grid de productos] (2 columnas en móvil)
  ↓
[Card de producto] (imagen + nombre + precio + botón)
2. DISEÑO DE CARDS DE PRODUCTO (MOBILE-FIRST)
Versión actual (mejorable):
text
┌─────────────────┐
│ STOCK DISPONIBLE │ (muy pequeño)
│ Curiosity3       │
│ $3.000.000       │
│ $2.700.000 OFERTA│
└─────────────────┘
Versión mejorada:
html
<!-- Card de Producto Rediseñada -->
<div class="product-card">
  <!-- Imagen (placeholder por ahora) -->
  <div class="product-image">
    <img src="producto.jpg" alt="Curiosity3" loading="lazy">
    <span class="badge-offer">-10%</span>
    <span class="badge-stock">✅ En Stock</span>
  </div>
  
  <!-- Info del producto -->
  <div class="product-info">
    <h3 class="product-name">Curiosity3</h3>
    <div class="product-rating">
      ⭐⭐⭐⭐☆ (124 reseñas)
    </div>
    <div class="product-price">
      <span class="price-current">$2.700.000</span>
      <span class="price-old">$3.000.000</span>
      <span class="price-discount">-10%</span>
    </div>
  </div>
  
  <!-- Botones de acción -->
  <div class="product-actions">
    <button class="btn-details">Detalles</button>
    <button class="btn-add">🛒 Agregar</button>
  </div>
</div>
CSS para la card:
css
.product-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s;
  margin-bottom: 16px;
}

.product-card:active {
  transform: scale(0.98); /*Feedback táctil*/
}

.product-image {
  position: relative;
  background: #F7FAFC;
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.badge-offer {
  position: absolute;
  top: 8px;
  left: 8px;
  background: #E53E3E;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 700;
}

.badge-stock {
  position: absolute;
  top: 8px;
  right: 8px;
  background: #48BB78;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 11px;
}

.product-info {
  padding: 12px;
}

.product-name {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #2D3748;
}

.product-rating {
  font-size: 13px;
  color: #718096;
  margin-bottom: 6px;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}

.price-current {
  font-size: 22px;
  font-weight: 700;
  color: #2D3748;
}

.price-old {
  font-size: 14px;
  color: #A0AEC0;
  text-decoration: line-through;
}

.price-discount {
  background: #FED7D7;
  color: #C53030;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
}

.product-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  padding: 0 12px 12px 12px;
}

.btn-details {
  padding: 10px;
  background: #EDF2F7;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #4A5568;
  cursor: pointer;
}

.btn-add {
  padding: 10px;
  background: #3182CE;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
}

.btn-add:active {
  transform: scale(0.95);
}
3. ESTRUCTURA DE PÁGINA (HOME EN MÓVIL)
Layout sugerido:
text
┌──────────────────────────────┐
│ 🛒 MIKI TECH    🔍  🛍️  👤 │ ← Header con carrito visible
├──────────────────────────────┤
│ [Buscar hardware...]         │ ← Barra de búsqueda
├──────────────────────────────┤
│ [📱 Todas] [🎮 Gamer] [💼 Pro]│ ← Filtros rápidos (chips)
├──────────────────────────────┤
│                              │
│ Tarjetas Gráficas           │ ← Título de sección (más grande)
│                              │
│ ┌─────┐  ┌─────┐          │
│ │ Img  │  │ Img  │          │ ← Grid 2 columnas
│ │Nombre │  │Nombre │          │
│ │$2.7M  │  │$5.2M  │          │
│ │[➕]   │  │[➕]   │          │
│ └─────┘  └─────┘          │
│                              │
│ ┌─────┐  ┌─────┐          │
│ │ Img  │  │ Img  │          │
│ │Nombre │  │Nombre │          │
│ │$2.8M  │  │$5.4M  │          │
│ │[➕]   │  │[➕]   │          │
│ └─────┘  └─────┘          │
│                              │
├──────────────────────────────┤
│ 🏠  🔍  ❤️  🛒  👤        │ ← Bottom Navigation
└──────────────────────────────┘
4. NAVEGACIÓN Y FILTROS
Filtros mejorados (para móvil):
html
<!-- Filtros en chips (scroll horizontal) -->
<div class="filter-chips">
  <button class="chip active">Todos</button>
  <button class="chip">En Stock</button>
  <button class="chip">Ofertas</button>
  <button class="chip">NVIDIA</button>
  <button class="chip">AMD</button>
  <button class="chip">Menos de $3M</button>
</div>

<!-- Ordenamiento -->
<select class="sort-select">
  <option>Relevancia</option>
  <option>Precio: menor a mayor</option>
  <option>Precio: mayor a menor</option>
  <option>Más vendidos</option>
</select>
CSS para chips:
css
.filter-chips {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 12px 0;
  scrollbar-width: none; /* Ocultar scrollbar en Firefox */
  -ms-overflow-style: none; /* IE */
}

.filter-chips::-webkit-scrollbar {
  display: none; /*Ocultar scrollbar en Chrome/Safari*/
}

.chip {
  padding: 8px 16px;
  background: #EDF2F7;
  border: none;
  border-radius: 20px;
  font-size: 14px;
  white-space: nowrap;
  cursor: pointer;
}

.chip.active {
  background: #3182CE;
  color: white;
}
5. HEADER MEJORADO
Versión mejorada:
html
<header class="mobile-header">
  <div class="header-top">
    <div class="logo">
      <span class="logo-icon">🛒</span>
      <span class="logo-text">MIKI TECH</span>
    </div>

    <div class="header-actions">
      <button class="search-toggle" aria-label="Buscar">
        🔍
      </button>
      <button class="cart-toggle" aria-label="Carrito">
        🛍️
        <span class="cart-badge">3</span> <!-- Contador -->
      </button>
      <button class="menu-toggle" aria-label="Menú">
        ☰
      </button>
    </div>
  </div>
  
  <!-- Barra de búsqueda (expandible) -->
  <div class="search-bar">
    <input type="text" placeholder="Buscar hardware...">
    <button>🔍</button>
  </div>
</header>
CSS para el header:
css
.mobile-header {
  background: white;
  padding: 12px 16px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-text {
  font-size: 20px;
  font-weight: 700;
  color: #2D3748;
}

.header-actions {
  display: flex;
  gap: 16px;
  align-items: center;
}

.header-actions button {
  background: none;
  border: none;
  font-size: 22px;
  cursor: pointer;
  position: relative;
  padding: 4px;
}

.cart-badge {
  position: absolute;
  top: -4px;
  right: -6px;
  background: #E53E3E;
  color: white;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 12px;
  min-width: 18px;
  text-align: center;
}

.search-bar {
  margin-top: 10px;
  display: flex;
  gap: 8px;
}

.search-bar input {
  flex: 1;
  padding: 10px 14px;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 16px;
}

.search-bar input:focus {
  outline: none;
  border-color: #3182CE;
}

.search-bar button {
  padding: 10px 16px;
  background: #3182CE;
  border: none;
  border-radius: 8px;
  color: white;
  font-size: 18px;
}
6. BOTTOM NAVIGATION (Navegación inferior)
html
<nav class="bottom-nav">
  <a href="/" class="nav-item active">
    <span class="nav-icon">🏠</span>
    <span class="nav-label">Inicio</span>
  </a>
  <a href="/search" class="nav-item">
    <span class="nav-icon">🔍</span>
    <span class="nav-label">Buscar</span>
  </a>
  <a href="/favorites" class="nav-item">
    <span class="nav-icon">❤️</span>
    <span class="nav-label">Favoritos</span>
  </a>
  <a href="/cart" class="nav-item cart-nav">
    <span class="nav-icon">🛒</span>
    <span class="nav-label">Carrito</span>
    <span class="nav-badge">3</span>
  </a>
  <a href="/account" class="nav-item">
    <span class="nav-icon">👤</span>
    <span class="nav-label">Cuenta</span>
  </a>
</nav>
css
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  display: flex;
  justify-content: space-around;
  padding: 8px 0;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
  border-top: 1px solid #E2E8F0;
  z-index: 100;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: #A0AEC0;
  font-size: 12px;
  position: relative;
  padding: 4px 12px;
}

.nav-item.active {
  color: #3182CE;
}

.nav-icon {
  font-size: 22px;
}

.nav-label {
  font-size: 11px;
  margin-top: 2px;
}

.nav-badge {
  position: absolute;
  top: 0;
  right: 0;
  background: #E53E3E;
  color: white;
  font-size: 10px;
  font-weight: 700;
  padding: 1px 5px;
  border-radius: 10px;
  min-width: 16px;
  text-align: center;
}
7. TÍTULOS Y SECCIONES MEJORADOS
html
<!-- Sección de productos -->
<section class="product-section">
  <div class="section-header">
    <h2 class="section-title">🎮 Tarjetas Gráficas</h2>
    <a href="/category/gpu" class="see-all">Ver todas →</a>
  </div>
  
  <div class="product-grid">
    <!-- Cards de productos aquí -->
  </div>
</section>
css
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 0 12px 0;
}

.section-title {
  font-size: 22px;
  font-weight: 700;
  color: #2D3748;
}

.see-all {
  font-size: 14px;
  color: #3182CE;
  text-decoration: none;
  font-weight: 500;
}

.product-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
📊 CHECKLIST DE MEJORAS PRIORIZADAS
🚨 Prioridad Alta (Hacer ahora):
Aumentar tamaño de fuente a mínimo 16px para texto

Agrandar botones a mínimo 44px de altura

Agregar imágenes a los productos

Mostrar precio original tachado + descuento visible

Agregar contador de carrito en el header

Mejorar espaciado entre productos (padding/margin)

Agregar feedback visual al tocar botones

⚠️ Prioridad Media (Próximo sprint):
Implementar grid de 2 columnas para productos

Agregar filtros por categoría y precio

Implementar barra de búsqueda funcional

Agregar bottom navigation con 5 íconos

Mostrar valoraciones de productos (estrellas)

Agregar badges de "Oferta" y "En Stock"

💡 Prioridad Baja (Futuro):
Agregar carrusel de productos destacados

Implementar historial de navegación

Agregar modo oscuro

Implementar wishlist (lista de deseos)

Agregar comparador de productos

🛠️ RECURSOS Y HERRAMIENTAS
Para mejorar el diseño:
Figma - Prototipado rápido

Coolors - Paleta de colores

Google Fonts - Fuentes modernas (ej: Inter, Poppins)

Unsplash - Imágenes de productos placeholder

Para pruebas en móvil:
Chrome DevTools (modo dispositivo)

BrowserStack - Pruebas en dispositivos reales

Lighthouse - Evaluación de rendimiento

Referencias de diseño:
Material Design (Google) - Components

Apple HIG - Guía de iOS

Dribbble - Inspiración visual

Shopify - Referencia de ecommerce

🎯 RESUMEN DE CAMBIOS SUGERIDOS
Elemento Estado Actual Estado Recomendado
Tamaño fuente Muy pequeño (<14px) 16-24px según jerarquía
Botones Pequeños (<40px) 44-48px de altura
Espaciado Muy apretado Padding de 12-16px
Imágenes Sin imágenes Con imagen + badges
Precios Solo precio actual Actual + original + % descuento
Navegación Solo superior Superior + bottom nav
Carrito No visible Contador visible siempre
Categorías Texto plano Chips scroll horizontales
🔥 BONUS: Código completo de ejemplo
html
<!-- Página de ejemplo completa -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MIKI TECH - Hardware</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header -->
  <header class="mobile-header">
    <!-- ... -->
  </header>
  
  <!-- Filtros -->
  <div class="filter-chips">
    <!-- ... -->
  </div>
  
  <!-- Productos -->
  <section class="product-section">
    <div class="section-header">
      <h2>🎮 Tarjetas Gráficas</h2>
      <a href="#">Ver todas →</a>
    </div>

    <div class="product-grid">
      <!-- Card 1 -->
      <div class="product-card">
        <div class="product-image">
          <img src="gpu1.jpg" alt="Curiosity3">
          <span class="badge-offer">-10%</span>
          <span class="badge-stock">✅ Stock</span>
        </div>
        <div class="product-info">
          <h3 class="product-name">Curiosity3</h3>
          <div class="product-price">
            <span class="price-current">$2.700.000</span>
            <span class="price-old">$3.000.000</span>
          </div>
        </div>
        <div class="product-actions">
          <button class="btn-details">Detalles</button>
          <button class="btn-add">🛒 Agregar</button>
        </div>
      </div>
      
      <!-- Más cards... -->
    </div>
  </section>
  
  <!-- Bottom Navigation -->
  <nav class="bottom-nav">
    <!-- ... -->
  </nav>
</body>
</html>
