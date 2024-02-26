from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from item.models import Category, Product
from cart.models import CartItem, Cart
from favourites.models import Favourite
from .forms import NewProductForm, EditProductForm

def get_user_data(request):
    user_data = {
        'user': None,
        'cart_items': None,
        'total': None,
        'product_count': None,
        'fav_count': None
    }

    if request.user.is_authenticated:
        user_data['user'] = request.user
        cart = Cart.objects.get(user=user_data['user'])
        user_data['cart_items'] = CartItem.objects.filter(cart=cart)
        user_data['product_count'] = user_data['cart_items'].count()
        user_data['total'] = sum(item.product.price * item.quantity for item in user_data['cart_items'])
        user_data['fav_count'] = Favourite.objects.filter(user=user_data['user']).count()

    return user_data

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    related_items = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:4]

    user_data = get_user_data(request)

    return render(request, 'item/details.html', {
        'product': product,
        'categories': categories,
        'related_items': related_items,
        **user_data
    })

def searchProduct(request):
    searched = None
    products = None
    categories = Category.objects.all()

    if request.method == 'POST':
        searched = request.POST.get('searched', '')
        products = Product.objects.filter(Q(name__contains=searched) | Q(description__contains=searched))
        
    user_data = get_user_data(request)

    return render(request, 'item/searchProducts.html', {
        'searched': searched,
        'products': products,
        'categories': categories,
        **user_data
    })


# Account section -- staff only logic --
@login_required
def add_items(request):
    user_data = get_user_data(request)
    categories = Category.objects.all()
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
        'form': form,
        'title': 'Add Item',
        'categories': categories,
        **user_data
    })

@login_required
def edit(request, pk):    
    categories = Category.objects.all()
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    user_data = {
        'user': None,
        'cart_items': None,
        'total': None,
        'product_count': None,
        'fav_count': None
    }

    if request.user.is_authenticated:
        user_data['user'] = request.user
        cart = Cart.objects.get(user=user_data['user'])
        user_data['cart_items'] = CartItem.objects.filter(cart=cart)
        user_data['product_count'] = user_data['cart_items'].count()
        user_data['total'] = sum(item.product.price * item.quantity for item in user_data['cart_items'])
        user_data['fav_count'] = Favourite.objects.filter(user=user_data['user']).count()

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)  
    else:
        form = EditProductForm(instance=item)

    return render(request, 'item/form.html',  { 
        'form' : form,
        'title' : 'Edit Item',
        'categories' : categories,
        **user_data
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    item.delete()

    return redirect('/')
