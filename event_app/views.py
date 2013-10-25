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

def listings(request):
	args = {}
	args['Events'] = Event.objects.all()
	return render_to_response('listings.html', args , context_instance=RequestContext(request))

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
			isGoing = False
			for i in Going.objects.all():
				if request.user.username == i.username:
					isGoing = True

			if not isGoing:
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

'''
oh so very bad hack
def going_to_event(request, event_id=1):
	if event_id:
		a = Event.objects.get(id=event_id)
		#u = User.objects.get(username=request.user.username) 

		modified_username = '_'+request.user.username+'_'
		if modified_username in a.attending:		
			a.going -= 1 
			a.attending = a.attending.replace(modified_username, '')
			a.save()
			return HttpResponseRedirect('/events/')
		else:
			a.going += 1 
			a.attending += modified_username
			a.save()
	return HttpResponseRedirect('/events/')

def maybe_to_event(request):
	pass
'''

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


