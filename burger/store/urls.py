from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', ProductByCategory.as_view(), name='store_category'),
    path('product/<str:slug>/', get_product, name='product'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
    path('basket-del-pcs/<int:product_id>/', basket_del_pcs, name='basket_del_pcs'),
]
