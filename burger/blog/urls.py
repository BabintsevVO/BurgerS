from django.urls import path
from .views import *

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
]