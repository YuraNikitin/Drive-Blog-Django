from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from ..form.tag import TagForm
from ..model.tag import Tag
from ..utils import *


def tags_list(request):
    if request.user.is_authenticated:
        tags = Tag.objects.all()
        return render(request, 'driveblog/tag_templates/tags_list.html', context={'tags': tags})
    else:
        return redirect('login')


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'driveblog/tag_templates/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'driveblog/tag_templates/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'driveblog/tag_templates/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'driveblog/tag_templates/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
