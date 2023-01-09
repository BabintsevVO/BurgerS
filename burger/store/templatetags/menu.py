from django import template
from store.models import ProductCategory

register = template.Library()


@register.inclusion_tag('store/menu_tpl.html')
def show_menu(menu_class='row'):
    store_categories = ProductCategory.objects.all()
    return {"store_categories": store_categories, "menu_class": menu_class}

