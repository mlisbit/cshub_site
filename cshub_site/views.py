from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response 
from django.views.generic.base import TemplateView
#from article.models import Article 
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
#registration imports
from forms import MyRegistrationForm, ContactForm
from models import OfficeHours, Notification

from django.core.mail import send_mail

from django.conf import settings

#password reset
from django.contrib.auth.views import password_reset

from django.contrib.auth.models import User

def home(request):
	args= {}
	args['users'] = User.objects.all()
	args['total_users'] = User.objects.all().__len__
	args['notifications'] = Notification.objects.all()
	args.update(csrf(request))
	return render_to_response('home.html', args, context_instance=RequestContext(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

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
	
def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		#non-successful profile update
		#registration success
		if form.is_valid():
			form.save()
			send_mail('NEW USER SIGNUP', form.cleaned_data['username'], 'newuser@example.com', ['mlisbit@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/accounts/register_success')
	else:
		form = MyRegistrationForm()
	args = {}
	args.update(csrf(request))

	args['form'] = form;

	return render_to_response('register.html', args, context_instance=RequestContext(request))

def register_success(request):
	return render_to_response('register_success.html')

def faq_view(request):
	return render_to_response('faq.html', {}, context_instance=RequestContext(request))

def about_site(request):
	return render_to_response('about-site.html', {}, context_instance=RequestContext(request))

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
			return HttpResponseRedirect('/')
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
	#args['form'] = form;
	return render_to_response('contact.html', args, context_instance=RequestContext(request))

def contact(request):
	pass

