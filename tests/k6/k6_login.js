import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  vus: 5,
  duration: '20s',
};

export default function () {
  // 1. Obtener la página de ingreso para extraer el token CSRF
  let res = http.get('http://127.0.0.1:8000/cuenta/ingreso/');
  
  let match = res.body.match(/name="csrfmiddlewaretoken" value="([^"]+)"/);
  let csrfToken = match ? match[1] : '';

  let payload = {
    csrfmiddlewaretoken: csrfToken,
    correo: 'admin@mikitech.com',
    clave: 'AdminMiki2026*',
    recordarme: 'on'
  };
  
  // 2. Enviar el login
  let resPost = http.post('http://127.0.0.1:8000/cuenta/ingreso/', payload, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': 'http://127.0.0.1:8000/cuenta/ingreso/' }
  });
  
  check(resPost, {
    'login exitoso o redireccion': (r) => r.status === 200 || r.status === 302,
  });
  
  sleep(1);
}
