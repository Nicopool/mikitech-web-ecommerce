"""PRUEBAS DE CARGA - Locust
Simula usuarios reales navegando en la tienda MIKITECH bajo condiciones normales.

Uso:
    locust -f tests/load/locustfile.py --headless -u 50 -r 5 --host=https://tu-app.railway.app
    locust -f tests/load/locustfile.py --web-host 0.0.0.0 --host=http://localhost:8000
"""

import random
from locust import HttpUser, task, between, tag


class MikitechLoadUser(HttpUser):
    """Simula un usuario navegando la tienda en condiciones normales de carga."""
    wait_time = between(2, 5)

    productos_populares = [
        "/productos/",
        "/productos/?orden=precio_asc",
        "/productos/?orden=precio_desc",
        "/productos/?orden=nuevo",
    ]

    terminos_busqueda = [
        "?q=amd",
        "?q=intel",
        "?q=nvidia",
        "?q=ssd",
        "?q=ram",
        "?q=teclado",
        "?q=monitor",
    ]

    def on_start(self):
        """Al iniciar, cada usuario visita la página principal."""
        self.client.get("/")

    @tag("ligero")
    @task(10)
    def ver_inicio(self):
        """Página principal — tarea más frecuente."""
        self.client.get("/")

    @tag("ligero")
    @task(8)
    def ver_ping(self):
        """Endpoint de verificación rápida."""
        self.client.get("/ping/")

    @tag("medio")
    @task(6)
    def ver_catalogo(self):
        """Explorar lista de productos."""
        url = random.choice(self.productos_populares)
        self.client.get(url)

    @tag("medio")
    @task(5)
    def buscar_productos(self):
        """Buscar productos por término."""
        url = f"/buscar/{random.choice(self.terminos_busqueda)}"
        self.client.get(url)

    @tag("pesado")
    @task(4)
    def ver_detalle_producto(self):
        """Ver detalle de un producto específico."""
        self.client.get("/productos/")
        self.client.get("/productos/?orden=precio_asc")

    @tag("medio")
    @task(3)
    def ver_carrito(self):
        """Ver el carrito de compras."""
        self.client.get("/carrito/")

    @tag("pesado")
    @task(2)
    def ver_categoria(self):
        """Navegar por categoría (simulando selección)."""
        self.client.get("/buscar/?categoria=procesadores")
        self.client.get("/buscar/?categoria=tarjetas-graficas")
        self.client.get("/buscar/?categoria=almacenamiento")

    @tag("pesado")
    @task(2)
    def filtrar_por_precio(self):
        """Filtrar productos por rango de precio."""
        precio_min = random.randint(100000, 500000)
        precio_max = precio_min + random.randint(500000, 2000000)
        self.client.get(f"/buscar/?precio_min={precio_min}&precio_max={precio_max}")

    @tag("pesado")
    @task(1)
    def ver_ofertas(self):
        """Ver productos en oferta."""
        self.client.get("/buscar/?oferta=true")

    @tag("critico")
    @task(1)
    def flujo_completo(self):
        """Simula un usuario real: inicio -> catálogo -> detalle -> carrito."""
        self.client.get("/")
        self.client.get("/productos/")
        self.client.get("/productos/?orden=precio_desc")
        self.client.get("/carrito/")
