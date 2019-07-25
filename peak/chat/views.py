from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.debug import sensitive_post_parameters
from .forms import UserRegisterForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "chat/index.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "chat/main.html", context)
@sensitive_post_parameters("password")
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
            return render(request, "chat/index.html", {"message": "The username or password you've entered doesn't match any account."})

def logout_view(request):
            logout(request)
            return render(request, "chat/index.html")

@sensitive_post_parameters("password")
def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST["username1"]
        password = request.POST["password1"]
        first_name = request.POST["Firstname"]
        last_name = request.POST["Lastname"]
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            form.save()
        if user is not None:
            return render(request, "chat/new.html", {"message": "Sorry, this account has already been created. If you have forgotten your password, proceed to the password reset page."})
        try:
            if user is None:
                user = User.objects.create_user(username=username, password=password, last_name=last_name,first_name= first_name)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except IntegrityError as e:
            return render(request, "chat/new.html", {"message": "Sorry, this username isn't available. Please try another."})
    return render(request, 'chat/new.html', {'form': UserRegisterForm})

def reset_view(request):
    return render(request, "chat/forget.html")
