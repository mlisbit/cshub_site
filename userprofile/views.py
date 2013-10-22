from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

# Create your views here.

@login_required 
def user_profile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		#succesful profil update view
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin')

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