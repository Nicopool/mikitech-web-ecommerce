import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  vus: 10,
  duration: '30s',
};

export default function () {
  const payload = JSON.stringify({
    correo: `test${__VU}@test.com`,
    codigo: '1234'
  });
  
  const res = http.post('http://127.0.0.1:8000/verificar/', payload, {
    headers: { 'Content-Type': 'application/json' },
  });
  
  check(res, {
    'status 200 o 400': (r) => r.status === 200 || r.status === 400,
  });
  
  sleep(1);
}
