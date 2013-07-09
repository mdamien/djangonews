from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from posts.models import *

def index(request):
	return render(request, 'posts/index.html', {'posts': Post.objects.all()})

def details(request,id):
	return render(request, 'posts/details.html', {'post': Post.objects.get(pk=id)})

@login_required
def upvote(request,id):
	pass

@login_required
def downvote(request,id):
	pass