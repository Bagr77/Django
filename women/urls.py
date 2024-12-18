from multiprocessing.resource_tracker import register

from . import views
from django.urls import path, re_path, register_converter
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('women/', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path("archive/<year4:year>/", views.archive),
    path('', views.major),
]