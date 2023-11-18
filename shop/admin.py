from django.contrib import admin

from .models import Category, Product, Comment, StarRating, Cafeteria, Table
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'user', 'written_at', 'star_rating', 'description']
    list_editable = ['description']

admin.site.register(Comment, CommentAdmin)


class StarRatingAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'star_1', 'star_2', 'star_3', 'star_4', 'star_5']
    list_editable = ['star_1', 'star_2', 'star_3', 'star_4', 'star_5']

admin.site.register(StarRating, StarRatingAdmin)


class CafeteriaAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'address', 'available', 'rows', 'cols', 'created_at', 'description']
    list_editable = ['address', 'available', 'rows', 'cols', 'description']


admin.site.register(Cafeteria, CafeteriaAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'hidden', 'available', 'number', 'row', 'col', 'created_at', 'order_id', 'ordered_until']
    list_editable = ['hidden', 'available', 'order_id', 'number']


admin.site.register(Table, TableAdmin)