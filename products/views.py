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
    """ A view to show product details """
    
    print("Incoming product_id: ", product_id)  
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user 
            rating.product = product
            rating.save()
            messages.success(request, f'Thanks for your rating of product {product.name}')
            return redirect('product_detail', product_id=product_id)
    else:
        form = RatingForm()

    context = {
        'product': product,
        'form': form,
        'rating': product.average_rating,
    }

    return render(request, 'products/product_detail.html', context)


def clearance_items(request):
    products = Product.objects.filter(is_clearance=True)
    return render(request, 'products/clearance.html', {'products': products})


@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'products/wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, product_id):
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
    if product in wishlist.products.all():  # Check if the product is actually in the wishlist
        wishlist.products.remove(product)
        messages.success(request, f'{product.name} has been removed from your wishlist.')  # Success message
    else:
        messages.info(request, f'{product.name} was not in your wishlist.')  # Information message if the product was not found

    return redirect('view_wishlist')
