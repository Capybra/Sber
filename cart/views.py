from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from shop.models import Product, Cafeteria, Table
from users.models import Profile
from orders.models import Order, OrderItem
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, 'Удалено')
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    cafeteria = Cafeteria.objects.get(id=3)
    tables = Table.objects.filter(cafeteria_id=3)  # ОТОБРАЖЕНИЕ ТЕКУЩЕЙ КАФЕТЕРИИ TODO
    context = {'cart': cart, 'cafeteria': cafeteria, 'tables': tables}
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', context)


def user_order(request, order_id=0):
    profile = Profile.objects.get(email=request.user.email)
    all_orders = Order.objects.filter(profile_id=profile.id)
    current_table = None
    if not order_id:
        order = Order.objects.filter(profile_id=profile.id).first()
    else:
        order = Order.objects.get(id=order_id)
    if order is None:
        order_items = None
        return render(request, 'cart/user_order.html', {'order': order})
    else:
        if order.in_cafe:
            current_table = order.table
        order_items = OrderItem.objects.filter(order_id=order.id)
    cafeteria = Cafeteria.objects.get(id=3)
    tables = Table.objects.filter(cafeteria_id=3)  # ОТОБРАЖЕНИЕ ТЕКУЩЕЙ КАФЕТЕРИИ TODO
    context = {'order_items': order_items, 'order': order, 'all_orders': all_orders,
               'cafeteria': cafeteria, 'tables': tables, 'current_table': current_table, 'profile': profile}
    return render(request, 'cart/user_order.html', context)

