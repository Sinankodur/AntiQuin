from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from item.models import Category, Product
from cart.models import Cart, CartItem
from favourites.models import Favourite
from .forms import AddressForm
from .models import Address

def profile(request):
    user = request.user
    categories = Category.objects.all()
    products = Product.objects.all()

    user_cart, created = Cart.objects.get_or_create(user=user)

    cart_items = CartItem.objects.filter(cart=user_cart)
    product_count = cart_items.count()
    total = sum(item.product.price * item.quantity for item in cart_items)

    favourites = Favourite.objects.filter(user=user)
    fav_count = favourites.count()

    return render(request, 'account/profile.html', {
        'categories': categories,
        'products': products,
        'total': total,
        'product_count': product_count,
        'fav_count': fav_count,
    })



@login_required
def address(request):
    user = request.user

    cart, created = Cart.objects.get_or_create(user=user)
        
    cart_items = CartItem.objects.filter(cart=cart)
    product_count = CartItem.objects.filter(cart=cart).count()
    total = sum(item.product.price * item.quantity for item in cart_items)
    categories = Category.objects.all()
    product = Product.objects.all()

    for item in cart_items:
        item.subtotal = item.product.price * item.quantity

    favourites = Favourite.objects.filter(user=user)
    fav_count = favourites.count()

    return render(request, 'account/address.html', {
        'cart_items': cart_items,
        'total': total,
        'categories' : categories,
        'product' : product,
        'product_count' : product_count,
        'fav_count' : fav_count,
    })



def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address_data = {
                'address_line': form.cleaned_data['inputAddress'],
                'address_line2': form.cleaned_data['inputAddress2'],
                'city': form.cleaned_data['inputCity'],
                'state': form.cleaned_data['inputState'],
                'pin_code': form.cleaned_data['inputZip'],
            }
            address_instance = Address.objects.create(**address_data)

            return redirect('/account/profile')
    else:
        form = AddressForm()

    return render(request, 'account/address.html', {'form': form})
