import gmplot
from django.contrib.auth.models import User
from shops.models import Shop


gmap = gmplot.GoogleMapPlotter(34.033958, -5.005365, 13)
gmap.apikey = "AIzaSyCklslPNLaCTUpMDHvR8dOgz_F6-B2O4rY"

for shop in Shop.objects.all():
    gmap.marker(shop.latitude, shop.longitude, "red", title=shop.name)

gmap.draw("map.html")
