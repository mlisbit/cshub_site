from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    try:
    	if re.search(pattern, request.path):
        	return 'active'
    except: 
    	pass
    return ''