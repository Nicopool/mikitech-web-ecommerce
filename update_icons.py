import os

mapping = {
    'bi-grid-1x2-fill': 'grid_view',
    'bi-grid-fill': 'grid_view',
    'bi-bag-fill': 'shopping_bag',
    'bi-card-list': 'receipt_long',
    'bi-clock-history': 'history',
    'bi-bar-chart-fill': 'bar_chart',
    'bi-gear-fill': 'settings',
    'bi-person-gear': 'manage_accounts',
    'bi-box-arrow-right': 'logout',
    'bi-hand-wave-fill': 'waving_hand',
    'bi-calendar3': 'calendar_today',
    'bi-bell': 'notifications',
    'bi-gear': 'settings',
    'bi-box-seam-fill': 'inventory_2',
    'bi-star-fill': 'star',
    'bi-bag-check': 'shopping_bag',
    'bi-calendar-event': 'event',
    'bi-cart-x': 'remove_shopping_cart',
    'bi-credit-card-2-back': 'credit_card',
    'bi-heart-fill': 'favorite',
    'bi-star': 'star_border',
    'bi-heart': 'favorite_border',
    'bi-person-badge': 'badge',
    'bi-geo-alt': 'location_on',
    'bi-telephone': 'phone',
    'bi-chat-left-text': 'chat',
    'bi-graph-up': 'trending_up',
    'bi-search': 'search',
}

emoji_map = {
    '🏠': 'home',
    '📦': 'inventory_2',
    '👥': 'group',
    '📂': 'folder',
    '💬': 'chat',
    '📊': 'bar_chart',
    '🔍': 'search',
    '🛒': 'shopping_cart',
    '💳': 'credit_card',
    '⊞': 'grid_view',
    '⚙️': 'settings',
    '↪': 'logout',
    '📋': 'receipt_long'
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    # Replace simple exact matches
    for bi, mat in mapping.items():
        content = content.replace(f'<i class="bi {bi}"></i>', f'<span class="material-symbols-outlined">{mat}</span>')
        # With extra classes at the end
        content = content.replace(f'<i class="bi {bi} text-warning"></i>', f'<span class="material-symbols-outlined text-warning">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} me-1"></i>', f'<span class="material-symbols-outlined me-1">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} ms-1"></i>', f'<span class="material-symbols-outlined ms-1">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-primary me-2"></i>', f'<span class="material-symbols-outlined text-primary me-2">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-muted"></i>', f'<span class="material-symbols-outlined text-muted">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-danger me-2"></i>', f'<span class="material-symbols-outlined text-danger me-2">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-white"></i>', f'<span class="material-symbols-outlined text-white">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-success"></i>', f'<span class="material-symbols-outlined text-success">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-danger"></i>', f'<span class="material-symbols-outlined text-danger">{mat}</span>')
        content = content.replace(f'<i class="bi {bi} text-primary"></i>', f'<span class="material-symbols-outlined text-primary">{mat}</span>')

    for emoji, mat in emoji_map.items():
        content = content.replace(f'<span class="sb-icon">{emoji}</span>', f'<span class="sb-icon"><span class="material-symbols-outlined">{mat}</span></span>')
        content = content.replace(f'<span>{emoji}</span>', f'<span><span class="material-symbols-outlined">{mat}</span></span>')
        content = content.replace(f'<i>{emoji}</i>', f'<span class="material-symbols-outlined">{mat}</span>')
        content = content.replace(f'<h1>{emoji} ', f'<h1><span class="material-symbols-outlined" style="font-size:inherit;">{mat}</span> ')

    if orig != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated " + filepath)

for root, _, files in os.walk('c:/Users/turca/Desktop/MIKITECH-APP/templates'):
    for f in files:
        if f.endswith('.html'):
            fix_file(os.path.join(root, f))
