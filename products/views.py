from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import RatingForm
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Rating, Wishlist
from .forms import ProductForm
from bag.views import clean_shopping_bag
from django.db.models import Avg, DecimalField
from django.db.models.functions import Coalesce


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    clean_shopping_bag(request)
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'avg_rating':
                products = products.annotate(
                    avg_rating=Coalesce(Avg('ratings__score'),
                                        0, output_field=DecimalField())
                )
                sortkey = 'avg_rating'
            elif sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please Enter Search Criteria.")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

    for product in products:
        product.avg_rating = product.average_rating()

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View function for displaying details of a product.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to display details for.
    """
    product = get_object_or_404(Product, pk=product_id)
    ratings = product.ratings.all().order_by('-created_at')
    form = RatingForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RatingForm(request.POST)
            request.session['show_bag_message'] = False
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                messages.success(
                    request,
                    f'Thanks for your rating of product {product.name}'
                    )
                return redirect('product_detail', product_id=product_id)
            else:
                messages.error(
                    request,
                    "There was an error with your submission."
                    )
        else:
            messages.error(request,
                           "You must be logged in to submit a rating.")
            return redirect('account_login')

    average_rating = (
        product.average_rating() if product.ratings.exists() else None
        )

    context = {
        'product': product,
        'form': form,
        'ratings': ratings,
        'average_rating': average_rating,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def delete_comment(request, product_id, comment_id):
    """
    View function for deleting a comment on a product.
    This view requires the user to be authenticated.
    If the user is a superuser
    or the owner of the comment, the comment will be deleted.
    """
    comment = get_object_or_404(Rating, id=comment_id, product_id=product_id)

    if request.user.is_superuser or request.user == comment.user:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    else:
        messages.error(
            request,
            "You do not have permission to delete this comment."
            )

    return redirect('product_detail', product_id=product_id)


@login_required
def edit_comment(request, product_id, rating_id):
    """
    View function for editing a comment on a product.

    This view allows the user to edit their own comment on a product.
    Superusers have the ability to edit any comment.
    """
    if request.user.is_superuser:
        rating = get_object_or_404(Rating, id=rating_id, product_id=product_id)
    else:
        rating = get_object_or_404(Rating, id=rating_id,
                                   product_id=product_id, user=request.user)
    request.session['show_bag_message'] = False

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your rating and comment have been updated.")
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(
                request,
                "There was a problem with your submission. "
                "Please check the form for errors."
                )
    else:
        form = RatingForm(instance=rating)
    return redirect('product_detail', product_id=product_id)


def clearance_items(request):
    """
    View function for displaying clearance items.

    This view retrieves all products marked as clearance items and renders
    them on the clearance pag
    """
    products = Product.objects.filter(is_clearance=True)
    return render(request, 'products/clearance.html', {'products': products})


@login_required
def view_wishlist(request):
    """
    View function for displaying wishlist items.
    Only authenticated users can view their wishlist.
    """
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'products/wishlist.html', {
        'wishlist': wishlist,
        })


@login_required
def add_to_wishlist(request, product_id):
    """
    View function for adding a product to the user's wishlist.

    This view adds a product to the user's wishlist if it's not already
    present. If the product is already in the wishlist, an informational
    message is displayed.
    """
    request.session['show_bag_message'] = False
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(
            request,
            f'{product.name} has been added to your wishlist!')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """
    View function for removing a product from the user's wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(
            request,
            f'{product.name} has been removed from your wishlist.'
            )
    else:
        messages.info(request, f'{product.name} was not in your wishlist.')

    return redirect('view_wishlist')


@login_required
def add_product(request):
    """
    Add a product to the store
    This view allows only superusers (store owners)
    to add products to the store.
    If the user is not a superuser, an error message is displayed.
    """
    request.session['show_bag_message'] = False
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    request.session['show_bag_message'] = False
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    request.session['show_bag_message'] = False
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
    except Product.DoesNotExist:
        messages.error(request, 'This product no longer exists.')

    return redirect(reverse('products'))
