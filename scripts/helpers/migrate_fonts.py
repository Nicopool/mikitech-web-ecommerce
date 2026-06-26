"""
Script de migración tipográfica: Unifica todas las fuentes a Inter.
Reemplaza: Jost, Oswald, Roboto, Plus Jakarta Sans → Inter
"""
import os
import re

# Pares (patrón regex, reemplazo)
REPLACEMENTS = [
    # font-family declarations con comillas simples
    (r"font-family:\s*'Jost'\s*,\s*sans-serif", "font-family: 'Inter', sans-serif"),
    (r"font-family:\s*'Oswald'\s*,\s*sans-serif", "font-family: 'Inter', sans-serif"),
    (r"font-family:\s*'Roboto'\s*,\s*sans-serif", "font-family: 'Inter', sans-serif"),
    (r"font-family:\s*'Plus Jakarta Sans'\s*,\s*sans-serif", "font-family: 'Inter', sans-serif"),
    (r"font-family:\s*'Oswald'\s*,\s*'Inter'\s*,\s*sans-serif", "font-family: 'Inter', sans-serif"),
    # font-family en atributos style inline (sin espacio después de :)
    (r"font-family:'Jost'\s*,\s*sans-serif", "font-family:'Inter', sans-serif"),
    (r"font-family:'Oswald'\s*,\s*sans-serif", "font-family:'Inter', sans-serif"),
    (r"font-family:'Roboto'\s*,\s*sans-serif", "font-family:'Inter', sans-serif"),
    (r"font-family:'Plus Jakarta Sans'\s*,\s*sans-serif", "font-family:'Inter', sans-serif"),
    # Referencias sueltas de nombre de fuente (en listas, fallbacks, etc.)
    (r"'Jost'\s*,\s*sans-serif", "'Inter', sans-serif"),
    (r"'Oswald'\s*,\s*sans-serif", "'Inter', sans-serif"),
    (r"'Plus Jakarta Sans'\s*,\s*sans-serif", "'Inter', sans-serif"),
]

# Reemplazos de URLs de Google Fonts (líneas completas de @import / <link>)
FONT_URL_REPLACEMENTS = [
    # Reemplaza cualquier combinación de Jost+Oswald en Google Fonts URL
    (
        r'family=Oswald:[^&"\s]*&?',
        ''  # eliminar Oswald del query string
    ),
    (
        r'family=Jost:[^&"\s]*&?',
        ''  # eliminar Jost del query string
    ),
    (
        r'family=Plus\+Jakarta\+Sans:[^&"\s]*&?',
        ''  # eliminar Plus Jakarta Sans
    ),
    (
        r'family=Roboto:[^&"\s]*&?',
        ''  # eliminar Roboto standalone
    ),
]

SKIP_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'migrations'}
EXTENSIONS = ('.html', '.css')

updated = []
errors = []

# Walk from project root
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fname in files:
        if not fname.endswith(EXTENSIONS):
            continue
        path = os.path.join(root, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                original = f.read()

            modified = original

            # Aplicar reemplazos de font-family
            for pattern, replacement in REPLACEMENTS:
                modified = re.sub(pattern, replacement, modified)

            # Limpiar URLs de Google Fonts
            for pattern, replacement in FONT_URL_REPLACEMENTS:
                modified = re.sub(pattern, replacement, modified)

            # Limpiar artefactos como & al final de URLs de Google Fonts
            modified = re.sub(r'(\?)[&]+', r'\1', modified)
            modified = re.sub(r'([&])[&]+', r'&', modified)
            modified = re.sub(r'[&]+"', '"', modified)
            modified = re.sub(r"[&]+'", "'", modified)

            if modified != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(modified)
                updated.append(path)
                print(f"UPDATED: {fname}")
            
        except Exception as e:
            errors.append(f"{fname}: {e}")
            print(f"ERROR {fname}: {e}")

print(f"\n{'='*50}")
print(f"Total archivos actualizados: {len(updated)}")
if errors:
    print(f"Errores: {errors}")
print("DONE")
