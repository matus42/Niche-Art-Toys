from django.contrib import admin
from .models import Product, Category, Rating, Wishlist


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


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_products')

    def display_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
