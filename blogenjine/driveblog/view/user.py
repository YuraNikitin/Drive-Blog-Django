from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

from ..form.user import LoginForm
from ..form.user import UserRegistrationForm
from ..utils import *


class Login(View):
    """Class login, contains method's POST, GET"""
    def get(self, request):
        form = LoginForm()

        return render(request, 'driveblog/user_templates/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('posts_list_url')
            else:
                return redirect('login')

        return render(request, 'driveblog/user_templates/login.html', {'form': form})


class RegisterNewUser(View):
    """Class registration, contains method's POST, GET"""
    def get(self, request):
        form = UserRegistrationForm()

        return render(request, 'driveblog/user_templates/register.html', context={'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')

        return render(request, 'driveblog/user_templates/register.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



