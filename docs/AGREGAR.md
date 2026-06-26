📋 MI ENTENDIMIENTO DE TU SOLICITUD
Lo que tienes AHORA:
Botón "AGREGAR" → Agrega directamente 1 unidad al carrito (sin preguntar cantidad)

El carrito SOLO se ve cuando haces clic en el ícono del carrito

No hay feedback visual cuando agregas un producto

Lo que QUIERES:
Botón "AGREGAR" → Abre un panel/ventana emergente (modal/overlay)

En ese panel, el usuario elige la cantidad que desea (1, 2, 3, etc.)

Después de confirmar, se agrega al carrito con la cantidad seleccionada

NO quieres que el carrito se abra automáticamente al agregar

El carrito solo se visualiza cuando el usuario hace clic en el ícono del carrito

Buena práctica: No perder al usuario en el flujo de compra

Flujo que DESEAS:
text

1. Usuario ve un producto
2. Hace clic en "AGREGAR"
3. ✨ Se abre un panel/ventana flotante (overlay)
4. ✨ El panel muestra:
   - Nombre del producto
   - Precio
   - Selector de cantidad (+ / - o input numérico)
   - Botones: "Agregar al carrito" o "Cancelar"
5. Usuario elige cantidad (ej: 3)
6. Hace clic en "Agregar al carrito"
7. ✨ El panel se cierra
8. ✨ El carrito se actualiza en segundo plano (el ícono muestra el contador actualizado)
9. El usuario sigue navegando sin interrupciones
10. Solo si hace clic en el ícono 🛒, ve el carrito completo
Beneficios de este enfoque:
✅ Control: El usuario decide cuántas unidades quiere

✅ Menos clics: No tiene que ir al carrito para modificar cantidades

✅ Menos abandono: No lo sacas de la página de productos

✅ Feedback visual: El contador del carrito se actualiza inmediatamente

✅ Experiencia fluida: Sigue navegando sin interrupciones

🔍 ¿Entendí bien?
Preguntas de confirmación:

¿Quieres que el panel muestre el producto que está agregando (nombre, imagen, precio)?

¿El selector de cantidad debe tener botones "+" y "-" o un input numérico?

¿Debe tener un límite máximo basado en el stock disponible?

¿Quieres que el panel tenga animación (slide, fade, etc.)?

¿El ícono del carrito debe mostrar el número total de items o el número de productos diferentes?

✅ SI ENTENDÍ BIEN - Aquí está tu PROMPT
markdown

# PROMPT PARA ANTIGRAVITY - SISTEMA DE AGREGADO CON SELECTOR DE CANTIDAD (OVERLAY)

## CONTEXTO ACTUAL

Mi ecommerce MIKI TECH actualmente tiene un flujo de agregado al carrito que NO es óptimo:

**Comportamiento actual:**

- Botón "AGREGAR" → Agrega 1 unidad directamente al carrito
- No pregunta cantidad
- No hay feedback visual (solo un contador que cambia)
- El carrito solo es visible al hacer clic en el ícono del carrito
- Los usuarios no pueden elegir cuántas unidades comprar sin ir al carrito

**Problemas:**

1. ❌ Usuarios no pueden comprar múltiples unidades de un solo producto
2. ❌ Si quieren 3 unidades, deben agregar 1, ir al carrito, modificar cantidad (3 clics extra)
3. ❌ Sin feedback visual cuando agregan un producto
4. ❌ Flujo poco intuitivo para compras por cantidad

## LO QUE QUIERO IMPLEMENTAR

### 1. SISTEMA DE OVERLAY/MODAL PARA AGREGAR

**Comportamiento deseado:**

1. Usuario hace clic en "AGREGAR" en una tarjeta de producto
2. Se abre un **panel overlay/modal** (sin cerrar la página actual)
3. El overlay muestra:
   - 📷 Imagen del producto (pequeña)
   - 📝 Nombre del producto
   - 💰 Precio unitario
   - 🔢 Selector de cantidad (con botones + y -)
   - 🛒 Botón principal: "Agregar al Carrito"
   - ❌ Botón secundario: "Cancelar" o "Seguir comprando"
4. Usuario selecciona la cantidad deseada (ej: 3)
5. Hace clic en "Agregar al Carrito"
6. El overlay se cierra con animación suave
7. El contador del carrito se actualiza (ej: 1 → 4)
8. El usuario sigue en la misma página sin interrupciones

### 2. CARACTERÍSTICAS DEL OVERLAY

**Diseño:**

- Fondo semitransparente (backdrop) que oscurece el contenido detrás
- Panel centrado o desde abajo (slide-up en móvil)
- Animación: fade-in + scale (entrada suave)
- Cierre al hacer clic fuera del panel (opcional)
- Cierre con tecla ESC

**Selector de cantidad:**

