from django.shortcuts import render, redirect
from .forms import TagForm, PostForm
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'driveblog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'driveblog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'driveblog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'driveblog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'driveblog/tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'driveblog/post_create_form.html'

