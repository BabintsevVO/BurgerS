from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html')


def get_category(request):
    return render(request, 'store/menu.html')