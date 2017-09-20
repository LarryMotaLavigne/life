from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return HttpResponse('You\'re at the index. <a href="/secure">Secure</a>')


@login_required
def secure(request):
    return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')