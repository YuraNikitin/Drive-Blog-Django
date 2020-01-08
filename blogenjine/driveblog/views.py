from django.shortcuts import render, redirect
from .forms import TagForm, PostForm
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin


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


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'driveblog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'driveblog/tag_create.html', context={'form': bound_form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'driveblog/post_create_form.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'driveblog/post_create_form.html', context={'form': bound_form})
