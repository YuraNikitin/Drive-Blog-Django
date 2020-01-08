from .forms import TagForm, PostForm
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from django.urls import reverse


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


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'driveblog/tag_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'driveblog/tag_delete.html'
    redirect_url = 'tags_list_url'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'driveblog/post_create_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'driveblog/post_update.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'driveblog/post_delete.html'
    redirect_url = 'posts_list_url'
