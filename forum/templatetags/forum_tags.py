from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='trade_spaces')
def trade_spaces(my_string):
   return str(my_string).replace (" ", "_").replace ("?", ".qm.")

