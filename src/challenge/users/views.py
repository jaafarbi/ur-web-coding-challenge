from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_signin(request):
    if request.user.is_authenticated:
        return redirect("/shops")
        
    if request.POST:
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/shops")

        return render(request, "index.html", {})
    else:
        return render(request, "index.html", {})

def user_signup(request):
    if request.POST:
        email = request.POST.get("email","")
        password = request.POST.get("password","")
        print(email, password)
        User.objects.create_user(email, email=email, password=password)
        return render(request, "index.html", {"signup_complete": True})
    else:
        return render(request, "index.html", {"signup": True})

def user_signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
