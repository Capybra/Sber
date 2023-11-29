from django import forms
from .models import Product
from shop.models import Product, Comment, CommentManage
from shop.forms import CommentForm

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'stock', 'description', 'available', 'week', 'clpc', 'star_rating', 'image']
        widgets = {
            'star_rating': forms.HiddenInput(),
            }
        labels = {
            'name': 'Имя',
            'price': 'Цена',
            'category': 'Категория',
            'stock': 'Кол-во',
            'description': 'Описание',
            'available': 'Доступен ли',
            'week': 'Неделя',
            'clpc': 'КБЖУ',
            'image': 'Изображение',
        }