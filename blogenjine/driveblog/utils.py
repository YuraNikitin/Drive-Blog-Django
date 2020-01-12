from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator


class ObjectListMixin():
    model = None
    obj_query = None

    def get(self, request):
        if request.user.is_authenticated:
            search_query = request.GET.get('search', '')
            if search_query:
                posts = self.model.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
            elif self.obj_query == 'user posts':
                posts = self.model.objects.filter(author=request.user)
            elif self.obj_query == 'other posts':
                posts = self.model.objects.all()
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
        else:
            return redirect('login')


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj,
                                                       'detail': True})


class ObjectCreateMixin():
    form_model = None
    template = None
    model = None

    def get(self, request):
        form = self.form_model()
        # print('id users'+ str(request.user))
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST, request.FILES)
        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.author = request.user
            new_obj.save()
            bound_form.save_m2m()

            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin():
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, request.FILES, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin():
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        try:
            obj = self.model.objects.get(Q(slug__iexact=slug) & Q(author=request.user))
            obj.delete()
            return redirect(reverse(self.redirect_url))
        except self.model.DoesNotExist:
            return render(request, 'driveblog/error.html')
