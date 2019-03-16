from django.shortcuts import render, redirect
from .models import Shop

#Split list in approx. n per list
def split_n_items_per_part(the_list, n):
    n_complete_parts = int(len(the_list)/n)
    n_left_items = len(the_list)%n

    res = [ the_list[i*n:n*i+n] for i in range(0,n_complete_parts) ]
    res.append(the_list[n_complete_parts*n:n_complete_parts*n+n_left_items+1])
    return res

# Create your views here.
def shop_nearby(request):
    if not request.user.is_authenticated:
        return redirect("/")

    shops = Shop.shops_to_be_displayed_nearby(request.user)
    group_4_shops = split_n_items_per_part(shops, 4)

    context = {
        "group_4_shops": group_4_shops,
        "shops_active": "active"
    }
    return render(request, 'index.html', context)

def shop_liked(request):
    if not request.user.is_authenticated:
        return redirect("/")

    shops = Shop.liked_by(request.user)
    group_4_shops = split_n_items_per_part(shops, 4)

    context = {
        "group_4_shops": group_4_shops,
        "preferred_shops_active": "active"
    }
    return render(request, 'index.html', context)


def shop_like(request, id_shop):
    if not request.user.is_authenticated:
        return redirect("/")

    Shop.objects.get(id=id_shop).add_like_by(request.user)
    return redirect(shop_nearby)

def shop_remove(request, id_shop):
    if not request.user.is_authenticated:
        return redirect("/")

    Shop.objects.get(id=id_shop).remove_like_by(request.user)
    return redirect(shop_liked)

def shop_dislike(request, id_shop):
    if not request.user.is_authenticated:
        return redirect("/")

    Shop.objects.get(id=id_shop).add_dislike_by(request.user)
    return redirect(shop_nearby)
