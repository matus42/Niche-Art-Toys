from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Rating
from django.db.models.functions import Lower
from django.db.models import Avg
from .forms import RatingForm


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
            messages.success(request, 'Thanks for your rating!')
            return redirect('product_detail', product_id=product_id)
    else:
        form = RatingForm()

    context = {
        'product': product,
        'form': form,
        'rating': product.average_rating,
    }

    return render(request, 'products/product_detail.html', context)