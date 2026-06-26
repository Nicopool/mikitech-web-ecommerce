import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 20 },  // Carga inicial normal
    { duration: '30s', target: 50 },  // Carga moderada
    { duration: '30s', target: 80 },  // Carga alta (límite anterior de runserver)
    { duration: '30s', target: 100 }, // Estrés máximo en Waitress
    { duration: '15s', target: 0 },   // Enfriamiento a 0 usuarios
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],   // Aceptar hasta 5% de fallos en nivel de estrés crítico
  }
};

export default function () {
  let res = http.get('http://127.0.0.1:8000/productos/');
  check(res, { 'catalogo status 200': (r) => r.status === 200 });
  sleep(1);
}
