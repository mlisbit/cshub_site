from django import template

register = template.Library()

@register.filter(name='number_going')
def number_going(array_of):
   return len(array_of)
