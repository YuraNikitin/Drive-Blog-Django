from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from ..form.post import PostForm
from ..model.post import Post
from ..utils import *


class PostsList(ObjectListMixin, View):
    model = Post
    obj_query = None


class PostsListUsers(ObjectListMixin, View):
    model = Post
    obj_query = {'author': ''}


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
