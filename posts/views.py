from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from posts.models import *
from django.forms import ModelForm

#import pdb; pdb.set_trace()

class SubmitForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'link','text')

def index(request):
	posts = list(Post.objects.all())
	posts.sort(key=Post.score,reverse=True)
	return render(request, 'posts/index.html', {'posts': posts})

def details(request,id):
	return render(request, 'posts/details.html', {'post': Post.objects.get(pk=id)})

@login_required
def submit(request):
	formset = ""
	if request.method == 'POST':
		formset = SubmitForm(request.POST)
		if formset.is_valid():
			post = formset.save(commit=False)
			post.user = request.user
			post.save()
			return redirect(post)
	else:
		formset = SubmitForm()
	return render(request,"posts/submit.html", {"formset": formset,})

@login_required
def upvote(request,id):
	post = Post.objects.get(pk=id)
	vote = Vote(voter=request.user,post=post,upvote=True)
	vote.save()
	return render(request, 'posts/details.html', {'post': post})

@login_required
def downvote(request,id):
	post = Post.objects.get(pk=id)
	vote = Vote(voter=request.user,post=post,upvote=False)
	vote.save()
	return render(request, 'posts/details.html', {'post': post})