import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  vus: 20,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<300'], // El 95% de las peticiones deben tardar menos de 300ms
    http_req_failed: ['rate<0.01'],   // Tasa de fallos menor al 1%
  }
};

export default function () {
  let res1 = http.get('http://127.0.0.1:8000/');
  check(res1, { 'home status 200': (r) => r.status === 200 });
  sleep(1);

  let res2 = http.get('http://127.0.0.1:8000/productos/');
  check(res2, { 'catalogo status 200': (r) => r.status === 200 });
  sleep(1);
}
