from locust import HttpUser, task, between

class MikitechUser(HttpUser):
    # Tiempo de espera aleatorio entre tareas de 1 a 3 segundos
    wait_time = between(1, 3)

    @task(5)
    def test_ping(self):
        """Prueba básica del endpoint de verificación rápida (liviano)"""
        self.client.get("/ping/")

    @task(3)
    def test_home(self):
        """Simula usuario entrando a la página principal de la tienda"""
        self.client.get("/")

    @task(2)
    def test_catalog(self):
        """Simula usuario explorando la lista de productos tecnológicos"""
        self.client.get("/productos/")

    @task(1)
    def test_cart(self):
        """Simula usuario ingresando a ver su carrito de compras"""
        self.client.get("/carrito/")
