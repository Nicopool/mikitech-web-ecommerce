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


@register.filter(name='fecha_relativa')
def fecha_relativa(value):
    """
    Retorna la fecha en formato relativo amigable en español:
    - Hoy
    - Ayer
    - El lunes, El martes, etc. (si es de la última semana)
    - dd Mes yyyy (si es anterior)
    """
    from django.utils import timezone
    import datetime
    
    if not value:
        return ""
    
    try:
        # Comparar fechas locales de Django
        local_fecha = timezone.localtime(value).date()
        local_ahora = timezone.localtime(timezone.now()).date()
        
        diferencia = (local_ahora - local_fecha).days
        
        if diferencia == 0:
            return "Hoy"
        elif diferencia == 1:
            return "Ayer"
        elif 1 < diferencia < 7:
            dias_semana = {
                0: "El lunes",
                1: "El martes",
                2: "El miércoles",
                3: "El jueves",
                4: "El viernes",
                5: "El sábado",
                6: "El domingo"
            }
            return dias_semana.get(local_fecha.weekday(), "")
        else:
            meses = {
                1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
                7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"
            }
            return f"{local_fecha.day} {meses.get(local_fecha.month, '')} {local_fecha.year}"
    except Exception:
        return value

