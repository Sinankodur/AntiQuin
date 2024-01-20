from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favourite

@login_required
def add_to_favourites(request, product_id):
    product_id = int(product_id)
    user = request.user

    if not Favourite.objects.filter(user=user, product_id=product_id).exists():
        favourites = Favourite(user=user, product_id=product_id)
        favourites.save()

    return redirect('favourites/')

@login_required
def view_favourites(request):
    user = request.user
    favourites = Favourite.objects.filter(user=user)
    fav_count = Favourite.objects.filter(favourites=favourites).count()

    return render(request, 'favourites/favourites.html', {
        'fav_count' : fav_count,
    })