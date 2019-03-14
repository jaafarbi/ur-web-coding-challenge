from django.contrib import admin
from .models import Shop, DislikedShop

# Register your models here.
admin.site.register(Shop)
admin.site.register(DislikedShop)
