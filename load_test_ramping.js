import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 10 },   // subir a 10 VUs en 1 min
    { duration: '1m', target: 30 },   // subir a 30 VUs
    { duration: '1m', target: 60 },   // subir a 60 VUs
    { duration: '1m', target: 90 },   // subir a 90 VUs
    { duration: '30s', target: 0 },   // reducir a 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.02'],
  },
};

export default function () {
  const res = http.get('http://127.0.0.1:8000/ping/');
  check(res, {
    'status 200': (r) => r.status === 200,
  });
  sleep(1);
}
