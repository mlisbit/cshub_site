from django.shortcuts import render


import base64
import hmac
import hashlib
import urllib
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.conf import settings

@login_required
def sso(request):
	if None in [settings.DISCOURSE_SSO_SECRET, settings.DISCOURSE_BASE_URL]:
		return HttpResponseForbidden('SSO is not enabled in site configuration.')
	
	payload = request.GET.get('sso')
	signature = request.GET.get('sig')

	if None in [payload, signature]:
		return HttpResponseBadRequest('No SSO payload or signature.')

	## Validate the payload

	try:
		payload = urllib.unquote(payload)
		assert 'nonce' in base64.decodestring(payload)
		assert len(payload) > 0
	except AssertionError:
		return HttpResponseBadRequest('Invalid payload..')

	key = settings.DISCOURSE_SSO_SECRET
	h = hmac.new(key, payload, digestmod=hashlib.sha256)
	this_signature = h.hexdigest()

	if this_signature != signature:
		return HttpResponseBadRequest('Payload does not match signature.')

	## Build the return payload

	params = {
		'nonce': base64.decodestring(payload).split('=')[1],
		'email': request.user.email,
		'external_id': request.user.id,
		'username': request.user.username
	}

	if request.user.first_name and request.user.last_name:
		params['name'] = '%s %s' %(request.user.first_name, request.user.last_name)

	if request.user.profile.user_avatar.name:
		params['avatar_url'] = request.build_absolute_uri('/static/' + request.user.profile.user_avatar.url)
	#return HttpResponse(json.dumps(params))
	return_payload = base64.encodestring(urllib.urlencode(params))
	h = hmac.new(key, return_payload, digestmod=hashlib.sha256)
	query_string = urllib.urlencode({'sso': return_payload, 'sig': h.hexdigest()})

	## Redirect back to Discourse

	url = '%s/session/sso_login' % settings.DISCOURSE_BASE_URL
	return HttpResponseRedirect('%s?%s' % (url, query_string))