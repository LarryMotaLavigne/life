from allauth.account.views import *
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


class ProfileView(TemplateView):
    template_name = "core/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["application_list"] = Application.objects.all()
        return context


profile = ProfileView.as_view()


class ProfileUpdate(AjaxableResponseMixin, UpdateView):
    model = Profile
    fields = ['picture', 'applications']