- Botón "-" (disminuir, mínimo 1)
- Input numérico mostrando cantidad actual
- Botón "+" (aumentar)
- Límite máximo: stock disponible (si existe)
- Si hay stock limitado, mostrar "Máximo X unidades disponibles"

**Ejemplo de selector:**
┌─────────────────────┐
│ ¿Cuántos deseas? │
│ │
│ [−] [ 3 ] [+] │
│ │
│ Precio total: $8.1M│
│ │
│ [Agregar al Carrito] │
│ [Seguir comprando] │
└─────────────────────┘

text

### 3. ACTUALIZACIÓN DEL CARRITO (SIN ABRIRLO)

**Comportamiento:**

- ❌ NO abrir el carrito al agregar (solo si el usuario hace clic en el ícono)
- ✅ Actualizar el contador del carrito (número de items totales)
- ✅ Mostrar notificación sutil (ej: "3x Curiosity3 agregado al carrito")
- ✅ Actualizar el estado global del carrito (Redux/Context)

**Ejemplo de notificación:**
┌─────────────────────────────┐
│ ✅ 3x Curiosity3 agregado │ ← Toast notification (esquina inferior)
│ al carrito │
└─────────────────────────────┘

text

### 4. INTERFAZ DE USUARIO (UI)

**Overlay (Desktop):**

