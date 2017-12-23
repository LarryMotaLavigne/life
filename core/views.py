from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "core/index.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

    context = {}
    return render(request, "core/index.html", context)


def logout_view(request):
    logout(request)
    context = {}
    return render(request, "core/index.html", context)


def signup_view(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                login(request, user)

    context = {}
    return render(request, "core/index.html", context)
