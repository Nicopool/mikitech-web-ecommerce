from django import template
import locale

register = template.Library()


@register.filter(name='cop_format')
def cop_format(value):
    """
    Formatea un número con el estilo colombiano:
    - Punto (.) como separador de miles
    - Sin decimales
    Ejemplo: 1250000 → 1.250.000
    """
    try:
        if value is None: return "0"
        value = int(round(float(value)))
        # Formato con punto colombiano
        return "{:,}".format(value).replace(",", ".")
    except (ValueError, TypeError):
        return value


@register.filter(name='currency_cop')
def currency_cop(value):
    """
    Formatea un precio como moneda colombiana.
    Ejemplo: 2199900 → $2.199.900
    """
    try:
        if value is None: return "$0"
        val = int(round(float(value)))
        formatted = "{:,}".format(val).replace(",", ".")
        return f"${formatted}"
    except (ValueError, TypeError):
        return value


@register.filter(name='precio_con_descuento')
def precio_con_descuento(value, porcentaje):
    """Calcula el precio con descuento aplicado."""
    try:
        val = float(value)
        desc = float(porcentaje)
        resultado = val * (1 - desc / 100)
        return int(round(resultado))
    except (ValueError, TypeError):
        return value
@register.filter(name='modulo')
def modulo(num, val):
    """Retorna el residuo de una división."""
    try:
        return int(num) % int(val)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0
