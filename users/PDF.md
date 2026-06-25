markdown

# PROMPT PARA GEMINI 3.5 FLASH - FACTURAS COMPLETAS + ADMIN PANEL

> Copia y pega esto EXACTAMENTE en Antigravity con modelo **Gemini 3.5 Flash**

---

## PROMPT

Actúa como un experto en facturación electrónica, reportes de ventas y paneles de administración.

CONTEXTO:
Tengo una tienda/sistema web donde los clientes compran productos. Actualmente las facturas PDF NO descargan en producción. Pero además de arreglar la descarga, necesito que el sistema REGISTRE TODO CORRECTAMENTE.

REQUISITO OBLIGATORIO (NO TE DESVIES):
Cuando un cliente compra 10 productos diferentes, la factura DEBE registrar CADA UNO de los 10 productos con:

Nombre del producto

Cantidad

Precio unitario

Subtotal (precio unitario × cantidad)

Impuestos (si aplica)

Total por producto

NO quiero una factura que diga "10 productos" genérico. QUIERO CADA LÍNEA DETALLADA.

PROBLEMAS ACTUALES:
Las facturas PDF no se descargan en producción (en local sí)

Al comprar múltiples productos, la factura NO registra todos individualmente (solo muestra el total)

En el PANEL DE ADMINISTRACIÓN no puedo ver:

Cuánto vendí en un día específico (ej: "2026-01-15")

Reporte completo de ventas (todas las facturas)

Detalle de cada factura con sus productos

LO QUE NECESITO QUE HAGAS:
PARTE 1: ESTRUCTURA DE BASE DE DATOS (CORREGIDA)
Dame las tablas CORRECTAS para:

sql
-- Tabla de facturas (cabecera)
facturas (
    id_factura,
    fecha,
    id_cliente,
    subtotal,
    impuestos,
    total,
    estado
)

-- Tabla de DETALLE de facturas (obligatoria)
factura_detalle (
    id_detalle,
    id_factura,  -- relación con facturas
    id_producto,
    nombre_producto,
    cantidad,
    precio_unitario,
    subtotal_linea,  -- cantidad * precio_unitario
    impuesto_linea,
    total_linea
)
Si mi estructura actual no tiene factura_detalle, dame el script SQL para CREARLA y MIGRAR los datos existentes.

PARTE 2: CÓDIGO PARA GUARDAR FACTURA CON TODOS LOS PRODUCTOS
Dame el código COMPLETO (PHP/Node/Python) que:

Recibe el carrito de compras (con 10 productos, por ejemplo)

Guarda UN registro en facturas (cabecera)

Guarda DIEZ registros en factura_detalle (uno por cada producto)

Maneja transacciones (si falla un detalle, no guarda nada)

Genera el PDF con CADA producto en líneas separadas

PARTE 3: CÓDIGO PARA GENERAR PDF CON DETALLE COMPLETO
Dame el código que genere un PDF que muestre:

text
FACTURA #0001
Fecha: 2026-01-15
Cliente: Juan Pérez

------------------------------------------

Producto         Cant   Precio   Subtotal
------------------------------------------

Mouse RGB        2      $25.00   $50.00
Teclado Mecánico 1      $80.00   $80.00
Monitor 24"      1     $200.00  $200.00
(seguir hasta producto 10)
------------------------------------------

Subtotal:              $330.00
Impuestos (19%):       $62.70
TOTAL:                 $392.70
PARTE 4: PANEL DE ADMINISTRACIÓN - REPORTES
Dame el código para el panel admin con:

A) Reporte de ventas por día específico:

Input: seleccionar fecha (ej: 2026-01-15)

Output:

Total vendido ese día: $XXX

Cantidad de facturas: X

Lista de productos vendidos ese día (con cantidades)

Botón para descargar PDF de ese reporte

B) Reporte completo de ventas (todas las facturas):

Mostrar TODAS las facturas ordenadas por fecha (más reciente primero)

Cada factura debe poder expandirse para ver sus productos individuales

Total general de todas las ventas

Botón para exportar a Excel/CSV

