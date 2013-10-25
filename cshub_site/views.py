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
from forms import MyRegistrationForm

#password reset
from django.contrib.auth.views import password_reset

from django.contrib.auth.models import User

def home(request):
	c= {}
	c['users'] = User.objects.all()
	c['total_users'] = User.objects.all().__len__
	c.update(csrf(request))
	return render_to_response('home.html', c, context_instance=RequestContext(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def login(request):
	c= {}
	c.update(csrf(request))
	return render_to_response('login.html', c, context_instance=RequestContext(request))
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
			return HttpResponseRedirect('/accounts/register_success')
	else:
		form = MyRegistrationForm()
	args = {}
	args.update(csrf(request))

	args['form'] = form;

	return render_to_response('register.html', args, context_instance=RequestContext(request))

def register_success(request):
	return render_to_response('register_success.html')

	