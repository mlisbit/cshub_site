from django import template
from django.contrib.auth.models import User
import json

register = template.Library()

#returns the posotions of the inputted user
@register.filter(name='get_positions')
def number_going(user):
   return User.objects.get(username=user).profile.club_position.all()

#will return a clean array of all the positions
@register.filter(name='clean_positions')
def number_going(user_positions):
	m = []
	for i in user_positions:
		m.append(str(i))
	return m