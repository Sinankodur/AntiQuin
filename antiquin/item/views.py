from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from item.models import Category,Product
from cart.models import CartItem, Cart
from favourites.models import Favourite
from .forms import NewProductForm

def detail(request,pk):
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    related_items = Product.objects.filter(category=product.category, is_sold = False).exclude(pk=pk)[0:4]

    if request.user.is_authenticated:
        user = request.user.id
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = CartItem.objects.filter(cart=cart).count()
        total = sum(item.product.price * item.quantity for item in cart_items)

        fav_count = Favourite.objects.filter(user=user).count()

        return render(request, 'item/details.html', {
            'product': product, 
            'categories': categories,
            "related_items": related_items,
            'total' : total,
            'product_count' : product_count,
            'fav_count' : fav_count
        })
    
    return render(request, 'item/details.html', {
            'product': product, 
            'categories': categories,
            "related_items": related_items,
        })

def searchProduct(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__contains=searched) | Q(description__contains=searched) )
        categories = Category.objects.all()

    if request.user.is_authenticated:
        user = request.user.id
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        product_count = cart_items.count()
        total = sum(item.product.price * item.quantity for item in cart_items)

        fav_count = Favourite.objects.filter(user=user).count()

        return render(request, 'item/searchProducts.html' ,{
            'searched': searched,
            'products': products,
            'categories': categories,
            'total' : total,
            'product_count' : product_count,
            'fav_count' : fav_count
        })
    
    return render(request, 'item/searchProducts.html' ,{
        'searched': searched,
        'products': products,
        'categories': categories,
        })


# Account section -- staff only logic --
@login_required
def add_items(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
        
    else:
        form = NewProductForm()

    return render(request, 'item/form.html', { 
        'form' : form,
        'title' : 'Add Items',
    })