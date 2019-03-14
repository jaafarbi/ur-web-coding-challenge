from django.db import models
from django.contrib.auth.models import User
import datetime


def default_time_now():
    return datetime.datetime.time(datetime.datetime.now())
# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    liked_by_users = models.ManyToManyField(User, blank=True, related_name="shops_liked")
    disliked_by_users = models.ManyToManyField(User, blank=True, related_name="shops_disliked", through="DislikedShop")



    def is_liked_by(self, user):
        # Check if a shop is liked by a given user
        if len(self.liked_by_users.all()) <= 0:
            return False
        else:
            return user in self.liked_by_users.all()

    def liked_by(user):
        # Returns list of all shops liked by a given user
        return Shop.objects.filter(liked_by_users=user)

    def all_but_liked_by(user):
        # Returns list of all shops liked by a given user
        return Shop.objects.exclude(liked_by_users=user)

    def add_like_by(self, user):
        # Perfom like by user on the shop
        self.liked_by_users.add(user)

    def remove_like_by(self, user):
        # Remove the like by user from the shop
        self.liked_by_users.remove(user)

    def is_liked_by(self, user):
        # Check if a shop is liked by a given user
        if len(self.liked_by_users.all()) <= 0:
            return False
        else:
            return user in self.liked_by_users.all()

    def disliked_by(user):
        # Returns list of all shops disliked by a given user
        return Shop.objects.filter(disliked_by_users=user)

    def all_but_disliked_by(user):
        # Returns list of all shops disliked by a given user
        return Shop.objects.exclude(disliked_by_users=user)

    def add_dislike_by(self, user):
        # Perfom dislike by user on the shop
        if DislikedShop.objects.filter(users=user, shops=self).count() == 0:
            DislikedShop.objects.create(users=user, shops=self)
        else:
            DislikedShop.objects.filter(users=user, shops=self).update(date_disliked=default_time_now())
        # remove_disliked_shop.apply_async((self.id, user.id), countdown=10)

    def remove_dislike_by(self, user):
        # Remove the dislike by user from the shop
        if DislikedShop.objects.filter(users=user, shops=self).count() > 0:
            DislikedShop.objects.remove(users=user, shops=self)



class DislikedShop(models.Model):
    amount_time_disapear_in_s = 3600*2
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    shops = models.ForeignKey(Shop, on_delete=models.CASCADE)
    date_disliked = models.TimeField(default=default_time_now, null=False, blank=False)
