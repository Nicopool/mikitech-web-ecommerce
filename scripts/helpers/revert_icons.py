import os

file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'templates/users/profile.html')
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<script src="https://unpkg.com/@phosphor-icons/web"></script>': '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">',
    
    # Sidebar
    'ph-fill ph-squares-four': 'bi bi-grid-1x2-fill',
    'ph-fill ph-shopping-bag': 'bi bi-bag-fill',
    'ph-fill ph-receipt': 'bi bi-card-list',
    'ph-fill ph-clock-counter-clockwise': 'bi bi-clock-history',
    'ph-fill ph-file-pdf': 'bi bi-file-earmark-bar-graph-fill',
    'ph-fill ph-gear': 'bi bi-gear-fill',
    'ph ph-sign-out': 'bi bi-box-arrow-right',
    
    # Topbar
    'ph-fill ph-hand-waving text-warning': 'bi bi-hand-wave-fill text-warning',
    'ph ph-calendar-blank': 'bi bi-calendar3',
    'ph ph-bell': 'bi bi-bell',
    'ph ph-gear': 'bi bi-gear',
    
    # Overview
    'ph-fill ph-package': 'bi bi-box-seam-fill',
    'ph-fill ph-star': 'bi bi-star-fill',
    
    # Pedidos
    'ph-fill ph-package text-primary me-2': 'bi bi-box2-fill text-primary me-2',
    'ph ph-shopping-bag': 'bi bi-bag-check',
    'ph ph-calendar': 'bi bi-calendar-event',
    'ph ph-shopping-cart text-muted': 'bi bi-cart-x text-muted',
    
    # Reseñas
    'ph-fill ph-star text-warning me-2': 'bi bi-star-fill text-warning me-2',
    'ph ph-package': 'bi bi-box',
    'ph ph-note-pencil text-muted': 'bi bi-pencil-square text-muted',
    
    # Credit Card
    'ph-fill ph-credit-card text-white': 'bi bi-credit-card-2-back text-white',
    
    # Favoritos
    'ph-fill ph-heart text-danger me-2': 'bi bi-heart-fill text-danger me-2',
    'ph ph-star': 'bi bi-star',
    'ph ph-heart text-muted': 'bi bi-heart text-muted',
    
    # Profile Info
    'ph-fill ph-identification-card text-primary me-2': 'bi bi-person-badge text-primary me-2',
    'ph-fill ph-map-pin text-danger': 'bi bi-geo-alt text-danger',
    'ph-fill ph-phone text-success': 'bi bi-telephone text-success',
    'ph-fill ph-chat-circle-text text-primary': 'bi bi-chat-left-text text-primary',
    
    # JS Error
    'ph ph-trend-up text-muted': 'bi bi-graph-up text-muted'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Iconos revertidos a Bootstrap.")
