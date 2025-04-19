from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, UploadFileForm
from .models import Women, Category, TagPost, UploadFiles
from .utils import DataMixin


class WomenHome(DataMixin, ListView):
    # model = Women
    template_name = 'women/index.html'
    context_object_name = 'post'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Women.published.all().select_related('cat')


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'women/about.html',
                  {'title': 'О сайте', 'form': form})



class ShowPost(DataMixin, DetailView):
    # model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)


    def get_object(self, queryset=None):
        return  get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    title_page = 'Добавление статьи'


class UpdatePage(DataMixin, UpdateView):
    model = Women
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование статьи'


class DeletePost(DeleteView):
    model = Women
    success_url = reverse_lazy('home')
    context_object_name = 'post'
    extra_context = {
        # 'menu': menu,
        'title': 'Удаление статьи',
    }

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class WomenCategory(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['post'][0].cat
        return  self.get_mixin_context(context,
                                       title=f"Категория - {cat.name}",
                                       cat_selected=cat.pk
                                       )


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class ShowTagList(DataMixin, ListView):
    template_name = 'women/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(tags__slug=self.kwargs['tag_slug']).select_related("cat")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['post'][0].tags.all()[0]
        return self.get_mixin_context(context, title=f"Тег - {tag.tag}")
