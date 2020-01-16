from ..model.post import Post
from ..form.post import PostForm
from django.views.generic import View
from ..utils import *
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsListUsers(ObjectListMixin, View):
    model = Post
    obj_query = 'user posts'


class PostsList(ObjectListMixin, View):
    model = Post
    obj_query = 'other posts'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'driveblog/post_templates/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'driveblog/post_templates/post_create_form.html'

    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'driveblog/post_templates/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'driveblog/post_templates/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True
