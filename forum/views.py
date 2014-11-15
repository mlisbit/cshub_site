from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response 
from django.views.generic.base import TemplateView
from django.template import RequestContext
from models import Catagory, Forum, Thread, Post
from django.contrib.auth.decorators import login_required

def forum_home(request):
	args = {}
	args['catagories'] = Catagory.objects.all()
	args['forums'] = Forum.objects.all()
	return render_to_response('forum_home.html', args, context_instance=RequestContext(request))

#a list of all the threads
def view_threads(request, forum_name):
	args = {}
	args['forum_name'] = forum_name
	args['pretty_forum_name'] = forum_name.replace ("_", " ").replace (".qm.", "?")
	args['current_url'] = request.get_full_path()
	args['threads'] = Thread.objects.filter(forum__name__exact=str(forum_name).replace ("_", " ").replace (".qm.", "?"))
	return render_to_response('sub_forum_home.html', args, context_instance=RequestContext(request))

#the actual thread, that people post in.
def view_thread(request, forum_name, thread_name):
	args = {}
	args['forum_name'] = forum_name.replace ("_", " ").replace (".qm.", "?")
	args['thread_name'] = thread_name.replace ("_", " ").replace (".qm.", "?")
	args['posts'] = Post.objects.filter(topic__name=str(thread_name).replace ("_", " ").replace (".qm.", "?"))
	args['thread'] = Thread.objects.filter(name=str(thread_name).replace ("_", " ").replace (".qm.", "?"))[0]
	args['current_url'] = request.get_full_path()
	return render_to_response('view_thread.html', args, context_instance=RequestContext(request))

@login_required
def reply_to_thread(request):
	thread_name = request.POST['thread_name']
	newpost = Post();
	newpost.message = request.POST['message']
	newpost.posted_by = request.user
	newpost.topic = Thread.objects.filter(name=str(thread_name).replace ("_", " ").replace (".qm.", "?"))[0]
	
	newpost.save()
	args = {}
	#return render_to_response('view_thread.html', args, context_instance=RequestContext(request))
	return HttpResponseRedirect(request.POST['current_url'])

@login_required
def create_thread(request):

	newThread = Thread();
	newThread.message = request.POST['message']
	newThread.name = request.POST['title']
	newThread.created_by = request.user
	forum_name = str(request.POST['forum_name']).replace ("_", " ").replace (".qm.", "?")
	newThread.forum = Forum.objects.filter(name=forum_name)[0]
	#newThread.topic = Forum.objects.filter(name=str(thread_name).replace ("_", " ").replace (".qm.", "?"))[0]
	newThread.save()
	args = {}
	#return render_to_response('view_thread.html', args, context_instance=RequestContext(request))
	return HttpResponseRedirect(request.POST['current_url'])