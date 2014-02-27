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

@register.filter(name='has_social_account')
def has_social_account(user):
	u = User.objects.get(username=user).profile
	if u.github_link or u.linkedin_link or u.twitter_link or u.facebook_link:
		return True
	return False

@register.filter(name='has_badges')
def has_badges(user):
	u = User.objects.get(username=user).profile.club_position.all()
	if u:
		return True
	return False