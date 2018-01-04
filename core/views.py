from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from core.models import Application


def index(request):
    application_list = Application.objects.all()
    context = {"application_list": application_list}
    return render(request, "core/index.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

    context = {}
    return redirect(index)


def logout_view(request):
    logout(request)
    context = {}
    return redirect(index)


def signup_view(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            if user is not None:
                login(request, user)

    context = {}
    return redirect(index)


def profile_view(request):
    context = {}
    return render(request, "core/profile.html", context)
