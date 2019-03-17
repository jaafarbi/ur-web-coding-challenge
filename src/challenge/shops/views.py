from django.shortcuts import render, redirect
from .models import Shop


from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin..

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
    context = {}
    context["shops_active"] = "active"
    context["ask_for_position"] = True

    if request.POST:
        latitude = float(request.POST.get("lat",""))
        longitude = float(request.POST.get("long",""))
        request.session["latitude"] = latitude
        request.session["longitude"] = longitude
        context["ask_for_position"] = False

    if "latitude" in request.session and "longitude"in request.session:
        context["ask_for_position"] = False
        shops = sorted(list(shops), key=lambda x: distance(request.session["latitude"], request.session["longitude"], x.latitude, x.longitude))

    group_4_shops = split_n_items_per_part(shops, 4)

    context["group_4_shops"] = group_4_shops

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
