from shops.models import Shop
from random import random



#Generate Random data for table Shops
for i in range(1,34):
    Shop.objects.create(name="Shop {}".format(i),
                        description="This is a description for Shop number {}".format(i),
                        latitude=random()*10,
                        longitude=random()*10)
