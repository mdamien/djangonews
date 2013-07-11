from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=600, blank=True)
    text = models.TextField(blank=True)

    def score(self):
        return Vote.objects.filter(post=self,upvote=True).count() - Vote.objects.filter(post=self,upvote=False).count()

    def get_absolute_url(self):
        return reverse('posts.views.details', args=[str(self.pk)])

    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    upvote = models.BooleanField()

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.post.title)