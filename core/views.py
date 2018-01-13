from allauth.account.views import *
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from core.forms import UserForm, ProfileForm
from core.models import Application
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


class ProfileView(TemplateView, AjaxableResponseMixin):
    template_name = "core/profile.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserForm(instance=self.request.user)
        context['profile_form'] = ProfileForm(instance=self.request.user.profile)
        context["application_list"] = Application.objects.all()
        return context


profile = ProfileView.as_view()
