from django.contrib import admin
from posts.models import *

admin.site.register(Post)
admin.site.register(Vote)
admin.site.register(Comment)
admin.site.register(CommentVote)