from django import template
import locale

register = template.Library()


@register.filter(name='cop_format')
def cop_format(value):
    """
    Formatea un número con el estilo americano:
    - Coma (,) como separador de miles
    - Sin decimales
    Ejemplo: 1250000 → 1,250,000
    """
    try:
        if value is None: return "0"
        value = int(round(float(value)))
        return "{:,}".format(value)
    except (ValueError, TypeError):
        return value


@register.filter(name='currency_cop')
def currency_cop(value):
    """
    Formatea un precio como moneda con estilo Americano.
    Ejemplo: 231280.00 → $231,280.00 COP
    """
    try:
        if value is None: return "$0.00 COP"
        val = float(value)
        # Formateo estándar americano: comas para miles, punto para decimales
        formatted = "{:,.2f}".format(val)
        return f"${formatted} COP"
    except (ValueError, TypeError):
        return value
