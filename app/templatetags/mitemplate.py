from django import template

register = template.Library()

@register.simple_tag
def precio_impuesto(preciocosto, impuesto):
    # you would need to do any localization of the result here
    precio=float(preciocosto)+(float(preciocosto)*(float(impuesto)*0.01))
    return precio 