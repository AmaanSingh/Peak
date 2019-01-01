from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import validate_email

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "chat/index.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "chat/main.html", context)

def login_view(request):
    if request.method == 'GET':
        return render(request, "chat/index.html")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "chat/index.html", {"message": "Invalid credentials."})

def logout_view(request):
            logout(request)
            return render(request, "chat/index.html")

def signup_view(request):
    if request.method == 'GET':
        return render(request, "chat/new.html")
    if request.method == 'POST':
        username = request.POST["username1"]
        password = request.POST["password1"]
        email = request.POST["email1"]
        first_name = request.POST["Firstname"]
        last_name = request.POST["Lastname"]
        user = authenticate(request, username=username,email=email,password=password, last_name=last_name, first_name= first_name)
        
        if user is None:
                user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name,first_name= first_name)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "chat/new.html", {"message": "Sorry, this account is already created."})
