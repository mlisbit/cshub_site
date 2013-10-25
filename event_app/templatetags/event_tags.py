from django import template

register = template.Library()

@register.filter(name='get_count')
def number_going(array_of):
   return len(array_of)


@register.filter(name='get_user_entry')
def number_going(username):
   return str("<Going: "+username+">")

@register.filter(name='to_string')
def number_going(thing):
   return str(thing)