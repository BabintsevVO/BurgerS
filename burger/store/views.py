from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProductCategory, Product


class Home(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Burgers'
        context['premiums'] = Product.objects.all().order_by('-rating')[:2]
        return context


class ProductByCategory(ListView):
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ProductCategory.objects.get(slug=self.kwargs['slug'])
        return context

def index(request):
    return render(request, 'store/index.html')


def get_category(request):
    return render(request, 'store/index.html')


def get_product(request):
    return render(request, 'store/index.html')
