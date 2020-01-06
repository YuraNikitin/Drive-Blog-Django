from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'driveblog/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'driveblog/post_detail.html', context={'post': post})