from django import template
import locale

register = template.Library()


@register.filter(name='cop_format')
def cop_format(value):
    """
    Formatea un número con el estilo de pesos colombianos:
    - Punto (.) como separador de miles
    - Sin decimales para precios enteros (COP no usa centavos)
    Ejemplo: 1250000 → 1.250.000
    """
    try:
        value = int(round(float(value)))
        formatted = f"{value:,}".replace(",", ".")
        return formatted
    except (ValueError, TypeError):
        return value


@register.filter(name='currency_cop')
def currency_cop(value):
    """
    Formatea un precio como moneda colombiana completa.
    Ejemplo: 231280.00 → $ 231.280
    Ejemplo: 5977400   → $ 5.977.400
    """
    try:
        # Convertir a entero (COP no usa centavos en precios de tienda)
        value = int(round(float(value)))
        # Formatear con punto como separador de miles (estilo colombiano)
        formatted = f"{value:,}".replace(",", ".")
        return f"$ {formatted}"
    except (ValueError, TypeError):
        return value
