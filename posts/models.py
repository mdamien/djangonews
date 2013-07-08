from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=600, blank=True)
    text = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.post.title)