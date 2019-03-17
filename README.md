# Web Coding Challenge: United Remote

I completed the coding challenge by using Python 3.7 and some libraries:
* **Django:** Web Framework.
* **Celery & Rabbitmq:** For executing asynchronous tasks like removing dislikes after a delay.
* **gmplot:** Just because it's fun to be able to plot shops on maps. :smile:

## Implemented Features
* Ability to sign up using email & password.
* Ability to sign in using email & password.
* Ability to list the shops sorted by distance. _(using HTML5 geolocation)_
* Ability to add a shop to a list of preferred shops (which do not appear in the default list).
* Ability to dislike shops for a certain amount of time.
* Ability to display the list of preferred shops.
* Ability to remove a shop from the preferred shops list.

## Database Structure
![Database Structure](/tables.png)  


I used the model User from the django library as the User table, created the model Shop in which I added a simple M2M relationship to User (here represented as LikedShop) and finally added another M2M relationship to User through the model DislikedShop with an extra filed *date_disliked*.


## What's next?
* Use AJAX to refresh the list of shops when liked/disliked.  
* Comment/Document code.  
* Put more effort on the page design.
