from django.contrib import admin
from .model.post import  Post
from .model.tag import Tag
# # Register your models here.
#
admin.site.register(Post)
admin.site.register(Tag)