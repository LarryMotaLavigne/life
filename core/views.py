from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"title": "lol"}
    return render(request, "core/index2.html", context)
