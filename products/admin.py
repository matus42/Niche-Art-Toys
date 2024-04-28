from django.contrib import admin
from .models import Product, Category, Rating

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'stock_quantity',
        'category',
        'price',
        'rating',
        'image',
        'is_clearance',
    )

    ordering = ('sku',)
    list_editable = ('is_clearance', 'stock_quantity',)
    list_filter = ('is_clearance', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'user',
        'score',
        'product',
        'comment',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
