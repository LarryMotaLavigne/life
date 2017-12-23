from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def index(request):
    context = {"title": "lol"}
    return render(request, "poker/index.html", context)

def session(request):
    context = {}
    return render(request, "poker/index.html", context)

def result(request, session_id):
    context = {}
    return render(request, "poker/index.html", context)
