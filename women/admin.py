from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5



@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# admin.site.register(Women, WomenAmin)
