from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"test": "lol"}
    return render(request, "runtastic/index.html", context)
