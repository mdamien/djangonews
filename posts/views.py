from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from posts.models import *
from django.forms import ModelForm
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#import pdb; pdb.set_trace()

class SubmitForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'link','text')

class CommentReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'parent','comment')

def index(request):
	posts = list(Post.objects.all())
	posts.sort(key=Post.score,reverse=True)
	paginator = Paginator(posts, 50)
	page = request.GET.get('p')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'posts/index.html', {'posts': posts})

def details(request,id):
	post = Post.objects.get(pk=id)
	comments = Comment.objects.filter(post=post)
	return render(request, 'posts/details.html', {'post': post,'comments':comments})

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

def vote(request,id,upvote):
	post = Post.objects.get(pk=id)
	vote = Vote.objects.filter(post=post,voter=request.user) #permits admin-mass-voting
	if vote:
		vote = vote[0]
		vote.upvote = upvote
		vote.save()
	else:
		vote = Vote(voter=request.user,post=post,upvote=upvote)
		vote.save()
	return redirect(post)

@login_required
def upvote(request,id):
	return vote(request,id,True)

@login_required
def downvote(request,id):
	return vote(request,id,False)

def comment_vote(request,post_id,node_id,upvote):
	post = Post.objects.get(pk=post_id)
	comment = Comment.objects.get(pk=node_id)
	vote = CommentVote.objects.filter(voter=request.user,comment=comment) #permits admin-mass-voting
	if vote:
		vote = vote[0]
		vote.upvote = upvote
		vote.save()
	else:
		vote = CommentVote(voter=request.user,comment=comment,upvote=upvote)
		vote.save()
	return redirect(post)

@login_required
def comment_downvote(request,post_id,node_id):
	return comment_vote(request,post_id,node_id,False)

@login_required
def comment_upvote(request,post_id,node_id):
	return comment_vote(request,post_id,node_id,True)

@login_required
def comment_reply(request,post_id,parent_id):
	formset = ""
	if request.method == 'POST':
		formset = CommentReplyForm(request.POST)
		if formset.is_valid():
			comment = formset.save(commit=False)
			comment.author = request.user
			comment.save()
			return redirect(comment.post)
	else:
		comment = Comment()
		comment.post = Post.objects.get(pk=post_id)
		if parent_id != "0":
			comment.parent = Comment.objects.get(pk=parent_id)
		formset = CommentReplyForm(instance=comment)
	formset.fields['post'].widget = forms.HiddenInput()
	formset.fields['parent'].widget = forms.HiddenInput()
	return render(request,"posts/comment_reply.html", {"formset": formset,})
