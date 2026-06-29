🎯 PROMPT PARA ENTIGRAVITY
text
Actúa como un experto en UI/UX y desarrollo de paneles de administración para ecommerce.
Necesito que me ayudes a rediseñar y mejorar mi panel de administración de inventario
aplicando las mejores prácticas de la industria.

---

## CONTEXTO ACTUAL

Tengo un panel administrativo para MIKI TECH con las siguientes características:

- Gestión de inventario con 215 productos registrados
- Vista en tabla con los campos: Nombre, SKU, Modelo, Slug, Descripción
- Filtro básico por nombre/marca y estado
- Precio en COP, Stock disponible y Estado (Activo/Inactivo)
- Secciones: Dashboard, Inventario, Clientes, Pedidos, Categorías, Análisis, Reportes
- Alertas de stock crítico (duplicadas en la interfaz)
- Carga masiva y creación de nuevos productos

---

## PROBLEMAS IDENTIFICADOS

1. **UX/UI deficiente**: Todo tiene el mismo peso visual, falta jerarquía, espaciado y color con propósito
2. **Datos incompletos**: Faltan columnas como Categoría, Proveedor, Fecha de creación, Costo
3. **Acciones confusas**: En la columna "Acciones" solo aparece "Activo" (error)
4. **Filtros limitados**: Solo permite filtrar por nombre y estado
5. **Sin indicadores visuales**: No hay KPIs, gráficos ni alertas configurables
6. **Duplicación**: La sección "ALERTAS STOCK - CRÍTICAS" aparece dos veces
7. **SKU opcional**: Muestra "N/A" cuando debería ser obligatorio
8. **Sin auditoría**: No hay historial de cambios ni trazabilidad
9. **Sin exportación**: No se pueden exportar datos a CSV/Excel
10. **Poca escalabilidad**: No tiene paginación ni carga perezosa

---

## REQUERIMIENTOS DE MEJORA (APLICANDO BUENAS PRÁCTICAS)

### 1. DISEÑO Y JERARQUÍA VISUAL

- Implementar un sistema de diseño con tarjetas (cards), sombras y espaciado consistente
- Usar colores con propósito: Verde para activo, rojo/naranja para stock crítico, azul para acciones primarias
- Jerarquía tipográfica clara (títulos 24px, subtítulos 18px, cuerpo 14px)
- Añadir iconografía consistente (FontAwesome o Material Icons)
- Mejorar el contraste y la accesibilidad (ratio 4.5:1)

### 2. FUNCIONALIDAD Y DATOS

- **Nuevas columnas en la tabla**: Categoría, Proveedor, Fecha creación, Costo, Margen de ganancia
- **SKU obligatorio**: Validar que no sea "N/A" y que sea único
- **Filtros avanzados**: Por rango de precios, categoría, proveedor, fecha de ingreso, umbral de stock
- **Acciones por lote**: Seleccionar múltiples productos y cambiar estado, actualizar precio o eliminar
- **Edición inline**: Poder editar precio y stock directamente desde la tabla
- **Historial de cambios**: Mostrar quién y cuándo modificó cada producto

### 3. KPIs Y DASHBOARD

Crear una sección superior con indicadores clave:

- Total de productos
- Productos con stock crítico (configurable)
- Valor total del inventario
- Productos sin stock
- Productos más vendidos (si hay datos)
- Tasa de conversión de productos activos

### 4. GRÁFICOS Y REPORTES

- Gráfico de barras: Stock por categoría
- Gráfico de torta: Distribución por estado (Activo/Inactivo/Agotado)
- Gráfico de tendencia: Movimiento de inventario en los últimos 30 días
- Botón de exportación a CSV/Excel

### 5. ALERTAS Y NOTIFICACIONES

- Eliminar duplicados de alertas
- Sistema de notificaciones toast (ej. "Producto actualizado correctamente")
- Alertas configurables: Permitir definir umbral de stock crítico
- Confirmaciones para acciones destructivas (eliminar, desactivar)

### 6. RENDIMIENTO Y ESCALABILIDAD

- Paginación de 20 productos por página
- Búsqueda en tiempo real con debounce (300ms)
- Carga perezosa (lazy loading) para imágenes
- Indicadores de carga (spinners)

