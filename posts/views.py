from django.shortcuts import get_object_or_404, render
from posts.models import *

def index(request):
	return render(request, 'posts/index.html', {'posts': Post.objects.all()})

def post(request,id):
	return render(request, 'posts/post.html', {'post': Post.objects.get(pk=id)})