from django import template
from menu.models import *

register = template.Library()


@register.inclusion_tag('menu/menu_templatetag.html')
def draw_menu():
    cats = Category.objects.all()
    return {'cats': cats}
