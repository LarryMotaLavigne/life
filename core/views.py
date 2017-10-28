from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "lol"}
    return render(request, "core/index.html", context)
    #
    # return HttpResponse('You\'re at the index. <a href="/secure">Secure</a>')


def homepage(request):
    context = {"title": "homepage"}
    return render(request, "core/login.html", context)


@login_required
def secure(request):
    return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')


