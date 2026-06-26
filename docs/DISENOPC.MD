
markdown

# PROMPT PARA ANTIGRAVITY - MEJORA DE UX DESKTOP PARA ECOMMERCE MIKI TECH

## CONTEXTO ACTUAL

Mi ecommerce **MIKI TECH** (venta de hardware/componentes) tiene una versión desktop que necesita mejoras significativas.

### Estado actual (basado en imagen proporcionada)

**Header:**

- Logo "MIKI TECH" a la izquierda
- Navegación simple: "Inicio Tienda Contacto"
- Barra de búsqueda: "Buscar hardware..."

**Cuerpo:**

- Sección "Tarjetas Gráficas" (se repite)
- Productos en lista vertical (no en grid)
- Cada producto muestra:
  - "STOCK DISPONIBLE"
  - Nombre del producto
  - Precio (algunos con oferta)
- Botones: "DETALLES" y "AGREGAR"

### Problemas identificados en desktop

1. **❌ Espacio desperdiciado** - Pantalla ancha pero contenido centrado y angosto
2. **❌ Sin grid de productos** - Lista vertical poco eficiente
3. **❌ Falta de imágenes** - Solo texto, sin visuales atractivos
4. **❌ Navegación limitada** - Solo 3 enlaces, sin categorías desplegables
5. **❌ Sin filtros laterales** - No hay forma de refinar búsqueda
6. **❌ Precios poco destacados** - No hay jerarquía visual clara
7. **❌ Sin carrito visible** - No se ve el contador del carrito
8. **❌ Sin breadcrumbs** - El usuario no sabe dónde está
9. **❌ Footer básico** - Sin información relevante
10. **❌ Sin llamadas a la acción** - Los botones no son persuasivos

### Tecnologías

- Frontend: [React/Vue/Angular/HTML+CSS]
- Framework CSS: [Tailwind/Bootstrap/Material-UI]
- Estado: [Redux/Context/Vuex]

## OBJETIVO PRINCIPAL

Rediseñar la experiencia **desktop** de MIKI TECH para que sea:

1. **Visualmente atractiva** - Diseño moderno y profesional
2. **Eficiente** - Aprovechar el espacio de pantalla ancha
3. **Intuitiva** - Navegación clara y fácil
4. **Conversora** - Optimizada para aumentar ventas
5. **Escalable** - Que pueda crecer con más productos y categorías

## REQUERIMIENTOS DE DISEÑO DESKTOP

### 1. ESTRUCTURA DE PÁGINA (LAYOUT)

#### Layout recomendado (3 columnas)

┌─────────────────────────────────────────────────────────────┐
│ HEADER (Logo + Búsqueda + Navegación + Carrito + Cuenta) │
├─────────┬───────────────────────────────────┬───────────────┤
│ Filtros │ GRID DE PRODUCTOS │ Widgets │
│ │ │ (Ofertas, │
│ - Cat. │ ┌─────┐ ┌─────┐ ┌─────┐ │ Destacados)│
│ - Precio│ │ Card │ │ Card │ │ Card │ │ │
│ - Marca │ └─────┘ └─────┘ └─────┘ │ │
│ - Rating│ ┌─────┐ ┌─────┐ ┌─────┐ │ │
│ │ │ Card │ │ Card │ │ Card │ │ │
│ │ └─────┘ └─────┘ └─────┘ │ │
│ │ │ │
├─────────┴───────────────────────────────────┴───────────────┤
│ FOOTER (Información + Links + Redes Sociales) │
└─────────────────────────────────────────────────────────────┘

text

#### Breakpoints desktop

- **Desktop pequeño:** 1024px - 1366px (3 columnas de productos)
- **Desktop mediano:** 1367px - 1920px (4 columnas de productos)
- **Desktop grande:** > 1920px (5 columnas de productos, max-width)

### 2. HEADER MEJORADO

#### Versión actual

[MIKI TECH] [Inicio] [Tienda] [Contacto] [Buscar hardware...]

