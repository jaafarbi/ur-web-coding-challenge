"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import user_signin, user_signup, user_signout
from shops.views import shop_nearby, shop_liked, shop_like, shop_dislike, shop_remove

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_signin),
    path('signup',user_signup),
    path('signout',user_signout),
    path('shops',shop_nearby),
    path('preferred_shops',shop_liked),
    path('like_shop/<int:id_shop>',shop_like),
    path('dislike_shop/<int:id_shop>',shop_dislike),
    path('remove_shop/<int:id_shop>',shop_remove),


]
