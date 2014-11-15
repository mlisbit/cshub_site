from django import template
from django.contrib.auth.models import User
from userprofile.models import UserProfile

register = template.Library()

@register.filter(name='trade_spaces')
def trade_spaces(my_string):
   return str(my_string).replace (" ", "_").replace ("?", ".qm.")

@register.filter(name='get_avatar')
def get_avatar(my_string):
   return str(my_string).replace (" ", "_").replace ("?", ".qm.")

