from django import template
from django.contrib.auth.models import User

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

@register.filter(name='get_profile_pic')
def get_profile_pic(user_string):
	try:
		u = User.objects.get(username=user_string)
	except:
		return str("imgs/thumb.png")
	return str(u.profile.user_avatar)