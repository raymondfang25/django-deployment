from django import template

register = template.Library()

@register.filter(name='remove')
def remove(value, arg):
    """
    Cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')
