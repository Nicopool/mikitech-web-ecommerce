import openpyxl
import random
import os

def main():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Productos"

    # Encabezados requeridos por la vista de carga masiva en Django
    columnas = ["NOMBRE", "CATEGORIA", "PRECIO", "STOCK", "MARCA", "DESCRIPCION", "URL_IMAGEN"]
    ws.append(columnas)

    # Listas de datos para generar combinaciones aleatorias de productos tecnológicos de alto rendimiento
    marcas = ["ASUS", "MSI", "Gigabyte", "Corsair", "AMD", "Intel", "NVIDIA", "Western Digital", "Samsung", "Kingston", "Logitech", "Razer"]
    
    categorias = {
        "Procesadores": [
            ("AMD Ryzen 7 7800X3D", "Procesador líder en gaming con tecnología 3D V-Cache."),
            ("Intel Core i9-14900K", "Procesador de 24 núcleos de alto rendimiento para multitarea extrema."),
            ("AMD Ryzen 5 7600X", "Excelente procesador de gama media para juegos y productividad."),
            ("Intel Core i5-14600K", "Gran rendimiento en gaming y edición con núcleos híbridos."),
            ("AMD Ryzen 9 7950X", "Procesador de 16 núcleos ideal para renderizado y desarrollo.")
        ],
        "Tarjetas Gráficas": [
            ("NVIDIA RTX 4090 OC", "La tarjeta gráfica más potente del mercado para 4K y Ray Tracing."),
            ("ASUS ROG Strix RTX 4070 Ti", "Rendimiento premium para gaming competitivo 1440p."),
            ("MSI Gaming Trio RX 7800 XT", "Excelente tarjeta AMD con 16GB de memoria VRAM."),
            ("Gigabyte Windforce RTX 4060", "Tarjeta ideal para gaming a 1080p con bajo consumo."),
            ("NVIDIA RTX 4080 Super", "Potencia de gama entusiasta para realidad virtual y modelado 3D.")
        ],
        "Placas Base": [
            ("ASUS ROG Maximus Z790", "Placa base premium con conectividad PCIe 5.0 y Wi-Fi 7."),
            ("MSI MAG B650 Tomahawk", "La mejor placa base calidad-precio para procesadores AMD Ryzen."),
            ("Gigabyte AORUS X670 Elite", "Robusto sistema de fases y disipación para overclocking AMD."),
            ("ASUS Prime B760-PLUS", "Placa versátil y económica para procesadores Intel Core.")
        ],
        "Memoria RAM": [
            ("Corsair Vengeance DDR5 32GB", "Kit de 2x16GB a 6000MHz de baja latencia con perfiles EXPO."),
            ("Kingston FURY Beast RGB 16GB", "Memoria DDR5 con disipador térmico y luces RGB personalizables."),
            ("G.Skill Trident Z5 Neo 64GB", "Máximo rendimiento de 2x32GB a 6400MHz para profesionales."),
            ("Corsair Dominator Titanium 32GB", "Diseño icónico con los mejores chips integrados para entusiastas.")
        ],
        "Almacenamiento": [
            ("Samsung 990 PRO NVMe 2TB", "SSD M.2 ultra rápido con velocidades de lectura de hasta 7450 MB/s."),
            ("WD Black SN850X 1TB", "Excelente disco con disipador para gaming extremo y consolas."),
            ("Crucial T700 PCIe 5.0 2TB", "Próxima generación de velocidad SSD superando los 12000 MB/s."),
            ("Kingston KC3000 M.2 1TB", "Gran rendimiento a precio competitivo con tecnología PCIe 4.0.")
        ],
        "Fuentes de Poder": [
            ("Corsair RM850x Gold", "Fuente de alimentación modular silenciosa con certificación 80 Plus Gold."),
            ("ASUS ROG Thor 1000W Platinum", "Pantalla OLED integrada y componentes de grado audiófilo."),
            ("MSI MAG A750GL", "Fuente compatible con PCIe 5.0 y conector nativo de 16 pines.")
        ],
        "Gabinetes": [
            ("Lian Li O11 Dynamic EVO", "Diseño modular de doble cámara de vidrio templado ideal para refrigeración."),
            ("Corsair 4000D Airflow", "Gabinete semitorre con flujo de aire optimizado y panel frontal de rejilla."),
            ("NZXT H9 Flow Matte Black", "Vista panorámica espectacular con gran espacio para radiadores de 360mm.")
        ],
        "Refrigeración": [
            ("Corsair iCUE H150i Elite", "Sistema de refrigeración líquida AIO de 360mm con pantalla LCD."),
            ("Noctua NH-D15 chromax.black", "El legendario disipador de aire de doble torre ultra silencioso."),
            ("DeepCool LT720 360mm", "Bomba multidimensional con efecto espejo de infinito de alto rendimiento.")
        ],
        "Monitores": [
            ("ASUS ROG Swift 360Hz", "Monitor gaming de 24.5 pulgadas con tasa de refresco ultra rápida."),
            ("Samsung Odyssey G9 Curvo 49\"", "Monitor ultrawide súper curvo ideal para simulación e inmersión."),
            ("MSI Optix 27\" QHD 165Hz", "El balance perfecto entre resolución QHD y fluidez en juegos."),
            ("LG UltraGear OLED 27\"", "Colores perfectos y tiempo de respuesta de 0.03ms para gaming.")
        ],
        "Periféricos": [
            ("Logitech G502 HERO", "Mouse gamer con sensor HERO 25K y peso ajustable."),
            ("Razer BlackWidow V4 Pro", "Teclado mecánico con switches Green y teclas macro adicionales."),
            ("Corsair HS80 RGB Wireless", "Auriculares de alta fidelidad con audio espacial Dolby Atmos."),
            ("Logitech G Pro X Superlight", "Mouse inalámbrico de solo 63g de peso preferido por profesionales.")
        ]
    }

    # Generamos 40 productos aleatorios sin duplicar el nombre exacto
    nombres_generados = set()
    productos_creados = 0

    while productos_creados < 40:
        cat_nombre, items = random.choice(list(categorias.items()))
        base_nombre, desc = random.choice(items)
        
        # Le añadimos variantes aleatorias para tener variedad de nombres
        marca = random.choice(marcas)
        modelo_num = random.randint(100, 9990)
        nombre_completo = f"{marca} {base_nombre} V-{modelo_num}"
        
        if nombre_completo not in nombres_generados:
            nombres_generados.add(nombre_completo)
            
            # Generar precio razonable (de $120.000 a $4.800.000 COP)
            precio = random.randint(12, 480) * 10000
            
            # Generar existencias/stock aleatorio
            stock = random.randint(5, 75)
            
            # URL de imagen genérica de hardware
            url_img = "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea"
            
            # Fila: NOMBRE, CATEGORIA, PRECIO, STOCK, MARCA, DESCRIPCION, URL_IMAGEN
            fila = [nombre_completo, cat_nombre, precio, stock, marca, desc, url_img]
            ws.append(fila)
            productos_creados += 1

    # Guardar en la ruta de estáticos
    ruta_salida = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'servidor-y-logica',
        'static',
        'plantilla_carga_masiva_mikitech.xlsx'
    )
    
    # Crear la carpeta de salida si no existe
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    wb.save(ruta_salida)
    print(f"[OK] Creado Excel con {productos_creados} productos en: {ruta_salida}")

if __name__ == '__main__':
    main()
