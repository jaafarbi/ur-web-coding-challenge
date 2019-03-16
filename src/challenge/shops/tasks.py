from celery import shared_task
from shops.models import Shop
from django.contrib.auth.models import User

@shared_task
def remove_dislike_async(shop_id, user_id):
    Shop.objects.get(id=shop_id).remove_dislike_by(User.objects.get(id=user_id))
