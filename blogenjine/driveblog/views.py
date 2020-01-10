from .forms import TagForm, PostForm
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)  # 1-count posts in page
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    contex = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url

    }

    return render(request, 'driveblog/index.html', context=contex)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'driveblog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'driveblog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'driveblog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'driveblog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'driveblog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'driveblog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'driveblog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'driveblog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'driveblog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True