### 7. ACCESIBILIDAD (A11Y)

- Etiquetas asociadas a todos los inputs (aria-label, for)
- Navegación completa por teclado (Tab, Enter, Escape)
- Texto alternativo en imágenes
- Estructura semántica HTML5 (header, nav, main, section)

---

## ENTREGABLES ESPERADOS

Por favor, proporcióname:

1. **Estructura HTML/CSS mejorada** con todo el diseño jerarquizado
2. **Componentes de UI** reutilizables (tarjetas, botones, tabs, modales)
3. **Scripts de JavaScript** para funcionalidades (filtros, edición inline, paginación, búsqueda)
4. **Ejemplo de datos mock** con las nuevas columnas
5. **Código para el dashboard** con KPIs y gráficos (usando Chart.js o similar)
6. **Sistema de notificaciones** (toast)
7. **Mejoras en accesibilidad** (aria labels, roles, etc.)
8. **Documentación** de los cambios y cómo implementarlos

---

## RESTRICCIONES TÉCNICAS

- El panel debe ser **responsive** (mobile-first)
- Usar CSS moderno (Flexbox/Grid) sin frameworks pesados (opcional: Tailwind o Bootstrap 5)
- JavaScript vanilla o con jQuery si es necesario
- Los gráficos pueden usar Chart.js o ECharts
- El código debe ser limpio, comentado y mantenible

---

## TONO Y ESTILO DE RESPUESTA

Quiero una respuesta detallada, con ejemplos de código concretos, explicaciones de por qué cada mejora es una buena práctica, y priorización de implementación. Incluye también un plan de acción paso a paso para migrar del panel actual al nuevo.

---

**IMPORTANTE**: Necesito que el resultado final sea un panel completamente funcional y profesional, listo para ser presentado a stakeholders o clientes. Prioriza la usabilidad, la claridad y la experiencia de usuario.

¡Manos a la obra! 🚀
💡 CÓMO USAR ESTE PROMPT EN ENTIGRAVITY
Copia el prompt completo (desde "Actúa como un experto..." hasta el final)

Pégalo en Entigravity como una nueva conversación

Especifica el formato de salida que prefieres (puedes agregar al final):

"Prefiero que me des el código en archivos separados (index.html, styles.css, script.js)"

"Necesito que me expliques cada cambio antes de mostrarme el código"

"Quiero que me des primero el plan de acción y luego los detalles técnicos"

📌 EXTRAS QUE PUEDES AÑADIR AL PROMPT
Si quieres ser más específico, agrega estas secciones:

Ejemplo de datos actuales (para que la IA los use como base):
javascript
const productos = [
  {
    id: 1,
    nombre: "Memoria RAM",
    sku: "N/A",
    modelo: "N/A",
    slug: "intel-perifericos-pro-2125",
    descripcion: "",
    precio: 20000,
    stock: 9,
    estado: "Activo"
  },
  // ... más productos
]
Requisitos adicionales de negocio:
"Necesito que los precios se muestren con formato de moneda COP ($)"

"El stock crítico se define cuando hay menos de 5 unidades"

"Quiero que el panel tenga modo oscuro/claro"

"Debe tener un sistema de roles (admin, editor, viewer)"

🎁 BONUS: VERSIÓN CORTA DEL PROMPT
Si prefieres algo más conciso:

text
Rediseña mi panel de administración de inventario para MIKI TECH aplicando
las mejores prácticas de UI/UX. Tengo 215 productos en una tabla con
columnas básicas (Nombre, SKU, Precio, Stock, Estado).

Necesito:

1. Diseño jerarquizado con colores, iconos y espaciado
2. Nuevas columnas: Categoría, Proveedor, Fecha, Costo
3. KPIs visuales (total productos, stock crítico, valor inventario)
4. Gráficos de stock por categoría y estado
5. Filtros avanzados y búsqueda en tiempo real
6. Edición inline y acciones por lote
7. Paginación, notificaciones y confirmaciones
8. Código responsive, accesible y bien documentado

Proporcióname HTML, CSS y JS con ejemplos concretos y explica
cada mejora. Prioriza usabilidad y escalabilidad.
