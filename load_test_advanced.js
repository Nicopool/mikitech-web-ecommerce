import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  vus: 20,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<200'],  // 95% de peticiones < 200ms
    http_req_failed: ['rate<0.01'],    // menos del 1% de fallos
  },
};

export default function () {
  const res = http.get('http://127.0.0.1:8000/ping/');
  check(res, {
    'status 200': (r) => r.status === 200,
  });
  sleep(1);
}
