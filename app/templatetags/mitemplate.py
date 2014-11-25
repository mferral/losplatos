from django import template

register = template.Library()

@register.simple_tag
def precio_impuesto(preciocosto, impuesto):
    # you would need to do any localization of the result here
    precio=float(preciocosto)+(float(preciocosto)*(float(impuesto)*0.01))
    return '%.2f' % precio

@register.simple_tag
def multiplica(cantidad, precio):
    preciototal=float(cantidad)*float(precio)
    return preciototal

@register.simple_tag
def porcentaje_ganancia(pventa, pcosto, impuesto):
    precio=float(pcosto)+(float(pcosto)*(float(impuesto)*0.01))
    ganancia=float(pventa)-float(precio)
    pganancia=(float(ganancia)*100)/float(pventa)
    return int(pganancia)
