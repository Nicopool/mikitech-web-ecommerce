import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  stages: [
    { duration: '20s', target: 60 }, // Pico rápido de 60 usuarios concurrentes
    { duration: '20s', target: 20 }, // Bajada rápida (mitigación de tráfico)
    { duration: '20s', target: 20 }, // Carga estabilizada residual
  ],
  thresholds: {
    http_req_duration: ['p(95)<150'], // Verificar que tras la mitigación el tiempo de respuesta regrese a <150ms
  }
};

export default function () {
  let res = http.get('http://127.0.0.1:8000/ping/');
  check(res, { 'ping status 200': (r) => r.status === 200 });
  sleep(1);
}
