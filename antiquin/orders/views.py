from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Order
from .forms import OrderForm
from item.models import Product,Category
from cart.models import Cart, CartItem
from favourites.models import Favourite


@login_required
def order_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=user_cart, product=product)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            order = Order.objects.create(
                user=request.user,
                quantity=quantity,
                total_price=total_price,
                is_paid=False
            )

            order.cart_item = cart_item
            order.save()

            cart_item.delete()

            # may to integrate payment processing here

            return render(request, '/orders/thank_you.html', {'order': order})

    else:
        form = OrderForm()

    return render(request, '/orders/order_now.html', {'product': product, 'form': form})



@login_required
def view_orders(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-order_date')
    # if this is needed or not need to check 
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

    return render(request, 'orders/orders.html', {
        'user_orders': user_orders,
        'cart_items': cart_items,
        'total': total,
        'categories' : categories,
        'product' : product,
        'product_count' : product_count,
        'fav_count' : fav_count,
    })

