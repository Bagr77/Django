from django import template
import sitewomen.sitewomen.women.views as views

from sitewomen.sitewomen.women.models import Category

register = template.Library()



@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

