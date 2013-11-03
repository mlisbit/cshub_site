from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import Positions
from django.template import RequestContext

# Create your views here.

@login_required 
def user_profile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		#succesful profil update view
		if form.is_valid():
			originalform = UserProfileForm(instance = request.user.profile)
			form.save()
			return HttpResponseRedirect('/accounts/profile')

	else:
		user = request.user
		profile = user.profile
		form = UserProfileForm(instance = profile)

	args = {}
	args.update(csrf(request))

	u = User.objects.get(username=user.username) # Get the first user in the system

	args['uname'] = u.username 
	args['name'] = u.first_name
	args['last'] = u.last_name
	args['email'] = u.email
	args['thumbnail'] = request.user.profile.user_avatar
	args['form'] = form

	return render_to_response('profile.html', args, context_instance=RequestContext(request))

def view_members(request):
	args = {}
	args.update(csrf(request))

	args['positions'] = Positions.objects.all()
	args['admin'] = User.objects.get(username='admin').profile.club_position.all()
	args['members'] = User.objects.all()
	return render_to_response('members.html', args, context_instance=RequestContext(request))

def view_member(request, username='mlisbit'):
	args = {}
	args.update(csrf(request))

	args['member'] = User.objects.get(username=username)
	args['profile'] = User.objects.get(username=username).profile

	return render_to_response('view_profile.html', args, context_instance=RequestContext(request))