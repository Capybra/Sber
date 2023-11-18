from django.contrib import admin
from django.urls import path

from shop.views import (
    product_list, 
    product_detail,
    logout_view,
    comment_add,
    get_table,
)

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('logout/', logout_view, name='logout_view'),
    path('get_table/', get_table, name='get_table'),
    path('<str:category_slug>/<int:week>', product_list, name='product_list_by_category'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail'),
    path('comment/<int:product_id>/<str:username>/', comment_add, name='comment_view'),
]
