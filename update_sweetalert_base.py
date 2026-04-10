import re

file_path = 'c:/Users/turca/Desktop/MIKITECH-APP/templates/base.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove old CSS logic
content = re.sub(r'/\* ── TOAST NOTIFICATIONS ── \*/.*?@keyframes toastProgress \{ from \{ width:100%; \} to \{ width:0%; \} \}', '', content, flags=re.DOTALL)

# 2. Add Sweetalert CDN in extra_head or before body
if '<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>' not in content:
    content = content.replace('{% block extra_head %}{% endblock %}', '<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>\n  {% block extra_head %}{% endblock %}')

# 3. Remove old HTML toast container and replace with Sweetalert Logic
old_js_block1 = re.compile(r'<!-- TOAST CONTAINER -->.*?<!-- NAVBAR -->', re.DOTALL)
new_js_block1 = '''<!-- NAVBAR -->'''
content = old_js_block1.sub(new_js_block1, content)

old_js_block2 = re.compile(r'<!-- TOAST JS GLOBAL -->.*?</script>', re.DOTALL)
new_js_block2 = '''<!-- SWEETALERT2 GLOBAL LOGIC -->
  <script>
    const Toast = Swal.mixin({
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 4000,
      timerProgressBar: true,
      background: '#111111',
      color: '#ffffff',
      iconColor: '#1D4ED8',
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    });

    // Mapeo manual para uso en JS frontal (window.toast)
    window.toast = {
      exito:   function(m) { Toast.fire({ icon: 'success', title: m }); },
      error:   function(m) { Toast.fire({ icon: 'error', title: m }); },
      info:    function(m) { Toast.fire({ icon: 'info', title: m }); },
      aviso:   function(m) { Toast.fire({ icon: 'warning', title: m }); }
    };
  </script>

  <!-- DJANGO MESSAGES TO SWEETALERT -->
  {% if messages %}
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      {% for message in messages %}
        var cType = "{{ message.tags }}";
        var sType = 'info';
        if (cType.includes('success')) sType = 'success';
        if (cType.includes('error')) sType = 'error';
        if (cType.includes('warning')) sType = 'warning';
        
        Toast.fire({
          icon: sType,
          title: "{{ message|escapejs }}"
        });
      {% endfor %}
    });
  </script>
  {% endif %}'''
content = old_js_block2.sub(new_js_block2, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("base.html actualizado exitosamente con SweetAlert2")
