# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response 
from django.views.generic.base import TemplateView
#import the models.
from models import Event 
from django.http import HttpResponseRedirect
from django.template import RequestContext

from forms import CommentForm, GoingForm
from event_app.models import Comment, Going
from django.core.context_processors import csrf 
from django.utils import timezone 
from datetime import datetime
from django.core.cache import cache
import time


def listings(request):
	args = {}

	events = cache.get('EVENT_LISTING_KEY')
	if not events:
		events = Event.objects.all().exclude(when__lte=datetime.now()).order_by('when')
		cache.set('EVENT_LISTING_KEY', events, 5)

	args['event_list'] = events
	return render_to_response('listings.html', args , context_instance=RequestContext(request))

def past_listings(request):
	args = {}
	events = cache.get('EVENT_LISTING_KEY')
	if not events:
		events = args['event_list'] = Event.objects.all().exclude(when__gte=datetime.now()).order_by('when')[::-1]
		cache.set('EVENT_LISTING_KEY', events, 30)
	
	args['event_list'] = events
	return render_to_response('past_listings.html', args , context_instance=RequestContext(request))

def listing(request, event_id=1):

	args = {}
	args.update(csrf(request))

	args['form'] = CommentForm()
	args['event'] = Event.objects.get(id=event_id)

	return render_to_response('listing.html', args, context_instance=RequestContext(request))

def going_to(request, event_id):
	e = Event.objects.get(id=event_id)
	
	if request.method == "POST":

		f = GoingForm(request.POST)
		if f.is_valid():
			#check if the user is already in the db of people going.

			test = ': '+event_id+','
			if test in str(Going.objects.all().filter(username=request.user.username).values()):
				print "the bitch was found"
				Going.objects.get(event_id=event_id, username=request.user.username).delete()
			else:
				c = f.save(commit=False)
				c.pub_date = timezone.now()
				c.username = request.user.username
				c.event = e
				c.save()

			return HttpResponseRedirect('/events/get/%s' % event_id)

	else:
		f = GoingForm()

	args = {}
	args.update(csrf(request))

	args['event'] = e

	return render_to_response('listing.html', args, context_instance=RequestContext(request))

def add_comment(request, event_id):
	e = Event.objects.get(id=event_id)

	if request.method == "POST":
		f = CommentForm(request.POST)

		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.username = request.user.username
			c.event = e
			c.save()
			return HttpResponseRedirect('/events/get/%s' % event_id)

	else:
		f = CommentForm()

	args = {}
	args.update(csrf(request))

	args['event'] = e
	args['form'] = f

	return render_to_response('listing.html', args, context_instance=RequestContext(request))


def see_going(request):
	pass 


