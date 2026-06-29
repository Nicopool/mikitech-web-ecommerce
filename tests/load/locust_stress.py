"""PRUEBAS DE ESTRÉS - Locust
Identifica el punto de quiebre del sistema: cuándo colapsa, cómo responde y cómo se recupera.

Escenarios:
1. Ramp-up progresivo: aumenta usuarios gradualmente hasta encontrar el límite
2. Pico repentino (spike): dispara muchos usuarios de golpe
3. Ciclo carga-recuperación: pico seguido de descanso para medir recuperación

Uso:
    # Ramp-up progresivo hasta 500 usuarios
    locust -f tests/load/locust_stress.py --headless -u 500 -r 10 -t 15m --host=https://tu-app.railway.app

    # Prueba de pico (spike): 200 usuarios en 10 segundos
    locust -f tests/load/locust_stress.py --headless -u 200 -r 20 -t 5m --host=https://tu-app.railway.app

    # Web UI para monitoreo en tiempo real
    locust -f tests/load/locust_stress.py --web-host 0.0.0.0 --host=http://localhost:8000
"""

import random
import time
from locust import HttpUser, task, between, tag, events
from locust.runners import STATE_STOPPING, STATE_STOPPED


class MikitechStressUser(HttpUser):
    """Usuario para pruebas de estrés — peticiones más agresivas."""
    wait_time = between(0.5, 2)

    terminos_busqueda = [
        "amd", "intel", "nvidia", "ssd", "ram",
        "teclado", "monitor", "mouse", "audifonos",
        "fuente", "gabinete", "placa", "disco", "cooler"
    ]

    @tag("critico")
    @task(15)
    def ping(self):
        """Endpoint más liviano — medir throughput máximo."""
        with self.client.get("/ping/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Ping falló: {response.status_code}")
            elif response.elapsed.total_seconds() > 2.0:
                response.failure(f"Ping lento: {response.elapsed.total_seconds():.2f}s")

    @tag("critico")
    @task(10)
    def home(self):
        """Página principal — primer punto de entrada."""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code not in [200, 302]:
                response.failure(f"Home falló: {response.status_code}")
            elif response.elapsed.total_seconds() > 3.0:
                response.failure(f"Home lento: {response.elapsed.total_seconds():.2f}s")

    @tag("pesado")
    @task(8)
    def catalogo(self):
        """Listado de productos — consulta a BD."""
        pagina = random.randint(1, 5)
        with self.client.get(
            f"/productos/?pagina={pagina}",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Catálogo falló: {response.status_code}")
            elif response.elapsed.total_seconds() > 4.0:
                response.failure(f"Catálogo lento: {response.elapsed.total_seconds():.2f}s")

    @tag("pesado")
    @task(6)
    def buscar(self):
        """Búsqueda — consulta pesada con filtros."""
        termino = random.choice(self.terminos_busqueda)
        with self.client.get(
            f"/buscar/?q={termino}",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Búsqueda falló: {response.status_code}")
            elif response.elapsed.total_seconds() > 5.0:
                response.failure(f"Búsqueda lenta: {response.elapsed.total_seconds():.2f}s")

    @tag("pesado")
    @task(4)
    def buscar_con_filtros(self):
        """Búsqueda con múltiples filtros — consulta más pesada."""
        termino = random.choice(self.terminos_busqueda)
        precio_min = random.randint(100000, 500000)
        precio_max = precio_min + random.randint(500000, 3000000)
        with self.client.get(
            f"/buscar/?q={termino}&precio_min={precio_min}&precio_max={precio_max}",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Búsqueda filtrada falló: {response.status_code}")
            elif response.elapsed.total_seconds() > 6.0:
                response.failure(f"Búsqueda filtrada lenta: {response.elapsed.total_seconds():.2f}s")

    @tag("critico")
    @task(3)
    def carrito(self):
        """Carrito — endpoint con sesión."""
        with self.client.get("/carrito/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Carrito falló: {response.status_code}")
            elif response.elapsed.total_seconds() > 3.0:
                response.failure(f"Carrito lento: {response.elapsed.total_seconds():.2f}s")

    @tag("critico")
    @task(2)
    def api_cart_status(self):
        """API de estado del carrito — usado en mini-cart."""
        with self.client.get("/api/cart-status/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Cart-API falló: {response.status_code}")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("[ESTRÉS] Prueba de estrés iniciada")
    print(f"[ESTRÉS] Usuarios máximos: {environment.parsed_options.num_users}")
    print(f"[ESTRÉS] Tasa de spawn: {environment.parsed_options.spawn_rate} usuarios/s")
    print(f"[ESTRÉS] Host: {environment.host}")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    stats = environment.stats
    total_rps = stats.total.current_rps if hasattr(stats.total, 'current_rps') else 0
    fail_ratio = stats.total.fail_ratio if hasattr(stats.total, 'fail_ratio') else 0

    print("\n========== RESUMEN DE PRUEBA DE ESTRÉS ==========")
    print(f"  Total de peticiones: {stats.total.num_requests}")
    print(f"  Fallos: {stats.total.num_failures} ({fail_ratio:.1%})")
    print(f"  Tiempo de respuesta promedio: {stats.total.avg_response_time:.1f}ms")
    print(f"  Percentil 95: {stats.total.get_response_time_percentile(0.95):.0f}ms")
    print(f"  Percentil 99: {stats.total.get_response_time_percentile(0.99):.0f}ms")
    print(f"  Throughput (pico): {stats.total.current_rps:.1f} req/s")
    print(f"  Host: {environment.host}")

    if fail_ratio > 0.10:
        print("  ⚠ CONCLUSIÓN: Sistema degradado o en punto de quiebre (>10% fallos)")
    elif fail_ratio > 0.0:
        print("  ⚠ CONCLUSIÓN: Sistema bajo presión con errores esporádicos")
    else:
        print("  ✓ CONCLUSIÓN: Sistema resistente sin errores bajo esta carga")

    if stats.total.avg_response_time > 2000:
        print("  ⚠ Tiempo de respuesta promedio excede 2s — posible bottleneck")
    print("==================================================\n")
