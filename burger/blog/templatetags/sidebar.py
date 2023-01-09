from django import template
from blog.models import Category, Tag, Post

register = template.Library()


@register.inclusion_tag('blog/categories_tpl.html')
def get_categories(menu_class='sidebar'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}


@register.inclusion_tag('blog/popular_post_tpl.html')
def get_popular_post():
    posts = Post.objects.order_by('-views')[:3]
    return {"posts": posts}
