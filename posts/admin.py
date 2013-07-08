from django.contrib import admin
from posts.models import Post,Vote

admin.site.register(Post)
admin.site.register(Vote)