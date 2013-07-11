from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=600, blank=True)
    text = models.TextField(blank=True)

    def score(self):
        return Vote.objects.filter(post=self,upvote=True).count() - Vote.objects.filter(post=self,upvote=False).count()

    def comments_count(self):
        return Comment.objects.filter(post=self).count()

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


class Comment(MPTTModel):
    """ Threaded comments for posts """
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    comment = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def score(self):
        return CommentVote.objects.filter(comment=self,upvote=True).count() - CommentVote.objects.filter(comment=self,upvote=False).count()

    class MPTTMeta:
        order_insertion_by=['date']

    def __unicode__(self):
        return "%s comment on %s" % (self.author.username, self.post)

class CommentVote(models.Model):
    voter = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    upvote = models.BooleanField()

    def __unicode__(self):
        return "%s upvoted %s" % (self.voter.username, self.comment)