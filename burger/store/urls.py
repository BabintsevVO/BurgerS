from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', ProductByCategory.as_view(), name='store_category'),
    path('product/<str:slug>/', get_product, name='product'),
]