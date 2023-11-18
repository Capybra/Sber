from django.urls import path

from . views import (
    cart_add, 
    user_order,
    cart_detail, 
    cart_remove
)

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('current_orders/', user_order, name='user_order'),
    path('current_orders/<int:order_id>/', user_order, name='user_order_special'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
