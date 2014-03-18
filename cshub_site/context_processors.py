def debug(request):
	from django.conf import settings
	return {'debug': settings.DEBUG}