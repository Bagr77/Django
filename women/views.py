from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string



# Create your views here.u

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

def index(request):
    data = {
        "title": 'Мега главная страница?',
        'menu': menu,
        'posts': data_db
    }

    return render(request,'women/index.html', context=data)
    #return HttpResponse('<h1>Супер главная страница !!!!<h1/>')

def about(request):
    return render(request, 'women/about.html',{'title': 'О сайте !!!!'})

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
