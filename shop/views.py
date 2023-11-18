from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from .models import Category, Product, StarRating, Comment
from .forms import CommentForm, StarRatingForm, ProductStarRatingUpdateForm
from cart.forms import CartAddProductForm
from users.views import user_registration
from users.forms import LoginForm, RegistrationForm
from decimal import Decimal, ROUND_HALF_UP

from config.views import get_natural_range
from django.http import JsonResponse
from .models import Cafeteria, Table
from django.views.decorators.http import require_GET

from django.views.generic import (
    ListView,
    DetailView
)
'''
class ProductListView(ListView):
    template_name = 'shop/product/list.html'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
'''

def product_list(request, category_slug=None, week=1):
    login_error = ""
    registration_error = ""
    if request.method == "POST":
        errors = user_registration(request)
        login_error, registration_error = errors["login_error"], errors["registration_error"]
    registration_form = RegistrationForm()
    login_form = LoginForm()
    category = None
    week_url = '/all/'
    comments = Comment.objects.exclude(description="")
    categories = Category.objects.all().order_by('-created_at')
    products = Product.objects.filter(available=True) & Product.objects.filter(week=week)
    if category_slug and category_slug != 'all':
        week_url = '/' + category_slug + '/'
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category) & Product.objects.filter(week=week)
    cafeteria = Cafeteria.objects.get(id=3)
    tables = Table.objects.filter(cafeteria_id=3)  # ОТОБРАЖЕНИЕ ТЕКУЩЕЙ КАФЕТЕРИИ TODO
    context = {
        'form_dict': {
            'login_form': login_form,
            'registration_form': registration_form,
        },
        'category': category,
        'categories': categories,
        'products': products,
        'login_error': login_error,
        'registration_error': registration_error,
        'week_url': week_url,
        'comments': comments,
        'tables': tables,
        'cafeteria': cafeteria,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


@require_POST
def comment_add(request, product_id, username):
    data = request.POST
    product = get_object_or_404(Product, id=product_id)
    comment_data = {"user": username, "star_rating": data['rating'], "description": data['comment-text'], "product": product_id}
    now_rating = StarRating.objects.filter(product_id=product_id)
    total_rating = 0
    if now_rating.count():
        now_rating = StarRating.objects.get(product_id=product_id)
        rating_data = model_to_dict(now_rating, fields=[field.name for field in now_rating._meta.fields])
        user_comments = Comment.objects.filter(user=username, product_id=product_id)
        if user_comments.count():
            for com in user_comments:
                com_rating = com.star_rating
                print(com_rating)
                rating_data[f'star_{str(com_rating)}'] -= 1
                com.delete()
        rating_data[f'star_{str(data["rating"])}'] += 1
        rating_sum = 0
        rating_count = 0
        for key in rating_data.keys():
            if "star" in key:
                rating_sum += rating_data[key] * int(key.split("_")[1])
                rating_count += rating_data[key]
        total_rating = Decimal(rating_sum / rating_count).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        rating_form = StarRatingForm(rating_data, instance=now_rating)
        rating_form.save()
    else:
        rating_data = {"star_1": 0, "star_2": 0, "star_3": 0, "star_4": 0, "star_5": 0, "product": product_id}
        rating_data[f'star_{str(data["rating"])}'] += 1
        total_rating = Decimal(data["rating"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        rating_form = StarRatingForm(rating_data)
        rating_form.save()
    comment_form = CommentForm(comment_data)
    comment_form.save()
    product_upd = ProductStarRatingUpdateForm({"star_rating": total_rating}, instance=product)
    product_upd.save()
    return redirect('shop:product_list')


@require_GET
def get_table(request):
    tableseatId = request.GET.get('seatId')
    try:
        table = Table.objects.get(id=tableseatId)
        data = {
            'number': table.number,
            'id': table.id,
        }
    except Table.DoesNotExist:
        data = {
            'number': "",
            'id': 0,
        }
    return JsonResponse(data)

def logout_view(request):
    logout(request)
    return redirect('shop:product_list')