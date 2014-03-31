from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response 
from django.views.generic.base import TemplateView
#from article.models import Article 
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
#registration imports
from forms import MyRegistrationForm, ContactForm
from models import OfficeHours, Notification, BannerImages
from userprofile.models import UserProfile
from django.views.decorators.cache import cache_page

from django.core.mail import send_mail

from django.conf import settings

from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives 

import json
import random

#encode to json
from django.core import serializers
from itertools import chain



def home(request):
	args= {}
	args['users'] = User.objects.all()
	#args['debug'] = settings.DEBUG
	args['images'] = BannerImages.objects.all()[:3]
	args['total_users'] = User.objects.all().__len__
	args['notifications'] = Notification.objects.all()
	args['json_time'] = serializers.serialize("json", UserProfile.objects.all(), fields=('user', 'twitter_link', 'github_link', 'facebook_link', 'linkedin_link'), relations={'user':{'fields':('username','first_name', 'last_name')}})
	args.update(csrf(request))
	return render_to_response('home.html', args, context_instance=RequestContext(request))

#graph members and social accounts with sigma
def graph(request):
	args= {}
	#serializes all desired fields :)
	args['json_time'] = serializers.serialize("json", UserProfile.objects.all(), fields=('user', 'twitter_link', 'github_link', 'facebook_link', 'linkedin_link'), relations={'user':{'fields':('username','first_name', 'last_name')}})
	return render_to_response('graph.html', args, context_instance=RequestContext(request))

def login(request):
	args= {}
	args.update(csrf(request))
	return render_to_response('login.html', args, context_instance=RequestContext(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username}, context_instance=RequestContext(request))

def invalid_login(request):
	return render_to_response('invalid_login.html', {}, context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html', {}, context_instance=RequestContext(request))

def register_success(request):
	return render_to_response('register_success.html', context_instance=RequestContext(request))

def faq_view(request):
	return render_to_response('faq.html', {}, context_instance=RequestContext(request))

def about_site(request):
	return render_to_response('about-site.html', {}, context_instance=RequestContext(request))

#@cache_page(60 * 5)
def view_contact(request):
	args = {}
	args.update(csrf(request))
	success = False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		contact_form = ContactForm(request.POST)

		if contact_form.is_valid():
			success = True
			email = contact_form.cleaned_data['email']
			title = contact_form.cleaned_data['title']
			text = contact_form.cleaned_data['text']

			send_mail(title, text + "\nemail: " + email, email, settings.EMAIL_TO, fail_silently=False)
		
			if request.is_ajax():
				return HttpResponse('OK')


		else:
			if request.is_ajax():
				errors_dict = {}
				
				for error in contact_form.errors:
					e = contact_form.errors[error]
					errors_dict[error] = unicode(e)

				return HttpResponseBadRequest(json.dumps(errors_dict))
	else:
		contact_form = ContactForm()

	try:
		args['office_hours'] = OfficeHours.objects.get(id=1);
	except: 
		pass
	args['contact_form'] = contact_form
	args['email'] = email
	args['title'] = title
	args['text'] = text
	args['success'] = success

	return render_to_response('contact.html', args, context_instance=RequestContext(request))

#@cache_page(60 * 5)
def register_user(request):
	if request.method == 'POST':
		registration_form = MyRegistrationForm(request.POST)
		#non-successful profile update
		#registration success
		if registration_form.is_valid():
			registration_form.save()
			send_mail('NEW USER SIGNUP', registration_form.cleaned_data['username'], 'newuser@example.com', ['mlisbit@gmail.com'], fail_silently=False)

			if request.is_ajax():
				return HttpResponse('OK')
			else:
				return HttpResponseRedirect('/accounts/register_success')
		else:
			if request.is_ajax():
				errors_dict = {}
				for error in registration_form.errors:
					e = registration_form.errors[error]
					errors_dict[error] = unicode(e)

				return HttpResponseBadRequest(json.dumps(errors_dict))
	else:
		registration_form = MyRegistrationForm()

	args = {}
	args.update(csrf(request))

	args['form'] = registration_form;

	return render_to_response('register.html', args, context_instance=RequestContext(request))

def reset_password_view(request):
	args = {}
	if request.user.is_superuser or request.user.is_staff:
		args['super'] = True

	if request.method == "POST":
		#this if intentionally meant to fail for testing right now
		if request.user.is_superuser or request.user.is_staff:
			return HttpResponse('No, no reset for you! you are staff.')
		else:
			email = request.POST['email_reset']
			if email_exists(email):
				print "send that email."
				if cache.get(email):
					print cache.get(email)
					return HttpResponse('You have already requested an email change, please check your email.')
				else: 
					reset_token = random.randint(1,999999999999999)
					cache.set(email, str(reset_token) , 9999)
					html_content="<b>York University Computing Students Hub</b><br><a href='http://www.cshub.ca/resetpass/"+str(email)+"/"+str(reset_token)+"'>Click here to reset your password</a>"
					msg = EmailMultiAlternatives("[cshub] password change request.", '', '', [email])
					msg.attach_alternative(html_content, "text/html")
					msg.send()
					return HttpResponse(str('Email sent'))
			else: 
				return HttpResponse('Invalid Email')
			
	else:
		return render_to_response('reset_password_view.html', args, context_instance=RequestContext(request))

def email_exists(e):
	try:
		u = User.objects.get(email=e)
	except:
		return False
	if u.is_superuser or u.is_staff:
		return False
	return True

def reset_password_edit(request, email_reset_email, email_reset_id):
	#if the token matches the email, allow reset. 
	if cache.get(email_reset_email) == email_reset_id:
		args = {}
		args['email'] = email_reset_email
		args['token'] = email_reset_id
		if request.POST:
			if request.POST['new_pass'] == request.POST['confirm_new_pass']:
				u = User.objects.get(email=email_reset_email)
				u.set_password(request.POST['new_pass'])
				u.save()
				return HttpResponse('Password Successfully reset')
			else:
				return HttpResponse('Password\'s didn\'t match :( ')
		else:
			return render_to_response('reset_password_edit.html', args, context_instance=RequestContext(request))
	else:
		return HttpResponse("Invalid arguements. If you continue to have problems, please send another password reset request.")

#only cache when not debugging
if not settings.DEBUG:
	view_contact = cache_page(60 * 5)(view_contact)
	register_user = cache_page(60 * 5)(register_user)