text

#### Versión mejorada

┌──────────────────────────────────────────────────────────────────────┐
│ 🛒 MIKI TECH │ [Todas] [Gamer] [Pro] [Ofertas] │ 🔍 [Buscar...] │ 🛍️(3) 👤 │
│ │ │ │
│ │ [Categorías ▼] [Marcas ▼] [Soporte ▼] │ │
└──────────────────────────────────────────────────────────────────────┘

text

#### Código ejemplo

```html
<header class="desktop-header">
  <div class="header-main">
    <!-- Logo -->
    <div class="logo">
      <span class="logo-icon">🛒</span>
      <span class="logo-text">MIKI TECH</span>
    </div>
    
    <!-- Navegación principal -->
    <nav class="main-nav">
      <a href="#" class="nav-link active">Inicio</a>
      <a href="#" class="nav-link">Tienda</a>
      <a href="#" class="nav-link">Ofertas</a>
      <div class="nav-dropdown">
        <a href="#" class="nav-link">Categorías ▾</a>
        <div class="dropdown-content">
          <a href="#">Tarjetas Gráficas</a>
          <a href="#">Procesadores</a>
          <a href="#">Placas Madre</a>
          <a href="#">Memorias RAM</a>
          <a href="#">Almacenamiento</a>
          <a href="#">Fuentes de Poder</a>
        </div>
      </div>
    </nav>
    
    <!-- Acciones -->
    <div class="header-actions">
      <div class="search-bar">
        <input type="text" placeholder="Buscar productos...">
        <button>🔍</button>
      </div>
      <button class="cart-btn">
        🛍️
        <span class="cart-badge">3</span>
      </button>
      <button class="user-btn">👤</button>
    </div>
  </div>
  
  <!-- Breadcrumbs -->
  <div class="breadcrumbs">
    <a href="#">Inicio</a> › <a href="#">Tienda</a> › <span>Tarjetas Gráficas</span>
  </div>
</header>
css
.desktop-header {
  background: white;
  border-bottom: 1px solid #E2E8F0;
  padding: 12px 32px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-main {
  display: flex;
  align-items: center;
  gap: 32px;
  max-width: 1440px;
  margin: 0 auto;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 28px;
  font-weight: 700;
  color: #2D3748;
  white-space: nowrap;
}

.main-nav {
  display: flex;
  gap: 24px;
  align-items: center;
}

.nav-link {
  font-size: 16px;
  font-weight: 500;
  color: #4A5568;
  text-decoration: none;
  padding: 8px 4px;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
}

.nav-link:hover {
  color: #3182CE;
  border-bottom-color: #3182CE;
}

.nav-link.active {
  color: #3182CE;
  border-bottom-color: #3182CE;
}

.nav-dropdown {
  position: relative;
}

.dropdown-content {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  min-width: 200px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
  border-radius: 8px;
  padding: 8px 0;
}

.nav-dropdown:hover .dropdown-content {
  display: block;
}

.dropdown-content a {
  display: block;
  padding: 8px 16px;
  color: #4A5568;
  text-decoration: none;
  font-size: 14px;
}

.dropdown-content a:hover {
  background: #F7FAFC;
  color: #3182CE;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-left: auto;
}

.search-bar {
  display: flex;
  align-items: center;
  background: #F7FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  padding: 4px 8px;
}

.search-bar input {
  border: none;
  background: transparent;
  padding: 8px 12px;
  font-size: 14px;
  width: 250px;
}

.search-bar input:focus {
  outline: none;
}

.search-bar button {
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
  padding: 4px 8px;
}

.cart-btn {
  position: relative;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  padding: 8px;
}

.cart-badge {
  position: absolute;
  top: 2px;
  right: 2px;
  background: #E53E3E;
  color: white;
  font-size: 12px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 12px;
  min-width: 20px;
  text-align: center;
}

.breadcrumbs {
  padding: 12px 0 4px 0;
  font-size: 14px;
  color: #A0AEC0;
  max-width: 1440px;
  margin: 0 auto;
}

.breadcrumbs a {
  color: #3182CE;
  text-decoration: none;
}

.breadcrumbs a:hover {
  text-decoration: underline;
}
3. PANEL DE FILTROS LATERAL
html
<aside class="filters-sidebar">
  <div class="filter-section">
    <h3>Categorías</h3>
    <ul class="filter-list">
      <li><a href="#" class="active">Tarjetas Gráficas</a></li>
      <li><a href="#">Procesadores</a></li>
      <li><a href="#">Placas Madre</a></li>
      <li><a href="#">Memorias RAM</a></li>
      <li><a href="#">Almacenamiento</a></li>
    </ul>
  </div>
  
  <div class="filter-section">
    <h3>Precio</h3>
    <div class="price-range">
      <input type="range" min="0" max="10000000" step="100000">
      <div class="price-inputs">
        <input type="number" placeholder="$0">
        <span>-</span>
        <input type="number" placeholder="$10M">
      </div>
    </div>
  </div>
  
  <div class="filter-section">
    <h3>Marcas</h3>
    <label><input type="checkbox"> NVIDIA</label>
    <label><input type="checkbox"> AMD</label>
    <label><input type="checkbox"> MSI</label>
    <label><input type="checkbox"> Gigabyte</label>
    <label><input type="checkbox"> ASUS</label>
  </div>
  
  <div class="filter-section">
    <h3>Calificación</h3>
    <label><input type="checkbox"> ★★★★★ (4.5+)</label>
    <label><input type="checkbox"> ★★★★☆ (4.0+)</label>
    <label><input type="checkbox"> ★★★☆☆ (3.5+)</label>
  </div>
  
  <div class="filter-section">
    <h3>Disponibilidad</h3>
    <label><input type="checkbox" checked> En Stock</label>
    <label><input type="checkbox"> En Oferta</label>
  </div>
  
  <button class="btn-apply-filters">Aplicar Filtros</button>
  <button class="btn-clear-filters">Limpiar</button>
</aside>
css
.filters-sidebar {
  width: 260px;
  flex-shrink: 0;
  padding-right: 24px;
}

.filter-section {
  margin-bottom: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid #E2E8F0;
}

.filter-section h3 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #2D3748;
}

.filter-list {
  list-style: none;
  padding: 0;
}

.filter-list li {
  margin-bottom: 6px;
}

.filter-list a {
  color: #4A5568;
  text-decoration: none;
  font-size: 14px;
  display: block;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s;
}

.filter-list a:hover {
  background: #F7FAFC;
  color: #3182CE;
}

.filter-list a.active {
  background: #EBF8FF;
  color: #3182CE;
  font-weight: 500;
}

.filter-section label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  color: #4A5568;
  margin-bottom: 6px;
  cursor: pointer;
}

.price-range {
  margin-top: 8px;
}

.price-range input[type="range"] {
  width: 100%;
}

.price-inputs {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
}

.price-inputs input {
  width: 80px;
  padding: 6px 8px;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
  font-size: 14px;
}

.btn-apply-filters {
  width: 100%;
  padding: 10px;
  background: #3182CE;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 8px;
}

.btn-apply-filters:hover {
  background: #2C5282;
}

.btn-clear-filters {
  width: 100%;
  padding: 8px;
  background: none;
  color: #A0AEC0;
  border: 1px solid #E2E8F0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}

.btn-clear-filters:hover {
  background: #F7FAFC;
}
4. GRID DE PRODUCTOS MEJORADO
Versión actual (lista vertical):
text
┌─────────────────────────────────────┐
│ STOCK DISPONIBLE                     │
│ Curiosity3                           │
│ $3.000.000  $2.700.000 OFERTA       │
│ [DETALLES] [AGREGAR]                │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│ STOCK DISPONIBLE                     │
│ NVIDIA Tarjetas Pro-3755             │
│ $5.220.115                           │
│ [DETALLES] [AGREGAR]                │
└─────────────────────────────────────┘
Versión mejorada (grid 3-4 columnas):
html
<section class="products-section">
  <div class="products-header">
    <h2>Tarjetas Gráficas</h2>
    <div class="products-toolbar">
      <span class="product-count">24 productos</span>
      <select class="sort-select">
        <option>Relevancia</option>
        <option>Precio: menor a mayor</option>
        <option>Precio: mayor a menor</option>
        <option>Más vendidos</option>
        <option>Mejor calificados</option>
      </select>
      <div class="view-options">
        <button class="view-grid active">▦</button>
        <button class="view-list">☰</button>
      </div>
    </div>
  </div>
  
  <div class="product-grid">
    <!-- Card de producto mejorada -->
    <div class="product-card">
      <div class="product-image">
        <img src="gpu1.jpg" alt="Curiosity3">
        <span class="badge-offer">-10%</span>
        <span class="badge-stock">✅ En Stock</span>
        <button class="btn-wishlist">❤️</button>
      </div>
      
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
        <div class="product-meta">
          <span class="meta-shipping">🚚 Envío gratis</span>
          <span class="meta-warranty">✅ Garantía 1 año</span>
        </div>
      </div>
      
      <div class="product-actions">
        <button class="btn-details">Ver Detalles</button>
        <button class="btn-add">🛒 Agregar al Carrito</button>
      </div>
    </div>
    
    <!-- Repetir para más productos -->
  </div>
  
  <!-- Paginación -->
  <div class="pagination">
    <button class="page-btn">‹</button>
    <button class="page-btn active">1</button>
    <button class="page-btn">2</button>
    <button class="page-btn">3</button>
    <button class="page-btn">...</button>
    <button class="page-btn">12</button>
    <button class="page-btn">›</button>
  </div>
</section>
css
.products-section {
  flex: 1;
}

.products-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 12px;
}

.products-header h2 {
  font-size: 28px;
  font-weight: 700;
  color: #2D3748;
}

.products-toolbar {
  display: flex;
  align-items: center;
  gap: 16px;
}

.product-count {
  color: #718096;
  font-size: 14px;
}

.sort-select {
  padding: 8px 12px;
  border: 1px solid #E2E8F0;
  border-radius: 6px;
  font-size: 14px;
  background: white;
}

.view-options {
  display: flex;
  gap: 4px;
}

.view-options button {
  padding: 6px 10px;
  background: none;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.view-options button.active {
  background: #3182CE;
  color: white;
  border-color: #3182CE;
}

/* Grid de productos */
.product-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 32px;
}

@media (min-width: 1367px) {
  .product-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Card de producto */
.product-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: all 0.3s ease;
  border: 1px solid #EDF2F7;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
  border-color: #3182CE;
}

.product-image {
  position: relative;
  height: 200px;
  background: #F7FAFC;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.product-image img {
  max-width: 80%;
  max-height: 80%;
  object-fit: contain;
  transition: transform 0.3s;
}

.product-card:hover .product-image img {
  transform: scale(1.05);
}

.badge-offer {
  position: absolute;
  top: 12px;
  left: 12px;
  background: #E53E3E;
  color: white;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 700;
}

.badge-stock {
  position: absolute;
  top: 12px;
  right: 12px;
  background: #48BB78;
  color: white;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 11px;
}

.btn-wishlist {
  position: absolute;
  bottom: 12px;
  right: 12px;
  background: white;
  border: none;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  font-size: 18px;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: all 0.2s;
}

.btn-wishlist:hover {
  background: #FED7D7;
  transform: scale(1.1);
}

.product-info {
  padding: 16px;
}

.product-name {
  font-size: 16px;
  font-weight: 600;
  color: #2D3748;
  margin-bottom: 4px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-rating {
  font-size: 13px;
  color: #718096;
  margin-bottom: 8px;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.price-current {
  font-size: 24px;
  font-weight: 700;
  color: #2D3748;
}

.price-old {
  font-size: 16px;
  color: #A0AEC0;
  text-decoration: line-through;
}

.price-discount {
  background: #FED7D7;
  color: #C53030;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
}

.product-meta {
  display: flex;
  gap: 12px;
  font-size: 12px;
  color: #718096;
  margin-top: 4px;
}

.product-actions {
  padding: 0 16px 16px 16px;
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: 8px;
}

.btn-details {
  padding: 10px;
  background: #EDF2F7;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  color: #4A5568;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-details:hover {
  background: #E2E8F0;
}

.btn-add {
  padding: 10px;
  background: #3182CE;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  color: white;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
}

.btn-add:hover {
  background: #2C5282;
  transform: scale(1.02);
}

/* Paginación */
.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 16px 0;
}

.page-btn {
  padding: 8px 14px;
  background: white;
  border: 1px solid #E2E8F0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.page-btn:hover {
  background: #F7FAFC;
}

.page-btn.active {
  background: #3182CE;
  color: white;
  border-color: #3182CE;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
5. WIDGETS LATERALES (Sidebar derecho)
html
<aside class="widgets-sidebar">
  <!-- Ofertas Destacadas -->
  <div class="widget">
    <h3>🔥 Ofertas del Día</h3>
    <div class="offer-item">
      <img src="offer1.jpg" alt="Oferta">
      <div class="offer-info">
        <h4>Gigabyte Pro-6305</h4>
        <span class="offer-price">$4.500.000</span>
        <span class="offer-old">$5.400.000</span>
        <span class="offer-timer">⏰ 3h 24m</span>
      </div>
    </div>
    <!-- Más ofertas... -->
  </div>
  
  <!-- Productos Más Vendidos -->
  <div class="widget">
    <h3>⭐ Más Vendidos</h3>
    <div class="top-product">
      <span class="top-rank">#1</span>
      <span>NVIDIA RTX 4080</span>
    </div>
    <!-- Más productos... -->
  </div>
  
  <!-- Newsletter -->
  <div class="widget newsletter">
    <h3>📧 Newsletter</h3>
    <p>Recibe ofertas exclusivas</p>
    <input type="email" placeholder="tu@email.com">
    <button>Suscribirse</button>
  </div>
</aside>
css
.widgets-sidebar {
  width: 240px;
  flex-shrink: 0;
  padding-left: 24px;
}

.widget {
  background: #F7FAFC;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 20px;
}

.widget h3 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #2D3748;
}

.offer-item {
  display: flex;
  gap: 12px;
  padding: 8px 0;
  border-bottom: 1px solid #E2E8F0;
}

.offer-item img {
  width: 60px;
  height: 60px;
  object-fit: contain;
  background: white;
  border-radius: 4px;
}

.offer-info h4 {
  font-size: 14px;
  font-weight: 500;
  margin: 0 0 4px 0;
}

.offer-price {
  font-size: 18px;
  font-weight: 700;
  color: #E53E3E;
}

.offer-old {
  font-size: 12px;
  color: #A0AEC0;
  text-decoration: line-through;
  margin-left: 6px;
}

.offer-timer {
  display: block;
  font-size: 12px;
  color: #718096;
  margin-top: 2px;
}

.top-product {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 0;
  font-size: 14px;
}

.top-rank {
  font-weight: 700;
  color: #3182CE;
  width: 24px;
}

.newsletter input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #E2E8F0;
  border-radius: 6px;
  font-size: 14px;
  margin-bottom: 8px;
}

.newsletter button {
  width: 100%;
  padding: 8px;
  background: #3182CE;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
}

.newsletter button:hover {
  background: #2C5282;
}
6. FOOTER MEJORADO
html
<footer class="desktop-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <h4>🛒 MIKI TECH</h4>
      <p>Tu tienda de confianza para hardware de alta calidad desde 2020.</p>
      <div class="social-links">
        <a href="#">📱</a>
        <a href="#">🐦</a>
        <a href="#">📘</a>
        <a href="#">📷</a>
      </div>
    </div>
    
    <div class="footer-col">
      <h4>Enlaces Rápidos</h4>
      <a href="#">Inicio</a>
      <a href="#">Tienda</a>
      <a href="#">Ofertas</a>
      <a href="#">Nuevos Productos</a>
    </div>
    
    <div class="footer-col">
      <h4>Ayuda</h4>
      <a href="#">FAQ</a>
      <a href="#">Envíos</a>
      <a href="#">Devoluciones</a>
      <a href="#">Garantías</a>
    </div>
    
    <div class="footer-col">
      <h4>Contacto</h4>
      <p>📧 soporte@mikitech.com</p>
      <p>📞 +57 300 123 4567</p>
      <p>📍 Bogotá, Colombia</p>
    </div>
  </div>
  
  <div class="footer-bottom">
    <span>© 2024 MIKI TECH. Todos los derechos reservados.</span>
    <div class="payment-methods">
      <span>💳 Visa</span>
      <span>💳 Mastercard</span>
      <span>💳 PayPal</span>
      <span>💳 MercadoPago</span>
    </div>
  </div>
</footer>
css
.desktop-footer {
  background: #2D3748;
  color: white;
  padding: 48px 32px 24px;
  margin-top: 48px;
}

.footer-grid {
  max-width: 1440px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 32px;
}

.footer-col h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
  color: white;
}

.footer-col p,
.footer-col a {
  color: #A0AEC0;
  line-height: 1.8;
  font-size: 14px;
}

.footer-col a {
  display: block;
  text-decoration: none;
}

.footer-col a:hover {
  color: white;
}

.social-links {
  display: flex;
  gap: 12px;
  margin-top: 12px;
}

.social-links a {
  font-size: 24px;
  text-decoration: none;
}

.footer-bottom {
  max-width: 1440px;
  margin: 0 auto;
  padding-top: 24px;
  border-top: 1px solid #4A5568;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  color: #A0AEC0;
}

.payment-methods {
  display: flex;
  gap: 16px;
}
PREGUNTAS ESPECÍFICAS PARA ANTIGRAVITY
¿Cuántas columnas de productos recomiendas para pantallas de 1920x1080?

¿Cómo implementar un mega menú para categorías en desktop?

¿Cuál es el mejor tamaño para imágenes de productos en desktop?

¿Cómo manejar el hover en tarjetas de producto?

¿Qué elementos deberían ser sticky en desktop?

¿Cómo mejorar el contraste y legibilidad en pantallas grandes?

¿Qué métricas de conversión son clave en desktop?

¿Cómo implementar un comparador de productos?

ENTREGABLES ESPERADOS
Código completo (HTML + CSS) para todas las secciones

Guía de estilos (tipografía, colores, espaciados)

Wireframes de las vistas principales

Recomendaciones de UX específicas para desktop

Checklist de implementación

Estrategia de testing en diferentes resoluciones

Por favor, actúa como un experto en UI/UX para ecommerce y proporciona una solución completa, moderna y optimizada para desktop.

text

---

## 📋 Resumen de mejoras clave para desktop

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Layout** | Lista vertical | Grid 3-4 columnas |
| **Header** | Simple, 3 enlaces | Con categorías desplegables + búsqueda |
| **Filtros** | No tenía | Sidebar izquierdo con filtros completos |
| **Cards** | Solo texto | Con imagen, rating, badges, meta-info |
| **Widgets** | No tenía | Ofertas, más vendidos, newsletter |
| **Footer** | Básico | Grid con info completa + redes sociales |
| **Interacción** | Estática | Hover, transiciones, feedback |

---

¿Quieres que profundice en alguna sección específica o que adapte el código a un framework particular (React, Vue, Angular)?
