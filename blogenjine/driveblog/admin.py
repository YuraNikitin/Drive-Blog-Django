from django.contrib import admin

from .model.post import Post
from .model.tag import Tag

admin.site.register(Post)
admin.site.register(Tag)
