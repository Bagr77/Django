from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse('<h1>Супер главная страница<h1/>')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям<h1/><p>cat_id {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям<h1/><p>cat_slug {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        url = reverse('cats', args=('music', ))
        return redirect(url)

    return HttpResponse(f"year: {year}")

def posts_list(request, year):
    if  1990 <= year <= 2023:
        return HttpResponse("posts: <year>")
    else:
        raise Http404()


def major(request):
    return HttpResponse('<h1>Супер главная страница<h1/>')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def page_not_found2(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