Botón para descargar reporte completo en PDF

C) Dashboard rápido con tarjetas:

Ventas de hoy: $XXX

Ventas de este mes: $XXX

Producto más vendido

Número total de facturas

PARTE 5: SOLUCIÓN PARA PDFs QUE NO DESCARGAN
Además de todo lo anterior, incluye la solución para que los PDFs descarguen en producción:

Headers correctos

Manejo de buffers (ob_clean())

Rutas absolutas para logos/assets

Configuración de memoria para PDFs grandes

PARTE 6: SCRIPT DE VERIFICACIÓN
Un script que verifique:

Que todas las facturas tengan su detalle (no hay facturas huérfanas)

Que los totales en cabecera coincidan con la suma de detalles

Que los PDFs se generan correctamente con todos los productos

FORMATO DE RESPUESTA EXIGIDO:
SQL - Creación de tablas y migración (bloque sql)

Código backend - Guardar factura con detalles (bloque php o el lenguaje que uses)

Código PDF - Generar PDF con líneas detalladas (bloque php)

Código admin panel - Reportes y dashboard (bloque html + javascript + php)

Script SQL de verificación - Consultas para comprobar integridad

Checklist de despliegue

EJEMPLO DE LO QUE ESPERO VER EN EL DETALLE DE FACTURA:
php
// Así debe guardarse una compra de 10 productos
foreach ($carrito as $producto) {
    $sql = "INSERT INTO factura_detalle (
        id_factura, id_producto, nombre_producto,
        cantidad, precio_unitario, subtotal_linea
    ) VALUES (
        $idFactura, $producto['id'], $producto['nombre'],
        $producto['cantidad'], $producto['precio'],
        $producto['cantidad'] * $producto['precio']
    )";
    // Ejecutar para CADA UNO de los 10 productos
}
IMPORTANTE - NO TE DESVIES:
NO me des una solución genérica que solo muestre "10 productos x $total"

QUIERO explícitamente que CADA producto tenga su propia línea en la factura y en la BD

En el admin panel QUIERO poder ver "el día X vendí $Y y estos productos específicos"

Si mi código actual no hace esto, dame el código COMPLETO para reemplazarlo.

text

---

## INSTRUCCIONES DE USO

| Paso | Acción |
|------|--------|
| 1 | Abre Antigravity |
| 2 | Selecciona **Gemini 3.5 Flash** |
| 3 | Copia el prompt COMPLETO de arriba |
| 4 | Pega y ejecuta |
| 5 | Aplica TODO el código que te dé |

---

## VARIANTE RÁPIDA (si quieres más corto)

Gemini 3.5 Flash: Necesito facturas que registren CADA producto individualmente (si compro 10 cosas, que salgan 10 líneas en la factura y 10 registros en BD). Además en admin panel quiero: reporte de ventas por día específico (que me diga cuánto vendí ese día y qué productos), reporte completo de ventas exportable a PDF/Excel. También arreglar que los PDFs descargan en local pero no en producción. Dame SQL, código PHP para guardar detalle, código para PDF con líneas individuales, y código para los reportes del admin. No te saltes el detalle de productos.

text

---

## COMANDOS PARA VERIFICAR DESPUÉS

```sql
-- Verificar que cada factura tiene sus detalles
SELECT f.id_factura, COUNT(d.id_detalle) as total_productos
FROM facturas f
LEFT JOIN factura_detalle d ON f.id_factura = d.id_factura
GROUP BY f.id_factura;

-- Ver ventas por día específico
SELECT DATE(fecha) as dia, SUM(total) as total_vendido, COUNT(*) as facturas
FROM facturas
WHERE DATE(fecha) = '2026-01-15'
GROUP BY DATE(fecha);

-- Ver qué productos se vendieron en un día específico
SELECT p.nombre, SUM(d.cantidad) as unidades_vendidas, SUM(d.total_linea) as total
FROM factura_detalle d
JOIN facturas f ON d.id_factura = f.id_factura
WHERE DATE(f.fecha) = '2026-01-15'
GROUP BY p.nombre
ORDER BY unidades_vendidas DESC;
