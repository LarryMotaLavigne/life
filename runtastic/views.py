from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"test": "lol"}
    return render(request, "core/index.html", context)
