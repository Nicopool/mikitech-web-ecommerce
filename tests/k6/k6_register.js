import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  vus: 5,
  duration: '20s',
};

export default function () {
  // 1. Obtener la página de registro para obtener el token CSRF
  let res = http.get('http://127.0.0.1:8000/cuenta/registro/');
  
  let match = res.body.match(/name="csrfmiddlewaretoken" value="([^"]+)"/);
  let csrfToken = match ? match[1] : '';

  let rand = Math.floor(Math.random() * 1000000);
  let email = `k6_test_${__VU}_${__ITER}_${rand}@mikitech.test`;
  let username = `k6user_${__VU}_${__ITER}_${rand}`;
  
  let payload = {
    csrfmiddlewaretoken: csrfToken,
    nombre_completo: 'Usuario de Pruebas K6',
    nombre_usuario: username,
    correo: email,
    clave: 'SecurePassk6*',
    clave2: 'SecurePassk6*',
    terminos: 'on'
  };
  
  // 2. Enviar el registro
  let resPost = http.post('http://127.0.0.1:8000/cuenta/registro/', payload, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': 'http://127.0.0.1:8000/cuenta/registro/' }
  });
  
  check(resPost, {
    'registro exitoso': (r) => r.status === 200 || r.status === 302,
  });
  
  sleep(1);
}
