from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('clearance/', views.clearance_items, name='clearance_items'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('product/<int:product_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('product/<int:product_id>/edit_comment/<int:rating_id>/', views.edit_comment, name='edit_comment'),
]