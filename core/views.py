from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "core/index.html", context)


def login_view(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Login':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
        elif request.POST.get('submit') == 'Register':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password)
        elif request.POST.get('submit') == 'Logout':
            logout(request)
            user = None
        # Login user
        if user is not None:
            login(request, user)

    context = {}
    return render(request, "core/index.html", context)


def logout_view(request):
    logout(request)
    context = {}
    return render(request, "core/index.html", context)