```html
<div class="modal-overlay" id="addToCartModal">
  <div class="modal-content">
    <button class="modal-close">✕</button>
    
    <div class="modal-product">
      <img src="producto.jpg" alt="Producto">
      <div class="modal-product-info">
        <h3>Curiosity3</h3>
        <p class="modal-price">$2.700.000</p>
      </div>
    </div>
    
    <div class="modal-quantity">
      <label>Cantidad:</label>
      <div class="quantity-selector">
        <button class="qty-btn minus">−</button>
        <input type="number" value="1" min="1" max="10">
        <button class="qty-btn plus">+</button>
      </div>
      <p class="stock-info">Disponibles: 10 unidades</p>
    </div>
    
    <div class="modal-total">
      <span>Total:</span>
      <span class="total-price">$2.700.000</span>
    </div>
    
    <div class="modal-actions">
      <button class="btn-secondary" onclick="closeModal()">
        Seguir comprando
      </button>
      <button class="btn-primary" onclick="addToCart()">
        🛒 Agregar al Carrito
      </button>
    </div>
  </div>
</div>
CSS del Overlay:

css
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: none; /* Hidden by default */
  justify-content: center;
  align-items: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease;
}

.modal-overlay.active {
  display: flex;
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 32px;
  max-width: 480px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}

.modal-close {
  position: absolute;
  top: 12px;
  right: 16px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #A0AEC0;
}

.modal-product {
  display: flex;
  gap: 16px;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #E2E8F0;
}

.modal-product img {
  width: 80px;
  height: 80px;
  object-fit: contain;
  background: #F7FAFC;
  border-radius: 8px;
}

.modal-product-info h3 {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 4px 0;
}

.modal-price {
  font-size: 20px;
  font-weight: 700;
  color: #2D3748;
}

.quantity-selector {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 12px 0 8px 0;
}

.qty-btn {
  width: 40px;
  height: 40px;
  background: #EDF2F7;
  border: none;
  border-radius: 8px;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.qty-btn:hover {
  background: #E2E8F0;
}

.qty-btn:active {
  transform: scale(0.95);
}

.quantity-selector input {
  width: 60px;
  text-align: center;
  padding: 8px;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 18px;
  font-weight: 600;
}

.quantity-selector input:focus {
  outline: none;
  border-color: #3182CE;
}

/* Quitar flechas del input number */
.quantity-selector input::-webkit-inner-spin-button,
.quantity-selector input::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.quantity-selector input {
  -moz-appearance: textfield;
}

.stock-info {
  font-size: 14px;
  color: #718096;
  margin: 4px 0 16px 0;
}

.modal-total {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 0;
  border-top: 2px solid #E2E8F0;
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: 600;
}

.total-price {
  font-size: 24px;
  color: #2D3748;
}

.modal-actions {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: 12px;
}

.btn-secondary {
  padding: 12px;
  background: #EDF2F7;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 500;
  color: #4A5568;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-secondary:hover {
  background: #E2E8F0;
}

.btn-primary {
  padding: 12px;
  background: #3182CE;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  color: white;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.btn-primary:hover {
  background: #2C5282;
  transform: scale(1.02);
}

.btn-primary:active {
  transform: scale(0.98);
}

/* Toast notification */
.toast-notification {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #48BB78;
  color: white;
  padding: 16px 24px;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  display: none;
  align-items: center;
  gap: 12px;
  font-weight: 500;
  z-index: 2000;
  animation: slideUp 0.3s ease;
}

.toast-notification.show {
  display: flex;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
5. JavaScript (Lógica)
javascript
// Estado global del carrito
let cart = [];
let cartCount = 0;

// Abrir modal
function openModal(productId) {
  const modal = document.getElementById('addToCartModal');
  const product = getProductById(productId);
  
  // Llenar datos del producto
  document.querySelector('.modal-product img').src = product.image;
  document.querySelector('.modal-product-info h3').textContent = product.name;
  document.querySelector('.modal-price').textContent = formatPrice(product.price);
  document.querySelector('.stock-info').textContent = `Disponibles: ${product.stock} unidades`;
  document.querySelector('.quantity-selector input').value = 1;
  updateTotal(product.price, 1);
  
  // Guardar producto actual en data attribute
  modal.dataset.productId = productId;
  modal.dataset.productPrice = product.price;
  
  // Mostrar modal
  modal.classList.add('active');
  document.body.style.overflow = 'hidden'; // Prevenir scroll
}

// Cerrar modal
function closeModal() {
  const modal = document.getElementById('addToCartModal');
  modal.classList.remove('active');
  document.body.style.overflow = 'auto';
}

// Actualizar cantidad
function updateQuantity(change) {
  const input = document.querySelector('.quantity-selector input');
  let value = parseInt(input.value) + change;
  const min = parseInt(input.min);
  const max = parseInt(input.max);
  
  if (value < min) value = min;
  if (value > max) value = max;
  
  input.value = value;
  
  // Actualizar total
  const price = parseFloat(document.getElementById('addToCartModal').dataset.productPrice);
  updateTotal(price, value);
}

// Actualizar total
function updateTotal(price, quantity) {
  const total = price * quantity;
  document.querySelector('.total-price').textContent = formatPrice(total);
}

// Agregar al carrito
function addToCart() {
  const modal = document.getElementById('addToCartModal');
  const productId = modal.dataset.productId;
  const quantity = parseInt(document.querySelector('.quantity-selector input').value);
  const product = getProductById(productId);
  
  // Agregar al carrito
  const existingItem = cart.find(item => item.id === productId);
  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    cart.push({
      id: productId,
      name: product.name,
      price: product.price,
      quantity: quantity,
      image: product.image
    });
  }
  
  // Actualizar contador
  cartCount += quantity;
  updateCartBadge(cartCount);
  
  // Mostrar toast notification
  showToast(`${quantity}x ${product.name} agregado al carrito`);
  
  // Cerrar modal
  closeModal();
}

// Mostrar toast
function showToast(message) {
  const toast = document.getElementById('toastNotification');
  toast.textContent = `✅ ${message}`;
  toast.classList.add('show');
  
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

// Actualizar badge del carrito
function updateCartBadge(count) {
  const badge = document.querySelector('.cart-badge');
  if (badge) {
    badge.textContent = count;
    badge.style.display = count > 0 ? 'block' : 'none';
  }
}

// Cerrar modal al hacer clic fuera
document.getElementById('addToCartModal').addEventListener('click', function(e) {
  if (e.target === this) {
    closeModal();
  }
});

// Cerrar modal con tecla ESC
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeModal();
  }
});
REQUERIMIENTOS ADICIONALES
Cantidad mínima: 1

Cantidad máxima: Stock disponible (si existe) o 99 (si no hay stock)

Precio total: Se actualiza en tiempo real al cambiar cantidad

Notificación: Toast que desaparece después de 3 segundos

Accesibilidad: El modal debe ser navegable con teclado

Responsive: El modal debe adaptarse a móvil (slide-up en móvil)

PREGUNTAS ESPECÍFICAS
¿El modal debe mostrar el precio total o solo el precio unitario?

¿Qué pasa si el producto tiene variantes (color, tamaño)?

¿El selector de cantidad debe tener botones grandes para móvil?

¿La notificación debe ser visible en todas las pantallas?

¿Qué sucede si el usuario intenta agregar más de lo que hay en stock?

ENTREGABLES ESPERADOS
✅ Código HTML del modal/overlay

✅ CSS completo con animaciones

✅ JavaScript para la lógica de cantidad y carrito

✅ Ejemplo de integración con las cards existentes

✅ Estrategia de manejo de stock

✅ Mejores prácticas de UX para este flujo

Por favor, proporciona una implementación completa y optimizada para desktop y móvil.

text

---

## 📋 Resumen del flujo para que lo verifiques

| Paso | Acción del usuario | Lo que pasa |
|------|-------------------|-------------|
| 1 | Clic en "AGREGAR" | Se abre modal overlay |
| 2 | Selecciona cantidad (ej: 3) | Se actualiza el precio total |
| 3 | Clic en "Agregar al Carrito" | Se cierra modal |
| 4 | - | Se actualiza contador del carrito |
| 5 | - | Aparece toast notification |
| 6 | Clic en 🛒 | Se abre el carrito con los items |

**¿Es esto exactamente lo que necesitas?** ¿O hay algún ajuste que quieras hacer antes de que te entregue el prompt final?
