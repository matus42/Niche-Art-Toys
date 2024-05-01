from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    request.session['show_bag_message'] = False
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag, not exceeding stock availability. """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    total_quantity = quantity + bag.get(item_id, 0)  # Total desired quantity including what's already in the bag

    if total_quantity <= product.stock_quantity:
        if item_id in bag:
            bag[item_id] += quantity
            request.session['show_bag_message'] = True
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]} in your bag.')
        else:
            bag[item_id] = quantity
            request.session['show_bag_message'] = True
            messages.success(request, f'Added {product.name} to your bag.')
    else:
        messages.error(request, f'Sorry, adding {total_quantity} units exceeds the available stock for {product.name}. Max {product.stock_quantity - bag.get(item_id, 0)} can be added.')

    request.session['bag'] = bag
    
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount, ensuring it does not exceed stock."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity <= product.stock_quantity:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]} in your bag.')
        else:
            bag.pop(item_id, None)
            messages.success(request, f'{product.name} has been removed from your bag.')
    else:
        messages.error(request, f'Cannot set quantity to {quantity}. Only {product.stock_quantity} units are available for {product.name}.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'{product.name} has been removed from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Failed to remove {product.name} from your bag. Please try again.')
        return HttpResponse(status=500)
