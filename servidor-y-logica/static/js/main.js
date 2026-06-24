/**
 * MIKITECH — JavaScript Vanilla Principal
 * Sin innerHTML. Sin alert/confirm. Solo createElement y appendChild.
 * Toasts para feedback visual.
 */

'use strict';

/* === UTILIDADES === */

/** Obtener cookie CSRF de Django */
function getCookie(name) {
  var value = '; ' + document.cookie;
  var parts = value.split('; ' + name + '=');
  if (parts.length === 2) return parts.pop().split(';').shift();
  return '';
}

/** Mostrar toast de feedback visual */
function showToast(type, message) {
  var container = document.getElementById('dynamic-toasts');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    container.id = 'dynamic-toasts';
    container.setAttribute('aria-live', 'assertive');
    document.body.appendChild(container);
  }

  var toast = document.createElement('div');
  toast.className = 'toast toast--' + (type || 'info');
  toast.setAttribute('role', 'alert');

  var span = document.createElement('span');
  span.textContent = message;
  toast.appendChild(span);

  container.appendChild(toast);

  // Auto-remove después de 4 segundos
  setTimeout(function() {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(function() {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 300);
  }, 4000);
}

/* === DROPDOWN DE CATEGORÍAS === */
(function setupDropdown() {
  var btn = document.getElementById('cat-btn');
  var menu = document.getElementById('cat-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', function(e) {
    e.stopPropagation();
    var isOpen = menu.style.opacity === '1';
    menu.style.opacity = isOpen ? '0' : '1';
    menu.style.visibility = isOpen ? 'hidden' : 'visible';
    menu.style.transform = isOpen ? 'translateY(-0.8rem)' : 'translateY(0)';
    btn.setAttribute('aria-expanded', !isOpen);
  });

  document.addEventListener('click', function() {
    menu.style.opacity = '0';
    menu.style.visibility = 'hidden';
    menu.style.transform = 'translateY(-0.8rem)';
    btn.setAttribute('aria-expanded', 'false');
  });
})();

/* === AUTO-CERRAR TOASTS === */
(function autoCloseToasts() {
  var toasts = document.querySelectorAll('.toast');
  toasts.forEach(function(toast) {
    setTimeout(function() {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(100%)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(function() {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, 4000);
  });
})();

/* === BOTONES TOGGLE FAVORITO EN CARD === */
(function setupFavButtons() {
  var favBtns = document.querySelectorAll('.fav-toggle');
  favBtns.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var productId = this.dataset.productId;
      var self = this;

      fetch('/interacciones/favorito/' + productId + '/', {
        method: 'POST',
        headers: { 'X-CSRFToken': getCookie('csrftoken') },
      })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        if (data.error && data.requires_auth) {
          showToast('error', 'Debes iniciar sesión para guardar favoritos.');
          return;
        }
        self.textContent = data.favorited ? '♥' : '♡';
        self.classList.toggle('active', data.favorited);
        self.setAttribute('aria-pressed', data.favorited);
        showToast('success', data.favorited ? '¡Guardado en favoritos!' : 'Eliminado de favoritos');
      })
      .catch(function() {
        showToast('error', 'Error de conexión. Intenta de nuevo.');
      });
    });
  });
})();

/* === VALIDACIÓN DE FORMULARIOS === */
(function setupFormValidation() {
  // Login
  var loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var email = document.getElementById('login-email').value.trim();
      var password = document.getElementById('login-password').value;

      if (!email) { showToast('error', 'Ingresa tu correo electrónico.'); return; }
      if (!password) { showToast('error', 'Ingresa tu contraseña.'); return; }
      if (!/\S+@\S+\.\S+/.test(email)) { showToast('error', 'El correo no es válido.'); return; }

      this.submit();
    });
  }

  // Registro
  var regForm = document.getElementById('register-form');
  if (regForm) {
    regForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var name = document.getElementById('reg-name').value.trim();
      var username = document.getElementById('reg-username').value.trim();
      var email = document.getElementById('reg-email').value.trim();
      var pass = document.getElementById('reg-password').value;
      var pass2 = document.getElementById('reg-password2').value;

      if (!name) { showToast('error', 'Ingresa tu nombre completo.'); return; }
      if (!username || username.length < 3) { showToast('error', 'El usuario debe tener al menos 3 caracteres.'); return; }
      if (!email || !/\S+@\S+\.\S+/.test(email)) { showToast('error', 'El correo no es válido.'); return; }
      if (!pass || pass.length < 6) { showToast('error', 'La contraseña debe tener al menos 6 caracteres.'); return; }
      if (pass !== pass2) { showToast('error', 'Las contraseñas no coinciden.'); return; }

      this.submit();
    });
  }

  // Gateway admin
  var gatewayForm = document.getElementById('gateway-form');
  if (gatewayForm) {
    gatewayForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var code = document.getElementById('gateway-code').value.trim();
      if (!code) { showToast('error', 'Ingresa el código de acceso.'); return; }
      this.submit();
    });
  }
})();

/* === PREVENIR ENVÍO MÚLTIPLE DE FORMULARIOS === */
(function preventDoubleSubmit() {
  var forms = document.querySelectorAll('form');
  forms.forEach(function(form) {
    form.addEventListener('submit', function() {
      var submitBtns = form.querySelectorAll('[type="submit"]');
      submitBtns.forEach(function(btn) {
        btn.disabled = true;
        btn.style.opacity = '0.7';
      });
      // Re-habilitar tras 5 segundos por si falla
      setTimeout(function() {
        submitBtns.forEach(function(btn) {
          btn.disabled = false;
          btn.style.opacity = '1';
        });
      }, 5000);
    });
  });
})();

/* === FILTROS: auto-submit en select === */
(function setupFilterAutoSubmit() {
  var filterSelects = ['filter-category', 'filter-brand', 'filter-sort'];
  filterSelects.forEach(function(id) {
    var el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('change', function() {
      var form = document.getElementById('filter-form');
      if (form) form.submit();
    });
  });
})();

/* === ACCESIBILIDAD: cerrar modal con ESC === */
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    var openDropdowns = document.querySelectorAll('.dropdown__menu');
    openDropdowns.forEach(function(menu) {
      menu.style.opacity = '0';
      menu.style.visibility = 'hidden';
    });
  }
});
