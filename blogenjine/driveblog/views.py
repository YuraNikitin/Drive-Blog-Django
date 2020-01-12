from .forms import *
from .models import *
from django.views.generic import View
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class PostsListUsers(ObjectListMixin, View):
    model = Post
    obj_query = 'user posts'


class PostsList(ObjectListMixin, View):
    model = Post
    obj_query = 'other posts'


def tags_list(request):
    if request.user.is_authenticated:
        tags = Tag.objects.all()
        return render(request, 'driveblog/tags_list.html', context={'tags': tags})
    else:
        return redirect('login')


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


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'driveblog/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('posts_list_url')
            else:
                return redirect('login')
        return render(request, 'driveblog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterNewUser(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'driveblog/register.html', context={'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        return render(request, 'driveblog/register.html', context={'form': form})
