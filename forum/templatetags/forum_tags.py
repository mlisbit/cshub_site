from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='encode_name')
def encode_name(my_string):
   return str(my_string).replace (" ", ".ws.").replace ("?", ".qm.").replace ("/", ".fs.").replace ("\\", ".bs.")

