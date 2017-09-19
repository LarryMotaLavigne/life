from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"title": "lol"}
    return render(request, "poker/index.html", context)

def session(request):
    context = {}
    return render(request, "poker/session.html", context)

def result(request, session_id):
    context = {}
    return render(request, "poker/result.html", context)
