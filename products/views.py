from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Rating, Wishlist
from django.db.models.functions import Lower
from django.db.models import Avg
from .forms import RatingForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

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
            if sortkey == 'category':
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
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
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
    product = get_object_or_404(Product, pk=product_id)
    ratings = product.ratings.all().order_by('-created_at')
    form = RatingForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                messages.success(request, f'Thanks for your rating of product {product.name}')
                return redirect('product_detail', product_id=product_id)
            else:
                messages.error(request, "There was an error with your submission.")
        else:
            messages.error(request, "You must be logged in to submit a rating.")
            return redirect('account_login') 

    average_rating = product.average_rating() if product.ratings.exists() else None

    context = {
        'product': product,
        'form': form,
        'ratings': ratings,
        'average_rating': average_rating,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Rating, id=comment_id, product_id=product_id)
    
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    else:
        messages.error(request, "You do not have permission to delete this comment.")
    
    return redirect('product_detail', product_id=product_id)
 

@login_required
def edit_comment(request, product_id, rating_id):
    rating = get_object_or_404(Rating, id=rating_id, product_id=product_id, user=request.user)
    request.session['show_bag_message'] = False
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            messages.success(request, "Your rating and comment have been updated.")
            return redirect('product_detail', product_id=product_id)
    else:
        form = RatingForm(instance=rating)
    return redirect('product_detail', product_id=product_id)



def clearance_items(request):
    products = Product.objects.filter(is_clearance=True)
    return render(request, 'products/clearance.html', {'products': products})


@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'products/wishlist.html', {
        'wishlist': wishlist,
        })


@login_required
def add_to_wishlist(request, product_id):
    request.session['show_bag_message'] = False
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request, f'{product.name} has been added to your wishlist!')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'{product.name} has been removed from your wishlist.')
    else:
        messages.info(request, f'{product.name} was not in your wishlist.')

    return redirect('view_wishlist')
