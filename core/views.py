from allauth.account.views import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, UpdateView

from core.models import Application, Profile
from core.utils import AjaxableResponseMixin


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LoginForm()
        context['signup_form'] = SignupForm()
        context["application_list"] = Application.objects.all()
        return context


index = IndexView.as_view()


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

    context = {}
    return redirect("index")


def logout_view(request):
    logout(request)
    context = {}
    return redirect("index")


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
    return redirect("index")


class ProfileView(TemplateView):
    template_name = "core/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["application_list"] = Application.objects.all()
        return context


class ProfileUpdate(AjaxableResponseMixin, UpdateView):
    model = Profile
    fields = ['picture', 'applications']
